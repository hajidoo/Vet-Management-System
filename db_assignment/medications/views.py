from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms
from django.db.models import Q
from models.models import Medication
from operator import attrgetter


class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'cost', 'otherdetails']
        widgets = {'otherdetails': forms.Textarea(attrs={'class': 'text-input', 'size': 200})}
        labels = {
            'name' : 'Name',
            'cost' : 'Cost',
            'otherdetails' : 'Other Details'
        }


def medication_list(request, template_name='medications/medication_list.html'):
    medication = Medication.objects.all()
    data = {}
    data['object_list'] = medication
    return render(request, template_name, data)


def medication_view(request, pk, template_name='medications/medication_detail.html'):
    medication = get_object_or_404(Medication, pk=pk)
    return render(request, template_name, {'object': medication})


def medication_create(request, template_name='medications/medication_form.html'):
    form = MedicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medication_list')
    return render(request, template_name, {'form': form})


def medication_update(request, pk, template_name='medications/medication_form.html'):
    medication = get_object_or_404(Medication, pk=pk)
    form = MedicationForm(request.POST or None, instance=medication)
    if form.is_valid():
        form.save()
        return redirect('medication_list')
    return render(request, template_name, {'form': form})


def medication_delete(request, pk, template_name='medications/medication_confirm_delete.html'):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == 'POST':
        medication.delete()
        return redirect('medication_list')
    return render(request, template_name, {'object': medication})


def medication_search(request, template_name='medications/medication_search.html'):
    query = request.GET.get('q')
    results = Medication.objects.filter(Q(name__icontains=query) | Q(cost__icontains=query) | Q(otherdetails=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def medication_sort(request, template_name='medications/medication_sort.html'):
    results = Medication.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)


