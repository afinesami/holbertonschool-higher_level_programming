--script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server

CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE
IFNOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, UNIQUE(id), PRIMARY KEY(id));
