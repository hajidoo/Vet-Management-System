from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django import forms
from django.db.models import Q
from models.models import Note, Animal
from operator import attrgetter


class NoteForm(ModelForm):
    class Meta:
        model = Note
        widgets = {'content': forms.Textarea(attrs={ 'class' : 'text-input', 'size':200})}
        fields = ['date', 'content']
        labels = {
            'date' : 'Date (YYYY-MM-DD)',
            'content' : 'Content'
        }


def note_list(request, template_name='notes/note_list.html'):
    note = Note.objects.all()
    data = {}
    data['object_list'] = note
    return render(request, template_name, data)


def note_view(request, pk, template_name='notes/note_detail.html'):
    note = get_object_or_404(Note, pk=pk)
    return render(request, template_name, {'object': note})


def note_create(request, template_name='notes/note_form.html'):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, template_name, {'form': form})


def note_create_for_animal(request, animalpk, template_name='notes/note_form.html'):
    form = NoteForm(request.POST or None)
    animal = get_object_or_404(Animal, pk=animalpk)
    form.instance.animal = animal
    if form.is_valid():
        form.save()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'form':form})


def note_update(request, pk, template_name='notes/note_form.html'):
    note = get_object_or_404(Note, pk=pk)
    animal = note.animal
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'form': form})


def note_delete(request, pk, template_name='notes/note_confirm_delete.html'):
    note = get_object_or_404(Note, pk=pk)
    animal = note.animal
    if request.method == 'POST':
        note.delete()
        return redirect('animal_view', animal.pk)
    return render(request, template_name, {'object': note})


def note_search(request, template_name='notes/note_search.html'):
    query = request.GET.get('q')
    results = Note.objects.filter(Q(date__icontains=query) | Q(content__icontains=query))
    data={}
    data['object_list'] = results
    return render(request, template_name, data)


def note_sort(request, template_name='notes/note_sort.html'):
    answer = request.GET['dropdown']
    results = Note.objects.all()
    data={}
    data['object_list'] = sorted(results, key=attrgetter(answer))
    return render(request, template_name, data)
