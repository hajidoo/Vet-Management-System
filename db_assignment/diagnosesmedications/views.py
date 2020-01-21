from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from models.models import DiagnosisMedication, Diagnosis


class DiagnosismedicationForm(ModelForm):
    class Meta:
        model = DiagnosisMedication
        fields = ['medication']
        labels = {'medication' : 'Medication'}


def diagnosismedication_create(request, diagnosispk,
                               template_name='diagnosesmedications/diagnosismedication_form.html'):
    form = DiagnosismedicationForm(request.POST or None)
    diagnosis = get_object_or_404(Diagnosis, pk=diagnosispk)
    form.instance.diagnosis = diagnosis
    if form.is_valid():
        form.save()
        return redirect('diagnosis_view', diagnosis.pk )
    return render(request, template_name, {'form' : form })


def diagnosismedication_update(request, pk,
                               template_name='diagnosesmedications/diagnosismedication_form.html'):
    instance = get_object_or_404(DiagnosisMedication, pk=pk)
    form = DiagnosismedicationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('diagnosis_view', instance.diagnosis.pk)
    return render(request, template_name, {'form' : form})


def diagnosismedication_delete(request, pk,
                               template_name='diagnosesmedications/diagnosismedication_confirm_delete.html'):
    instance = get_object_or_404(DiagnosisMedication, pk=pk)
    diagnosis = instance.diagnosis
    if request.method == 'POST':
        instance.delete()
        return redirect('diagnosis_view', diagnosis.pk )
    return render(request, template_name, {'object': instance})