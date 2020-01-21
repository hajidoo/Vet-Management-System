from django.urls import path

from . import views

urlpatterns = [
    path('', views.medication_list, name='medication_list'),
    path('view/<str:pk>', views.medication_view, name='medication_view'),
    path('new', views.medication_create, name='medication_new'),
    path('edit/<str:pk>', views.medication_update, name='medication_edit'),
    path('delete/<str:pk>', views.medication_delete, name='medication_delete'),
    path('search', views.medication_search, name='medication_search'),
    path('sort/', views.medication_sort, name='medication_sort')
]