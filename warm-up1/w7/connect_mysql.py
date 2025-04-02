import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .credential file
load_dotenv(".credential")

try:
    # Get credentials from environment variables
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
        # ssl_disabled=True
    )
    cursor = conn.cursor()

    # Get MySQL Data Directory (Storage Location)
    cursor.execute("SHOW VARIABLES LIKE 'datadir';")
    datadir = cursor.fetchone()[1]

    # Get All Databases and Their Sizes
    cursor.execute("""
        SELECT table_schema AS 'Database',
               ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)'
        FROM information_schema.tables
        GROUP BY table_schema
        ORDER BY SUM(data_length + index_length) DESC;
    """)

    # Fetch All Databases Info
    databases = cursor.fetchall()

    # Print the Results
    print(f"📌 MySQL Data Directory: {datadir}\n")
    print("📂 List of Databases and Their Sizes:")
    print("-" * 50)
    for db in databases:
        print(f"📁 Database: {db[0]} | 🏷️ Size: {db[1]} MB | 📍 Location: {datadir}{db[0]}")
    
    # Close Connection
    cursor.close()
    conn.close()

except pymysql.MySQLError as err:
    print(f"❌ Error: {err}")
