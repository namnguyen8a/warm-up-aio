from dotenv import load_dotenv
import os
import requests  # To make HTTP requests
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Function get patient via name, id
get_patient_id = {
    "name": "get_patient_via_id",
    "description": "Gets a patient record via id",
    "parameters": {
        "type": "object",
        "properties": {
            "PatientID": {
                "type": "integer",  # integer because the PatientID is an integer in FastAPI
                "description": "The patient id, e.g. 1 for patient name Nguyen Van A ",
            },
        },
        "required": ["PatientID"],  # FullName is required
    },
}

get_patient_name = {
    "name": "get_patient_via_name",
    "description": "Gets a patient record via name",
    "parameters": {
        "type": "object",
        "properties": {
            "FullName": {
                "type": "string",  # string because the FullName is an string in FastAPI
                "description": "The patient name, e.g. Nam",
            },
        },
        "required": ["FullName"],  # FullName is required
    },
}


# Configure the client and tools
client = genai.Client(api_key=GEMINI_API_KEY)
tools = types.Tool(function_declarations=[get_patient_id, get_patient_name])  # Added both functions
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Bệnh nhân tên là Trần Thị B này là ai ?",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    
    # Handle function call for getting a specific patient by patient_id
    if function_call.name == "get_patient_via_id":
        PatientID = function_call.args["PatientID"]  # Use the patient_id from the arguments
        
        # Call your FastAPI endpoint to get a specific patient by ID
        user_data = requests.get(f"http://127.0.0.1:8000/patients/{PatientID}").json()
        
        # Format the API result to send back to Gemini
        api_result = f"The patient with ID {PatientID} is: {user_data[0]}"
        
        # Output the result directly
        print(f"API result: {api_result}")
    elif function_call.name == "get_patient_via_name":
        FullName = function_call.args["FullName"]  # Use the patient_name from the arguments
        
        # Call your FastAPI endpoint to get a specific patient by ID
        user_data = requests.get(f"http://127.0.0.1:8000/patients/name/{FullName}").json()
        
        # Format the API result to send back to Gemini
        api_result = f"The patient with name {FullName} is: {user_data[0]}"
        
        # Output the result directly
        print(f"API result: {api_result}")
    else:
        print("Unknown function called by Gemini.")
else:
    print("No function call found in the response.")
    print(response.text)