import streamlit as st
from llm_function_calling.gemini_function_calling import GEMINI_API_KEY, get_patient_id, get_patient_name
from google import genai
from google.genai import types
import requests

st.set_page_config(page_title="EMR Management")
st.title("EMR Management")

BASE_URL = "http://127.0.0.1:8000"

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Chat input
user_input = st.chat_input("Say something...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            try:
                client = genai.Client(api_key=GEMINI_API_KEY)
                tools = types.Tool(function_declarations=[get_patient_id, get_patient_name])
                config = types.GenerateContentConfig(tools=[tools])
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_input,
                    config=config,
                )
                if response.candidates[0].content.parts[0].function_call:
                    function_call = response.candidates[0].content.parts[0].function_call
                    if function_call.name == "get_patient_via_id":
                        PatientID = function_call.args["PatientID"]
                        user_data = requests.get(f"{BASE_URL}/patients/{PatientID}").json()
                        api_result = f"The patient with ID {PatientID} is: {user_data[0]}"
                        # Send API result back to LLM for natural language response
                        follow_up_response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=[
                                types.Content(role="user", parts=[types.Part(text=f"Đây là dữ liệu của bệnh nhân: {api_result}. Hãy trả lời thật tự nhiên.")])
                            ]
                        )
                        reply = follow_up_response.text
                    elif function_call.name == "get_patient_via_name":
                        FullName = function_call.args["FullName"]
                        user_data = requests.get(f"{BASE_URL}/patients/name/{FullName}").json()
                        api_result = f"The patient with name {FullName} is: {user_data[0]}"
                        # Send API result back to LLM for natural language response
                        follow_up_response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=[
                                types.Content(role="user", parts=[types.Part(text=f"Đây là dữ liệu của bệnh nhân: {api_result}. Hãy trả lời thật tự nhiên.")])
                            ]
                        )
                        reply = follow_up_response.text
                    else:
                        reply = response.text
                else:
                    reply = response.text
                st.session_state.chat_history
            except Exception as e:
                reply = f"⚠️ Error: {str(e)}"
            st.markdown(reply)

    # Add response to history
    st.session_state.chat_history.append(("assistant", reply))
