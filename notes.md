-- Database Schema outline:

        CREATE DATABASE IF NOT EXISTS RacingTelemetry;
USE RacingTelemetry;

-- 1. Create the independent lookup tables
CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_name VARCHAR(100) NOT NULL,
    team_name VARCHAR(100)
);

CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    car_model VARCHAR(100) NOT NULL,
    car_class VARCHAR(50)
);

CREATE TABLE tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    length_miles DECIMAL(4,2)
);

-- 2. Create the Sessions table (The bridge connecting Driver, Car, and Track)
CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    car_id INT,
    track_id INT,
    session_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
);

-- 3. Create the Lap Times table (Linked directly to a specific session)
CREATE TABLE lap_times (
    lap_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT,
    lap_number INT NOT NULL,
    lap_time_ms INT NOT NULL, -- Stored in milliseconds (e.g., 92450 for 1:32.450)
    is_valid BOOLEAN DEFAULT TRUE, -- To flag if someone cut a track or crashed
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);


-- SOME TABLE NAMES AND COLUMN NAMES HAVE BEEN CHANGED, SEE SCHEMA FOR REVISED NAMES IF NEEDED



-- THIS IS FOR THE CODE, USED AS OUTLINE, AGAIN SOME VARIABLE NAMES ARE DIFFERENT 

import mysql.connector
from mysql.connector import Error

def insert_lap_time(driver_id, track_id, lap_time_seconds):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='lap_time_tracker'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            query = """
            INSERT INTO laptimes (driver_id, track_id, lap_time) 
            VALUES (%s, %s, %s);
            """
            
            data = (driver_id, track_id, lap_time_seconds)
            
            cursor.execute(query, data)
            
            connection.commit()
            print(f"Successfully inserted lap time: {lap_time_seconds}s")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Example usage:
# insert_lap_time(1, 5, 84.32)
Why it works this way (Line-by-Line Breakdown):
import mysql.connector & from mysql.connector import Error

What: We are bringing in the driver that allows Python to speak SQL, plus a specific Error object to catch database hiccups.

Why: Python doesn't natively know how to talk to MySQL network protocols. This library acts as the translator.

connection = None & cursor = None

What: We initialize these variables as empty inside the function.

Why: If the connection fails immediately (e.g., wrong password), the code jumps to the finally block. If we didn't define these as None first, Python would throw a crash error saying "variable referenced before assignment" when trying to close them.

mysql.connector.connect(...)

What: Opens the actual network socket to your database.

Why: You must authenticate and target the specific schema (lap_time_tracker) before sending queries.

cursor = connection.cursor()

What: Creates a "Cursor" object.

Why: Think of the cursor like a blinking text cursor in a terminal, or a temporary workspace. It’s the object that actually transmits the SQL string to the server and holds the results coming back.

query = "... VALUES (%s, %s, %s);" & data = (...)

What: We split the SQL command and the actual data into two separate pieces. The %s act as placeholders.

Why (Crucial Security): This is called a Parameterized Query. You never want to use Python string formatting (like f"VALUES ({driver_id})"). If a user inputs malicious text, it can cause SQL Injection and wreck your database. Passing them separately forces MySQL to treat the data strictly as data, never as executable SQL code.

cursor.execute(query, data)

What: Combines the query and data safely and fires it at the MySQL engine.

connection.commit()

What: Tells the database to permanently save the changes.

Why: Databases use "transactions." When you insert data, it's held in a temporary staging area. If you don't call .commit(), your data will vanish the moment the script ends.

The finally: block

What: This code always runs, whether the script succeeded or crashed.

Why: Database connections are limited resources. If your script crashes but leaves the connection open, your MySQL server will eventually run out of available slots and lock everyone out. We must explicitly .close() the cursor and connection.


Here is structure outline for app:
[LapTimeTracker_Project] Project!3
  ├── database.py       <-- Handles all SQL communication
  ├── telemetry.py      <-- Handles reading the live simulation/game data
  └── main.py           <-- The automation engine that connects them and runs
  