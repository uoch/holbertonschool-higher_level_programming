-- The 'CREATE' DATABASE statement creates a new database called hbtn_0d_2. The IF NOT EXISTS clause checks if the database already exists, and if it does, the statement does nothing.
-- The 'CREATE' USER statement creates a new user with the username 'user_0d_2' and the password 'user_0d_2_pwd'. The IF NOT EXISTS clause checks if the user already exists, and if it does, the statement does nothing.
-- The 'GRANT' SELECT statement grants the SELECT privilege on all tables in the database hbtn_0d_2 to the user 'user_0d_2'@'localhost'. This allows the user to only retrieve data from the database and not modify it.
-- Note that you may need to modify the script depending on your MySQL server configuration and the hostname or IP address of the client connecting to the server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
