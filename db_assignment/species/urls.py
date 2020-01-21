from django.urls import path

from . import views

urlpatterns = [
    path('', views.species_list, name='species_list'),
    path('view/<str:pk>', views.species_view, name='species_view'),
    path('new', views.species_create, name='species_new'),
    path('edit/<str:pk>', views.species_update, name='species_edit'),
    path('delete/<str:pk>', views.species_delete, name='species_delete'),
    path('search', views.species_search, name='species_search'),
    path('sort/', views.species_sort, name='species_sort')
]