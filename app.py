# Lap Time trakcer code for Project!3 

import mysql.connector
from mysql.connector import Error

def insertLapTime(driverId, trackId, carId, lap_time_ms):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'MySQLpass3449!?',
            database = 'laptimes'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = """
                INSERT INTO lapRecords (driverId, trackId, carId, lap_time_ms)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (driverId, trackId, carId, lap_time_ms))
            connection.commit()
            print("Data successfully committed to the database!")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")



# --- TEST CALL ---
# This actually triggers the recipe above using dummy IDs and a 1-minute, 24-second lap time
insertLapTime(driverId=1, trackId=1, carId=1, lap_time_ms=84000)
