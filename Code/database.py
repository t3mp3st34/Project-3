#Project!3
# Handles all SQL communication

#Please ensure you have the MySQL Connector/Python installed and a MySQL server running with the appropriate database and table setup before using this code.
#Please replace the connection parameters (host, user, password, database) with your actual MySQL server credentials and database name.

#The databse download will be availabe for download on Git


import mysql.connector
from mysql.connector import Error

#Database connection 

def dbConnect():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host = 'yourhostname',
            user = 'youruser',
            password = 'yourpass',
            database = 'laptimes'
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None


def insertLapTime(SessionId, lapNumber, lap_time_ms):
    connection = None
    
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

#This will pull the best lap time for a given driver and track, excluding the current session, and return it for comparison with the current lap time.

def getLapComparison(driverId, trackId, currentSessionId):
    connection = Noine
    cursor = None
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'MySQLpass3449',
            database = 'laptimes'
        )







