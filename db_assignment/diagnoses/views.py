from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms
from models.models import Diagnosis, Animal, Appointment
from django.db.models import Q
from operator import attrgetter


class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['code', 'description', 'status', 'treatment']
        widgets = {
            'description': forms.Textarea(attrs={ 'class' : 'text-input', 'size':200}),
            'treatment': forms.Textarea(attrs={'class': 'text-input', 'size': 200})
        }

        labels = {
            'code' : 'Code',
            'description' : 'Description',
            'status' : 'Status',
            'treatment' : 'Treatment'
        }


def diagnosis_list(request, template_name='diagnoses/diagnosis_list.html'):
    diagnosis = Diagnosis.objects.all()
    data = {}
    data['object_list'] = diagnosis
    return render(request, template_name, data)


def diagnosis_view(request, pk, template_name='diagnoses/diagnosis_detail.html'):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    return render(request, template_name, {'object': diagnosis})


# todo delete
def diagnosis_create(request, template_name='diagnoses/diagnosis_form.html'):
    form = DiagnosisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('diagnosis_list')
    return render(request, template_name, {'form': form})


def diagnosis_create_for_appointment(request, appointmentpk, template_name='diagnoses/diagnosis_form.html'):

    form = DiagnosisForm(request.POST or None)
    appointment = get_object_or_404(Appointment, pk=appointmentpk)
    form.instance.appointment = appointment
    if form.is_valid():
        form.save()
        return  redirect('animal_view', appointment.animal.pk)
    return render(request, template_name, {'form':form})


def diagnosis_update(request, pk, template_name='diagnoses/diagnosis_form.html'):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    animal = get_object_or_404(Animal, pk= diagnosis.appointment.animal.pk)
    form = DiagnosisForm(request.POST or None, instance=diagnosis)
    if form.is_valid():
        form.save()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'form': form})


def diagnosis_delete(request, pk, template_name='diagnoses/diagnosis_confirm_delete.html'):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    animal = get_object_or_404(Animal, pk= diagnosis.appointment.animal.pk)
    if request.method == 'POST':
        diagnosis.delete()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'object': diagnosis})


def diagnosis_search(request, template_name='diagnoses/diagnosis_search.html'):
    query = request.GET.get('q')
    results = Diagnosis.objects.filter(Q(code__icontains=query) | Q(description__icontains=query) | Q(status__icontains=query) |
                                    Q(treatment__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def diagnosis_sort(request, template_name='diagnoses/diagnosis_sort.html'):
    results = Diagnosis.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
