from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms
from django.db.models import Q
from models.models import Species
from operator import attrgetter


class SpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = ['name', 'description', 'obligatoryprocedures', 'legalissues']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'text-input', 'size': 200}),
            'legalissues': forms.Textarea(attrs={'class': 'text-input', 'size': 200})
        }
        labels = {
            'name' : 'Name',
            'description' : 'Description',
            'obligatoryprocedures' : 'Obligatory Procedures',
            'legalissues' : 'Legal Issues'
        }


def species_list(request, template_name='species/species_list.html'):
    species = Species.objects.all()
    data = {}
    data['object_list'] = species
    return render(request, template_name, data)


def species_view(request, pk, template_name='species/species_detail.html'):
    species = get_object_or_404(Species, pk=pk)
    return render(request, template_name, {'object': species})


def species_create(request, template_name='species/species_form.html'):
    form = SpeciesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('species_list')
    return render(request, template_name, {'form': form})


def species_update(request, pk , template_name='species/species_form.html'):
    species = get_object_or_404(Species, pk=pk)
    form = SpeciesForm(request.POST or None, instance=species)
    if form.is_valid():
        form.save()
        return redirect('species_list')
    return render(request, template_name, {'form': form})


def species_delete(request, pk, template_name='species/species_confirm_delete.html'):
    species = get_object_or_404(Species,pk=pk)
    if request.method == 'POST':
        species.delete()
        return redirect('species_list')
    return render(request, template_name, {'object': species})


def species_search(request, template_name='species/species_search.html'):
    query = request.GET.get('q')
    results = Species.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(obligatoryprocedures__icontains=query) |
                                    Q(legalissues__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def species_sort(request, template_name='species/species_sort.html'):
    results = Species.objects.all()
    data = {}
    if 'dropdown' in request.GET:
        answer = request.GET['dropdown']
        data['object_list'] = sorted(results, key=attrgetter(answer))
    else:
        data['object_list'] = results
    return render(request, template_name, data)
