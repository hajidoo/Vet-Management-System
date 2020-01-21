from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms
from django.core.paginator import Paginator 

from django.db.models import Q
from models.models import Animal, Client, Vet, Appointment
from appointments.views import AppointmentForm
from operator import attrgetter


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'registrationdate', 'birth', 'gender',
                  'height', 'weight', 'otherdetails', 'species', 'vet']
        widgets = {'otherdetails': forms.Textarea(attrs={'class': 'text-input', 'size': 200})}
        labels = {
            'name' : 'Name',
            'registrationdate' :  'Registration Date (YYYY-MM-DD)',
            'birth' : 'Birth (YYYY-MM-DD)',
            'gender' : 'Gender',
            'height' : 'Height',
            'weight' :  'Weight',
            'otherdetails' : 'Other Details',
            'species' : 'Species',
            'vet' : 'Vet'
        }


# show all animals
def animal_list(request, template_name='animals/animal_list.html'):
    animal = Animal.objects.all()

    data = {}
    data['object_list'] = animal
    # paginator = Paginator(animal, 10) 
    return render(request, template_name, data)


# show animal's details
def animal_view(request, pk, template_name='animals/animal_detail.html'):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, template_name, {'object': animal, 'last_visit': animal.last_visit})


def animal_create(request, template_name='animals/animal_form.html'):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('animal_list')
    return render(request, template_name, {'form': form})


# add an animal and go back to client
def animal_create_for_client(request, clientpk, template_name='animals/animal_form.html'):
    form = AnimalForm(request.POST or None)
    form.instance.client = get_object_or_404(Client,pk=clientpk)
    if form.is_valid():
        form.save()
        return redirect('animal_view', form.instance.pk)
    return render(request, template_name, {'form': form})


def animal_new_appointment(request, pk, template_name='animals/animal_form.html'):
    form = AnimalForm(request.POST or None)
    animal = get_object_or_404(Animal, pk=pk)
    form.instance.animal = animal
    if form.is_valid():
        appointment = form.instance
        appointment.custom_save()
        appointment.new_visit
        return redirect('animal_list', appointment.vet.pk)
    return render(request, template_name, {'form': form})


# edit an animal and go back to the client
def animal_update(request, pk, template_name='animals/animal_form.html'):
    animal = get_object_or_404(Animal, pk=pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'form': form})


# delete an animal and go back to the client
def animal_delete(request, pk, template_name='animals/animal_confirm_delete.html'):
    animal = get_object_or_404(Animal, pk=pk)
    client = animal.client
    if request.method == 'POST':
        animal.delete()
        return redirect('client_view', client.pk)
    return render(request, template_name, {'object': animal})


def animal_search(request, template_name='animals/animal_search.html'):
    query = request.GET.get('q')
    results = Animal.objects.filter(Q(name__icontains=query) | Q(registrationdate__icontains=query) | Q(birth__icontains=query) |
                                    Q(gender__icontains=query) | Q(height__icontains=query) | Q(weight__icontains=query) |
                                    Q(otherdetails__icontains=query) |Q(vet__firstname__icontains=query) | Q(vet__lastname__icontains=query) |
                                    Q(species__name__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def animal_sort(request, template_name='animals/animal_sort.html'):
    results = Animal.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
