from django.urls import path

from . import views

urlpatterns = [
    path('new/<int:diagnosispk>', views.diagnosisprocedure_create, name='diagnosisprocedure_new'),
    path('edit/<int:pk>', views.diagnosisprocedure_update, name='diagnosisprocedure_edit'),
    path('delete/<int:pk>', views.diagnosisprocedure_delete, name='diagnosisprocedure_delete')
]