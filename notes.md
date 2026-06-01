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

