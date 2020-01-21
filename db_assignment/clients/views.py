from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from operator import attrgetter

# Create your views here.
from models.models import Client


# Function Based Views
class ClientForm(ModelForm): # formularz do tworzenia/edycji klienta
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'registrationdate']
        labels = {
            'firstname' : 'First Name',
            'lastname' : 'Last Name',
            'registrationdate' : 'Registration Date (YYYY-MM-DD)'
        }

def client_list(request, template_name='clients/client_list.html'):
    client = Client.objects.all()
    data = {}
    data['object_list'] = client
    return render(request, template_name, data)


def client_view(request, pk, template_name='clients/client_detail.html'):
    client = get_object_or_404(Client,pk=pk)
    return render(request, template_name, {'object':client})


def client_create(request, template_name='clients/client_form.html'):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_view', form.instance.pk)
    return render(request,template_name, {'form':form})


def client_update(request, pk , template_name='clients/client_form.html'):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_view', pk)
    return render(request,template_name, {'form':form})

def client_delete(request, pk, template_name='clients/client_confirm_delete.html'):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request,template_name,{'object':client})


def client_search(request, template_name='clients/client_search.html'):
    query = request.GET.get('q')
    results = Client.objects.filter(Q(firstname__icontains=query) |Q(lastname__icontains=query) | Q(registrationdate__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def client_sort(request, template_name='clients/client_sort.html'):
    results = Client.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
