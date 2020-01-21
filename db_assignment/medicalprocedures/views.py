from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms

from django.db.models import Q
from models.models import MedicalProcedure
from operator import attrgetter


class MedicalProcedureForm(ModelForm):
    class Meta:
        model = MedicalProcedure
        fields = ['name', 'cost', 'otherdetails']
        widgets = {'otherdetails': forms.Textarea(attrs={'class': 'text-input', 'size': 200})}
        labels = {
            'name' : 'Name',
            'cost' : 'Cost',
            'otherdetails' : 'Other Details'
        }


def medicalprocedure_list(request, template_name='medicalprocedures/medicalprocedure_list.html'):
    medicalprocedure = MedicalProcedure.objects.all()
    data = {}
    data['object_list'] = medicalprocedure
    return render(request, template_name, data)


def medicalprocedure_view(request, pk, template_name='medicalprocedures/medicalprocedure_detail.html'):
    medicalprocedure = get_object_or_404(MedicalProcedure, pk=pk)
    return render(request, template_name, {'object': medicalprocedure})


def medicalprocedure_create(request, template_name='medicalprocedures/medicalprocedure_form.html'):
    form = MedicalProcedureForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicalprocedure_list')
    return render(request, template_name, {'form': form})


def medicalprocedure_update(request, pk, template_name='medicalprocedures/medicalprocedure_form.html'):
    medicalprocedure = get_object_or_404(MedicalProcedure, pk=pk)
    form = MedicalProcedureForm(request.POST or None, instance=medicalprocedure)
    if form.is_valid():
        form.save()
        return redirect('medicalprocedure_list')
    return render(request, template_name, {'form': form})


def medicalprocedure_delete(request, pk, template_name='medicalprocedures/medicalprocedure_confirm_delete.html'):
    medicalprocedure = get_object_or_404(MedicalProcedure, pk=pk)
    if request.method == 'POST':
        medicalprocedure.delete()
        return redirect('medicalprocedure_list')
    return render(request, template_name, {'object': medicalprocedure})


def medicalprocedure_search(request, template_name='medicalprocedures/medicalprocedure_search.html'):
    query = request.GET.get('q')
    results = MedicalProcedure.objects.filter(Q(name__icontains=query) | Q(cost__icontains=query) | Q(otherdetails=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def medicalprocedure_sort(request, template_name='medicalprocedures/medicalprocedure_sort.html'):
    results = MedicalProcedure.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
