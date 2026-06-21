#Project!3
# Handles all SQL communication

#Please ensure you have the MySQL Connector/Python installed and a MySQL server running with the appropriate database and table setup before using this code.
#Please replace the connection parameters (host, user, password, database) with your actual MySQL server credentials and database name.

#The databse download will be availabe for download on Git


import mysql.connector
from mysql.connector import Error
import config


#MySQL connection
def dbConnection():
    try: #Establishes and returns MYSQL connection 
        connection = mysql.connector.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.database
        )
        return connection
    except Error as e:
        print(f"Database connection failure: {e}")
        return None 

# logs a completed lap time using reusable connection bridge
def insertLapTime(lapNumber, lap_time_ms):

    connection = dbConnection();
    if connection is None:
        print("Cannot log lap: Database connection offline")
        return

    cursor = None
    try: 
        cursor = connection.cursor()
        query = """
            INSERT INTO lapRecords (sessionId, lapNumber, lap_time_ms, is_valid)
            VALUES (%s, %s, %s, TRUE)
            """
        
        cursor.execute(query, (1, lapNumber, lap_time_ms))
        connection.commit()
        print(f"Lap {lapNumber} successfully saved!")

    except Error as e:
        print(f"Failed to execute query: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
    
   

#Run this to test connection 
if __name__ == "__main__":
    print("[*] Testing databse connection..")

    test_connection = dbConnection()

    if test_connection and test_connection.is_connected():
        print("Successfully connected to 'laptimes' MySQL database!")

        test_connection.close()
        print("Database connection closed safely")

        print("Testing lap record insertion...")
        insertLapTime(lapNumber=1, lap_time_ms=84500)
    
    else:
        print("Could not establish a connection")

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



<<<<<<< HEAD
#def getLapComparison(driverId, trackId, carId, sessionId):
    
=======

>>>>>>> 4b46de6f6330c2344281aa4818061e759a782d6f



