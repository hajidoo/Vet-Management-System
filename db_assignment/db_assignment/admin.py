from django.contrib import admin

# Register your models here.
from models.models import Client, Animal, Appointment, Diagnosis, MedicalProcedure, Medication, \
    DiagnosisMedicalProcedure, DiagnosisMedication, Note, Species, Vet

admin.register(Client)
admin.register(Animal)
admin.register(Appointment)
admin.register(Diagnosis)
admin.register(MedicalProcedure)
admin.register(Medication)
admin.register(DiagnosisMedicalProcedure)
admin.register(DiagnosisMedication)
admin.register(Note)
admin.register(Species)
admin.register(Vet)

