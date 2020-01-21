from django.contrib import admin

# Register your models here.
from models.models import Client, Animal, Appointment, Diagnosis, MedicalProcedure, Medication, \
    DiagnosisMedicalProcedure, DiagnosisMedication, Note, Species, Vet

admin.site.register(Client)
admin.site.register(Animal)
admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(MedicalProcedure)
admin.site.register(Medication)
admin.site.register(DiagnosisMedicalProcedure)
admin.site.register(DiagnosisMedication)
admin.site.register(Note)
admin.site.register(Species)
admin.site.register(Vet)

