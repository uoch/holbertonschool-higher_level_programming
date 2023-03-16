-- The CREATE USER statement creates a new user with the username 'user_0d_1' and the password 'user_0d_1_pwd'. The IF NOT EXISTS clause checks if the user already exists, and if it does, the statement does nothing.
-- The GRANT ALL PRIVILEGES statement grants all privileges on all databases and tables to the user 'user_0d_1'@'localhost'. This allows the user to perform any action on the MySQL server.
-- Note that you may need to modify the script depending on your MySQL server configuration and the hostname or IP address of the client connecting to the server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';