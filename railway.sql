# CREATE DATABASE railway;
USE railway;
DROP TABLE IF EXISTS loginTest;
CREATE TABLE loginTest(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    user_password VARCHAR(20)
);
INSERT INTO loginTest(username, user_password) VALUES ('admin', 'pass');
