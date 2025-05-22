from fastapi import APIRouter
from app.database.databases import get_execute, get_execute_variable, get_connection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.model import Patient

router = APIRouter()

# Create patient record
@router.post("/patients/", tags=["patients"])
async def create_patient(patient: Patient):
    query = """
        INSERT INTO PATIENT (PatientID, FullName, BirthDate, Gender, Address, MedicalID)
        VALUES
        (%s, %s, %s, %s, %s, %s);
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (patient.PatientID, patient.FullName, patient.BirthDate, patient.Gender, patient.Address, patient.MedicalID))
        conn.commit()
    return {"message": "Create patient record successful!"}

# Query all the current patients
@router.get("/patients/", tags=["patients"])
async def get_patients():
    query = "SELECT * FROM PATIENT;"
    res = get_execute(query)
    json_res = jsonable_encoder(res)
    return JSONResponse(content=json_res)

# Query the patients via ID
@router.get("/patients/{patient_id}", tags=["patients"])
async def get_patient_id(patient_id: int):
    query = "SELECT * FROM patient WHERE PatientID = %s;"
    res = get_execute_variable(query, patient_id)
    json_res = jsonable_encoder(res)
    return JSONResponse(content=json_res)

# Query the patients via name
@router.get("/patients/name/{patient_name}", tags=["patients"]) 
async def get_patient_name(patient_name: str):
    query = f"SELECT * FROM patient WHERE FullName LIKE '%{patient_name}%';"
    res = get_execute(query)
    json_res = jsonable_encoder(res)
    return JSONResponse(content=json_res)

# Update the patient
@router.put("/patients/{patient_id}", tags=["patients"])
async def update_patient_id(patient_id: int, patient: Patient):
    query = """
        UPDATE PATIENT
        SET FullName = %s,
            BirthDate = %s,
            Gender = %s,
            Address = %s,
            MedicalID = %s
        WHERE PatientID = %s;
        """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (
                patient.FullName,
                patient.BirthDate,
                patient.Gender,
                patient.Address,
                patient.MedicalID,
                patient_id
            ))
            conn.commit()
    return {"message": f"Update patient {patient_id} successfully!"}

# Delete the patient
@router.delete("/patients/{patient_id}", tags=["patients"])
async def delete_patient_id(patient_id: int):
    query = "DELETE FROM PATIENT WHERE PatientID = %s;"
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (patient_id,))
            conn.commit()
    return {"message": f"Delete patient {patient_id} successfully!"}

@router.get("/patients/{patient_id}/history", tags=["patients"])
async def get_patient_id_history(patient_id: int):
    query = """
        SELECT  p.fullname, v.symptoms, v.diagnosis, pre.medicationname,
                pre.dosage, pre.frequency, t.result
        FROM    patient p
        INNER JOIN visit v
        ON  p.patientid = v.patientid
        INNER JOIN prescription pre
        ON v.visitid = pre.visitid
        INNER JOIN test t
        ON v.visitid = t.visitid
        WHERE
            p.patientid = %s;
    """
    res = get_execute_variable(query, patient_id)
    json_res = jsonable_encoder(res)
    return JSONResponse(content=json_res)

