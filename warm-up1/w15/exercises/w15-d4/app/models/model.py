from pydantic import BaseModel
from datetime import date

class Patient(BaseModel):
    PatientID: int
    FullName: str
    BirthDate: date
    Gender: str
    Address: str
    MedicalID: str

class Visit(BaseModel):
    VisitID: int
    PatientID: int
    VisitDate: str
    Symptoms: str
    Diagnosis: str
    ImagingResults: str

class Prescription(BaseModel):
    PrescriptionID: int
    VisitID: int
    MedicationName: str
    Dosage: str
    Frequency: str
    TreatmentPlan: str
    Procedures: str
    FollowUp: str

class Test(BaseModel):
    TestID: int
    VisitID: int
    TestType: str
    Result: str
    TestDate: str
    ResponsibleDoctor: str
    ReceivingTime: str
    MedicalFacility: str
    Department: str