DROP DATABASE IF EXISTS Vet;
CREATE DATABASE Vet;
USE Vet;

-- tables
-- Table: Animals
CREATE TABLE Animals (
    AnimalID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    RegistrationDate DATE NOT NULL,
    Birth DATE NOT NULL,
    Gender VARCHAR(6) NOT NULL,
    Height FLOAT NOT NULL,
    Weight FLOAT NOT NULL,
    OtherDetails VARCHAR(200) NULL,
    Clients_ClientID INT NOT NULL,
    Species_Name VARCHAR(20) NOT NULL,
    Vets_VetID INT NULL,
    CONSTRAINT AnimalPK PRIMARY KEY (AnimalID)
);

CREATE INDEX Animals_Name_idx ON Animals (Name);

CREATE INDEX Animals_ClientID_idx ON Animals (Clients_ClientID);

-- Table: Appointments
CREATE TABLE Appointments (
	AppointmentID INT NOT NULL AUTO_INCREMENT,
    Date DATE NOT NULL,
    Status VARCHAR(20) NOT NULL,
    Details VARCHAR(20) NOT NULL,
    Vets_VetID INT NOT NULL,
    Animals_AnimalID INT NOT NULL,
    CONSTRAINT Appointments_pk PRIMARY KEY (AppointmentID)
);

CREATE INDEX Appointments_Status_idx ON Appointments (Status);

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    RegistrationDate DATE NOT NULL,
    CONSTRAINT Clients_pk PRIMARY KEY (ClientID)
);

CREATE INDEX Clients_LastName_idx1 USING BTREE ON Clients (LastName);


-- Table: Diagnoses

CREATE TABLE Diagnoses (
    DiagnosisID INT NOT NULL AUTO_INCREMENT,
    Code VARCHAR(20) NOT NULL,
    Description VARCHAR(200) NOT NULL,
    Status VARCHAR(20) NOT NULL,
    Treatment VARCHAR(200) NOT NULL,
    Appointments_AppointmentID INT NOT NULL,
    CONSTRAINT Diagnoses_pk PRIMARY KEY (DiagnosisID)
);

CREATE INDEX Diagnoses_Code_idx ON Diagnoses (Code);

CREATE INDEX Diagnoses_Status_idx ON Diagnoses (Status);

-- Table: Diagnoses_MedicalProcedures
CREATE TABLE Diagnoses_MedicalProcedures (
	Diagnoses_MedicalProceduresID INT NOT NULL auto_increment,
    Diagnoses_DiagnosisID INT NOT NULL,
    MedicalProcedures_Name VARCHAR(20) NOT NULL,
    CONSTRAINT Diagnoses_MedicalProcedures_pk PRIMARY KEY (Diagnoses_MedicalProceduresID)
);

-- Table: Diagnoses_Medications
CREATE TABLE Diagnoses_Medications (
	Diagnoses_MedicationsID INT NOT NULL auto_increment,
    Medications_Name VARCHAR(20) NOT NULL,
    Diagnoses_DiagnosisID INT NOT NULL,
    CONSTRAINT Diagnoses_Medications_pk PRIMARY KEY (Diagnoses_MedicationsID)
);

-- Table: MedicalProcedures
CREATE TABLE MedicalProcedures (
    Name VARCHAR(20) NOT NULL,
    Cost FLOAT NOT NULL,
    OtherDetails VARCHAR(200) NULL,
    CONSTRAINT MedicalProcedures_pk PRIMARY KEY (Name)
);

CREATE INDEX MedicalProcedures_Cost_idx USING BTREE ON MedicalProcedures (Cost);

-- Table: Medications
CREATE TABLE Medications (
    Name VARCHAR(20) NOT NULL,
    Cost FLOAT NOT NULL,
    OtherDetails VARCHAR(200) NULL,
    CONSTRAINT Medications_pk PRIMARY KEY (Name)
);

CREATE INDEX Medications_Cost_idx USING BTREE ON Medications (Cost);

-- Table: Notes
CREATE TABLE Notes (
    NoteID INT NOT NULL AUTO_INCREMENT,
    NoteDate DATE NOT NULL,
    Content VARCHAR(200) NOT NULL,
    Animals_AnimalID INT NOT NULL,
    CONSTRAINT Notes_pk PRIMARY KEY (NoteID)
);

CREATE INDEX Notes_Date_idx ON Notes (NoteDate);

-- Table: Species
CREATE TABLE Species (
    Name VARCHAR(20) NOT NULL,
    ObligatoryProcedures VARCHAR(20) NOT NULL,
    Description VARCHAR(200) NOT NULL,
    LegalIssues VARCHAR(200) NOT NULL,
    CONSTRAINT Species_pk PRIMARY KEY (Name)
);

CREATE INDEX Species_Name_idx ON Species (Name);

-- Table: Vets
CREATE TABLE Vets (
    VetID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Qualifications VARCHAR(20) NOT NULL,
    Birth DATE NOT NULL,
    CONSTRAINT Vets_pk PRIMARY KEY (VetID)
);


-- foreign keys
-- Reference: Animals_Clients (table: Animals)
ALTER TABLE Animals ADD CONSTRAINT Animals_Clients FOREIGN KEY Animals_Clients (Clients_ClientID)
    REFERENCES Clients (ClientID)
    ON DELETE CASCADE;

-- Reference: Animals_Species (table: Animals)
ALTER TABLE Animals ADD CONSTRAINT Animals_Species FOREIGN KEY Animals_Species (Species_Name)
    REFERENCES Species (Name);

-- Reference: Animals_Vets (table: Animals)
ALTER TABLE Animals ADD CONSTRAINT Animals_Vets FOREIGN KEY Animals_Vets (Vets_VetID)
    REFERENCES Vets (VetID);

-- Reference: Appointments_Animals (table: Appointments)
ALTER TABLE Appointments ADD CONSTRAINT Appointments_Animals FOREIGN KEY Appointments_Animals (Animals_AnimalID)
    REFERENCES Animals (AnimalID)
    ON DELETE CASCADE;

-- Reference: Appointments_Vets (table: Appointments)
ALTER TABLE Appointments ADD CONSTRAINT Appointments_Vets FOREIGN KEY Appointments_Vets (Vets_VetID)
    REFERENCES Vets (VetID);

-- Reference: Diagnoses_Appointments (table: Diagnoses)
ALTER TABLE Diagnoses ADD CONSTRAINT Diagnoses_Appointments FOREIGN KEY Diagnoses_Appointments (Appointments_AppointmentID)
    REFERENCES Appointments (AppointmentID)
    ON DELETE CASCADE;

-- Reference: Diagnoses_MedicalProcedures_Diagnoses (table: Diagnoses_MedicalProcedures)
ALTER TABLE Diagnoses_MedicalProcedures ADD CONSTRAINT Diagnoses_MedicalProcedures_Diagnoses FOREIGN KEY Diagnoses_MedicalProcedures_Diagnoses (Diagnoses_DiagnosisID)
    REFERENCES Diagnoses (DiagnosisID)
    ON DELETE CASCADE;

-- Reference: Diagnoses_MedicalProcedures_MedicalProcedures (table: Diagnoses_MedicalProcedures)
ALTER TABLE Diagnoses_MedicalProcedures ADD CONSTRAINT Diagnoses_MedicalProcedures_MedicalProcedures FOREIGN KEY Diagnoses_MedicalProcedures_MedicalProcedures (MedicalProcedures_Name)
    REFERENCES MedicalProcedures (Name);

-- Reference: Diagnoses_Medications_Diagnoses (table: Diagnoses_Medications)
ALTER TABLE Diagnoses_Medications ADD CONSTRAINT Diagnoses_Medications_Diagnoses FOREIGN KEY Diagnoses_Medications_Diagnoses (Diagnoses_DiagnosisID)
    REFERENCES Diagnoses (DiagnosisID)
    ON DELETE CASCADE;

-- Reference: Diagnoses_Medications_Medications (table: Diagnoses_Medications)
ALTER TABLE Diagnoses_Medications ADD CONSTRAINT Diagnoses_Medications_Medications FOREIGN KEY Diagnoses_Medications_Medications (Medications_Name)
    REFERENCES Medications (Name);

-- Reference: Notes_Animals (table: Notes)
ALTER TABLE Notes ADD CONSTRAINT Notes_Animals FOREIGN KEY Notes_Animals (Animals_AnimalID)
    REFERENCES Animals (AnimalID)
    ON DELETE CASCADE;

-- End of file.

