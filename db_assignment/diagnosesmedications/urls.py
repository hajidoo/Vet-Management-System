from django.urls import path

from . import views

urlpatterns = [
    path('new/<int:diagnosispk>', views.diagnosismedication_create, name='diagnosismedication_new'),
    path('edit/<int:pk>', views.diagnosismedication_update, name='diagnosismedication_edit'),
    path('delete/<int:pk>', views.diagnosismedication_delete, name='diagnosismedication_delete')
]