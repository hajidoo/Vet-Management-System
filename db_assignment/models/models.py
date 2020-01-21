# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.db import connection

from models.validators import validate_positive


class Client(models.Model):
    clientid = models.AutoField(db_column='ClientID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    registrationdate = models.DateField(db_column='RegistrationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'

    def __str__(self):
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return reverse('client_edit', kwargs={'pk': self.pk})




class Animal(models.Model):
    animalid = models.AutoField(db_column='AnimalID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    registrationdate = models.DateField(db_column='RegistrationDate')  # Field name made lowercase.
    birth = models.DateField(db_column='Birth')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', validators=[validate_positive])  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', validators=[validate_positive])  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey('Client', models.CASCADE, db_column='Clients_ClientID')  # Field name made lowercase.
    species = models.ForeignKey('Species', models.CASCADE, db_column='Species_Name')  # Field name made lowercase.
    vet = models.ForeignKey('Vet', models.SET_NULL, db_column='Vets_VetID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Animals'

    def __str__(self):
        return self.name

    def _get_last_visit(self):
        with connection.cursor() as cursor:
            cursor.execute("select last_visit(%s)", [self.pk])
            row = cursor.fetchone()
        if row == (None,):
            return "Never"

        return row[0]

    last_visit = property(_get_last_visit)



class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='AppointmentID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=20)  # Field name made lowercase.
    vet = models.ForeignKey('Vet', models.CASCADE, db_column='Vets_VetID')  # Field name made lowercase.
    animal = models.ForeignKey(Animal, models.CASCADE, db_column='Animals_AnimalID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appointments'

    def __str__(self):
        return str(self.date) + " " + str(self.vet) + " " + str(self.animal)

    def custom_save(self):
        with connection.cursor() as cursor:
            cursor.callproc('new_visit', [self.date, self.status, self.details, self.vet.pk, self.animal.pk])
            row = cursor.fetchone()
        return row



class Diagnosis(models.Model):
    diagnosisid = models.AutoField(db_column='DiagnosisID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    treatment = models.CharField(db_column='Treatment', max_length=200)  # Field name made lowercase.
    appointment = models.ForeignKey(Appointment, models.CASCADE, db_column='Appointments_AppointmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diagnoses'

    def __str__(self):
        return "diagnosis " + str(self.pk) + self.description

class MedicalProcedure(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', validators=[validate_positive])  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MedicalProcedures'

    def __str__(self):
        return self.name + " " + str(self.cost)


class Medication(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', validators=[validate_positive])  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medications'

    def __str__(self):
        return self.name + " " + str(self.cost)

class DiagnosisMedicalProcedure(models.Model):
    diagnosis_medicalprocedureid = models.AutoField(db_column='Diagnoses_MedicalProceduresID', primary_key=True)  # Field name made lowercase.
    diagnosis = models.ForeignKey(Diagnosis, models.CASCADE, db_column='Diagnoses_DiagnosisID')  # Field name made lowercase.
    medicalprocedure = models.ForeignKey('MedicalProcedure', models.CASCADE, db_column='MedicalProcedures_Name')

    class Meta:
        managed = False
        db_table = 'Diagnoses_MedicalProcedures'

    def __str__(self):
        return  self.medicalprocedure.name + " " + str(self.medicalprocedure.cost)


class DiagnosisMedication(models.Model):
    diagnosis_medicationid = models.AutoField(db_column='Diagnoses_MedicationsID', primary_key=True)  # Field name made lowercase.
    medication = models.ForeignKey('Medication', models.CASCADE, db_column='Medications_Name')  # Field name made lowercase.
    diagnosis = models.ForeignKey(Diagnosis, models.CASCADE, db_column='Diagnoses_DiagnosisID')

    class Meta:
        managed = False
        db_table = 'Diagnoses_Medications'

    def __str__(self):
        return  self.medication.name + " " + str(self.medication.cost)


class Note(models.Model):
    noteid = models.AutoField(db_column='NoteID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='NoteDate')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200)  # Field name made lowercase.
    animal = models.ForeignKey(Animal, models.CASCADE, db_column='Animals_AnimalID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notes'

    def get_absolute_url(self):
        return reverse('note_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return "note " + self.pk + str(self.date)


class Species(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    obligatoryprocedures = models.CharField(db_column='ObligatoryProcedures', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    legalissues = models.CharField(db_column='LegalIssues', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Species'

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('species_edit', kwargs={'pk': self.pk})


class Vet(models.Model):
    vetid = models.AutoField(db_column='VetID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    qualifications = models.CharField(db_column='Qualifications', max_length=20)  # Field name made lowercase.
    birth = models.DateField(db_column='Birth')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vets'

    def __eq__(self, other):
        return str(self) == str(other)

    def __lt__(self, other):
        return str(self) < str(other)


    def __gt__(self, other):
        return str(self) > str(other)


    def __str__(self):
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return reverse('vet_edit', kwargs={'pk': self.pk})
