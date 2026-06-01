-- Tracking fastest lap times per session


CREATE DATABASE IF NOT EXISTS LapTimes;
USE LapTimes;

-- Lookup Tables
CREATE TABLE IF NOT EXISTS Drivers (
	driverID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(50) NOT NULL
);
    
    
CREATE TABLE cars(
		carId INT auto_increment PRIMARY KEY,
        carYear INT NOT NULL,
        make VARCHAR(25) NOT NULL,
        model VARCHAR(25) NOT NULL
);
        
CREATE TABLE tracks (
	trackId INT auto_increment PRIMARY KEY,
    trackName VARCHAR(50) NOT NULL,
    location VARCHAR(100), 
    lengthMiles DECIMAL(4,2)
);

-- This links all our data together
CREATE TABLE sessions (
	sessionId INT auto_increment PRIMARY KEY,
    driverId INT,
    carId INT,
    trackId INT,
    sessionDate DATE NOT NULL,
    weatherConditions VARCHAR(35),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
    FOREIGN KEY (carId) REFERENCES cars(carId),
    FOREIGN KEY (trackId) REFERENCES tracks(trackId)
    );
    
    
CREATE TABLE lapRecords (
	lapId INT auto_increment PRIMARY KEY,
    sessionId INT,
    lapNumber INT NOT NULL,
    lap_time_ms INT NOT NULL, -- stored in milliseconds
    is_valid BOOLEAN DEFAULT TRUE, -- Flags track cuts
    FOREIGN KEY (sessionId) REFERENCES sessions(sessionId)
);

    
	
ALTER TABLE drivers 
RENAME COLUMN laastName TO lastName;

-- Test Records
INSERT INTO drivers (driverID, firstName, lastName) VALUES
(1, 'Max', 'Verstappen');

ALTER TABLE cars
RENAME COLUMN year TO carYear;

INSERT INTO cars (carId, carYear, make, model) VALUES
(1, 2017, 'FERRARI', 'F1 W15');


INSERT INTO tracks (trackId, trackName, location, lengthMiles) VALUES 
(1, 'Monza Circuit', 'Italy', 3.60);


 -- Creating a practice session linking the table
 
 INSERT INTO sessions (sessionId, driverId, carId, trackId, sessionDate, weatherConditions)
 VALUES(
 1, 1, 1, 1, '2026-05-31', 'Sunny'
 );
 
 ALTER TABLE lapTimes
 RENAME TO lapRecords;
 
 INSERT INTO lapRecords (lapId, sessionId, lapNumber, lap_time_ms, is_valid) VALUES
 (1, 1, 1, 106500, TRUE)