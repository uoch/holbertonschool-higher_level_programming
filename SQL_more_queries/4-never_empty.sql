-- The DEFAULT keyword specifies a default value for the "id" column. In this case, the default value is 1.
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1,  name VARCHAR(256) NOT NULL);