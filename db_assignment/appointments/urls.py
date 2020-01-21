from django.urls import path

from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('view/<int:pk>', views.appointment_view, name='appointment_view'),
    path('new', views.appointment_create, name='appointment_new'),
    path('new/<int:animalpk>', views.appointment_create_for_animal, name='appointment_new_for_animal'),
    path('edit/<int:pk>', views.appointment_update, name='appointment_edit'),
    path('delete/<int:pk>', views.appointment_delete, name='appointment_delete'),
    path('search/', views.appointment_search, name='appointment_search'),
    path('sort/', views.appointment_sort, name='appointment_sort')
]