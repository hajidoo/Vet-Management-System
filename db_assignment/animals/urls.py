from django.urls import path

from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('view/<int:pk>', views.animal_view, name='animal_view'),
    path('new', views.animal_create, name='animal_new'),
    path('new/<int:clientpk>', views.animal_create_for_client, name='animal_new_for_client'),
    path('edit/<int:pk>', views.animal_update, name='animal_edit'),
    path('delete/<int:pk>', views.animal_delete, name='animal_delete'),
    path('search/', views.animal_search, name='animal_search'),
    path('sort/', views.animal_sort, name='animal_sort'),
    path('new_appointment/<int:pk>', views.animal_new_appointment, name='animal_new_appointment')
]