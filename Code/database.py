#Project!3
# Handles all SQL communication

import mysql.connector
from mysql.connector import Error

def insertLapTime(SessionId, lapNumber, lap_time_ms):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'MySQLpass3449',
            database = 'laptimes'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = """
                INSERT INTO lapRecords (SessionId, lapNumber, lap_time_ms)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (SessionId, lapNumber, lap_time_ms))
            connection.commit()
            print(f"Lap {lapNumber} ({lap_time_ms}ms) successfully committed to Session {SessionId}!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")



# --- TEST CALL ---
# This triggers the recipe above using dummy IDs and a laptime
#insertLapTime(SessionId=1, lapNumber=2, lap_time_ms=8400)


def getLapComparison(driverId, trackId, )




