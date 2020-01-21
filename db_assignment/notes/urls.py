from django.urls import path

from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('view/<int:pk>', views.note_view, name='note_view'),
    path('new', views.note_create, name='note_new'),
    path('new/<int:animalpk>', views.note_create_for_animal, name='note_new_for_animal'),
    path('edit/<int:pk>', views.note_update, name='note_edit'),
    path('delete/<int:pk>', views.note_delete, name='note_delete'),
    path('search', views.note_search, name='note_search'),
    path('sort/', views.note_sort, name='note_sort')
]