from django.urls import path

from . import views

urlpatterns = [
    path('', views.medicalprocedure_list, name='medicalprocedure_list'),
    path('view/<str:pk>', views.medicalprocedure_view, name='medicalprocedure_view'),
    path('new', views.medicalprocedure_create, name='medicalprocedure_new'),
    path('edit/<str:pk>', views.medicalprocedure_update, name='medicalprocedure_edit'),
    path('delete/<str:pk>', views.medicalprocedure_delete, name='medicalprocedure_delete'),
    path('search', views.medicalprocedure_search, name='medicalprocedure_search'),
    path('sort', views.medicalprocedure_sort, name="medicalprocedure_sort")
]