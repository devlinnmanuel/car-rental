-- DROP DATABASE students;
CREATE DATABASE students;
USE students;

CREATE TABLE student (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(10) UNIQUE NOT NULL,
    nama VARCHAR(200) NOT NULL,
    tgl_lahir DATE NOT NULL
);

INSERT INTO student (nim, nama, tgl_lahir) VALUES
('12345', 'Budi', '2005-03-21'),
('35611', 'Susi', '2005-07-11'),
('57743', 'Andi', '2005-11-03');

SELECT * FROM student;