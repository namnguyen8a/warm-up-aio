import os
from dotenv import load_dotenv
import pymysql

load_dotenv("../../.credential")

def get_connection():
    return pymysql.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = "emrdb"
    )

# with get_connection() as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM PATIENT;")
#         print(cursor.fetchall())

def get_execute(query: str): 
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def get_execute_variable(query: str, id: int):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchall()

