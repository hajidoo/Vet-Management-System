from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.db.models import Q
from models.models import Appointment, Animal
from operator import attrgetter


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'status', 'details', 'vet']
        labels = {
            'date' : 'Date (YYYY-MM-DD)',
            'status' : 'Status',
            'details' : 'Details',
            'vet' : 'Vet'
        }


def appointment_list(request, template_name='appointments/appointment_list.html'):
    appointment = Appointment.objects.all()
    data = {}
    data['object_list'] = appointment
    return render(request, template_name, data)


def appointment_view(request, pk, template_name='appointments/appointment_detail.html'):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, template_name, {'object': appointment})


#todo is this even needed
def appointment_create(request, template_name='appointments/appointment_form.html'):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, template_name, {'form': form})


def appointment_create_for_animal(request, animalpk, template_name='appointments/appointment_form.html'):
    form = AppointmentForm(request.POST or None)
    animal = get_object_or_404(Animal, pk=animalpk)
    form.instance.animal = animal
    if form.is_valid():
        appointment = form.instance
        appointment.custom_save()
        return redirect('client_view', animal.client.pk)
    return render(request, template_name, {'form': form})


def appointment_update(request, pk, template_name='appointments/appointment_form.html'):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('client_view',appointment.animal.client.pk)
    return render(request, template_name, {'form': form})


def appointment_delete(request, pk, template_name='appointments/appointment_confirm_delete.html'):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('client_view',appointment.animal.client.pk)
    return render(request, template_name, {'object': appointment})


def appointment_search(request, template_name='appointments/appointment_search.html'):
    query = request.GET.get('q')
    results = Appointment.objects.filter(Q(details__icontains=query) | Q(date__icontains=query) | Q(status__icontains=query) |
                                         Q(vet__firstname__icontains=query) | Q(vet__lastname__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def appointment_sort(request, template_name='appointments/appointment_sort.html'):
    results = Appointment.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)

