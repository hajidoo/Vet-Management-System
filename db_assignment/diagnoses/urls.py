from django.urls import path

from . import views

urlpatterns = [
    path('', views.diagnosis_list, name='diagnosis_list'),
    path('view/<int:pk>', views.diagnosis_view, name='diagnosis_view'),
    path('new', views.diagnosis_create, name='diagnosis_new'),
    path('new/<int:appointmentpk>', views.diagnosis_create_for_appointment, name='diagnosis_new_for_appointment'),
    path('edit/<int:pk>', views.diagnosis_update, name='diagnosis_edit'),
    path('delete/<int:pk>', views.diagnosis_delete, name='diagnosis_delete'),
    path('search', views.diagnosis_search, name='diagnosis_search'),
    path('sort/', views.diagnosis_sort, name="diagnosis_sort")
]
