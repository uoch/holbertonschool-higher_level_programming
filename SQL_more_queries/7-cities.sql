-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa ;
use hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities 
(id INT NOT NULL AUTO_INCREMENT ,
name VARCHAR(256),
UNIQUE (id),
PRIMARY KEY (id))
FOREIGN KEY (state_id) REFERENCES states(id);