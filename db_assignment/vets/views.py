from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.db.models import Q
from models.models import Vet
from operator import attrgetter


class VetForm(ModelForm):
    class Meta:
        model = Vet
        fields = ['firstname', 'lastname', 'qualifications', 'birth']
        labels = {
            'firstname' : 'First Name',
            'lastname' : 'Last Name',
            'qualifications' : 'Qualifications',
            'birth' : 'Birth (YYYY-MM-DD)'
        }


def vet_list(request, template_name='vets/vet_list.html'):
    vet = Vet.objects.all()
    data = {}
    data['object_list'] = vet
    return render(request, template_name, data)


def vet_view(request, pk, template_name='vets/vet_detail.html'):
    vet = get_object_or_404(Vet,pk=pk)
    return render(request, template_name, {'object': vet})


def vet_create(request, template_name='vets/vet_form.html'):
    form = VetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vet_list')
    return render(request, template_name, {'form': form})


def vet_update(request, pk, template_name='vets/vet_form.html'):
    vet = get_object_or_404(Vet, pk=pk)
    form = VetForm(request.POST or None, instance=vet)
    if form.is_valid():
        form.save()
        return redirect('vet_list')
    return render(request, template_name, {'form': form})


def vet_delete(request, pk, template_name='vets/vet_confirm_delete.html'):
    vet = get_object_or_404(Vet, pk=pk)
    if request.method == 'POST':
        vet.delete()
        return redirect('vet_list')
    return render(request, template_name, {'object': vet})


def vet_search(request, template_name='vets/vet_search.html'):
    query = request.GET.get('q')
    results = Vet.objects.filter(Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(qualifications__icontains=query) |
                                    Q(birth__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def vet_sort(request, template_name='vets/vet_sort.html'):
    results = Vet.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
