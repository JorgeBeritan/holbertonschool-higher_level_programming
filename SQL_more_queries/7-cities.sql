-- Create a table cities with reference a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, states_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (states_id) REFERENCES states(id));
