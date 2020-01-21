from django.urls import path

from . import views

urlpatterns = [
    path('', views.vet_list, name='vet_list'),
    path('view/<int:pk>', views.vet_view, name='vet_view'),
    path('new', views.vet_create, name='vet_new'),
    path('edit/<int:pk>', views.vet_update, name='vet_edit'),
    path('delete/<int:pk>', views.vet_delete, name='vet_delete'),
    path('search', views.vet_search, name='vet_search'),
    path('sort/', views.vet_sort, name='vet_sort')
]