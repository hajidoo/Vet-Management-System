from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from models.models import DiagnosisMedicalProcedure, Diagnosis


class DiagnosisprocedureForm(ModelForm):
    class Meta:
        model = DiagnosisMedicalProcedure
        fields = ['medicalprocedure']
        labels = {'medicalprocedure' : 'Medical Procedure'}


def diagnosisprocedure_create(request, diagnosispk,
                               template_name='diagnosesprocedures/diagnosisprocedure_form.html'):
    form = DiagnosisprocedureForm(request.POST or None)
    diagnosis = get_object_or_404(Diagnosis, pk=diagnosispk)
    form.instance.diagnosis = diagnosis
    if form.is_valid():
        form.save()
        return redirect('diagnosis_view', diagnosis.pk )
    return render(request, template_name, {'form' : form })


def diagnosisprocedure_update(request, pk,
                               template_name='diagnosesprocedures/diagnosisprocedure_form.html'):
    instance = get_object_or_404(DiagnosisMedicalProcedure, pk=pk)
    form = DiagnosisprocedureForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('diagnosis_view', instance.diagnosis.pk)
    return render(request, template_name, {'form' : form})


def diagnosisprocedure_delete(request, pk,
                               template_name='diagnosesprocedures/diagnosisprocedure_confirm_delete.html'):
    instance = get_object_or_404(DiagnosisMedicalProcedure, pk=pk)
    diagnosis = instance.diagnosis
    if request.method == 'POST':
        instance.delete()
        return redirect('diagnosis_view', diagnosis.pk )
    return render(request, template_name, {'object' : instance})
