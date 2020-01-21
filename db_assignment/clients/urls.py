from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('view/<int:pk>', views.client_view, name='client_view'),
    path('new', views.client_create, name='client_new'),
    path('edit/<int:pk>', views.client_update, name='client_edit'),
    path('delete/<int:pk>', views.client_delete, name='client_delete'),
    path('search/', views.client_search, name='client_search'),
    path('sort/', views.client_sort, name='client_sort')
]