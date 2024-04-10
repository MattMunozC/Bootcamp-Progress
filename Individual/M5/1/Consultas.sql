CREATE USER 'Explorador' identified by 'ELSEÑORDELANOCHE';

GRANT SELECT ON world.* to 'Explorador';

use world;

SELECT count(*) FROM city;

SELECT * FROM country ORDER BY NAME DESC;

SELECT count(DISTINCT countrylanguage.language) as 'languages' FROM country 
LEFT JOIN countrylanguage ON country.code=countrylanguage.countrycode 
WHERE Region='South America';

CREATE DATABASE example1;
use Example1;

CREATE TABLE operadores(
	RUN int PRIMARY KEY,
    name text,
    surname text,
    dir text,
    email text
);

CREATE TABLE USUARIOS(
	Id_coder int PRIMARY KEY,
    name varchar(255),
    surname varchar(255),
    email varchar(255),
    phone int
);

CREATE TABLE CAPACITACION(
	id_course int PRIMARY KEY,
    name text,
    schedule text
);


INSERT INTO operadores (RUN, name, surname, dir, email) VALUES
(12345678, 'John', 'Doe', '123 Main St', 'john.doe@example.com'),
(23456789, 'Jane', 'Smith', '456 Elm St', 'jane.smith@example.com'),
(34567890, 'Michael', 'Johnson', '789 Oak St', 'michael.johnson@example.com'),
(45678901, 'Emily', 'Brown', '101 Pine St', 'emily.brown@example.com'),
(56789012, 'David', 'Martinez', '222 Maple St', 'david.martinez@example.com'),
(67890123, 'Sarah', 'Garcia', '333 Cedar St', 'sarah.garcia@example.com'),
(78901234, 'Daniel', 'Lopez', '444 Birch St', 'daniel.lopez@example.com'),
(89012345, 'Jessica', 'Rodriguez', '555 Walnut St', 'jessica.rodriguez@example.com'),
(90123456, 'Christopher', 'Perez', '666 Spruce St', 'christopher.perez@example.com'),
(12312312, 'Anna', 'Taylor', '777 Fir St', 'anna.taylor@example.com');


INSERT INTO USUARIOS (Id_coder, name, surname, email, phone) VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', 1234567890),
(2, 'Bob', 'Smith', 'bob.smith@example.com', 2345678901),
(3, 'Charlie', 'Brown', 'charlie.brown@example.com', 3456789012),
(4, 'Diana', 'Williams', 'diana.williams@example.com', 4567890123),
(5, 'Eva', 'Garcia', 'eva.garcia@example.com', 5678901234),
(6, 'Frank', 'Martinez', 'frank.martinez@example.com', 6789012345),
(7, 'Gina', 'Lopez', 'gina.lopez@example.com', 7890123456),
(8, 'Henry', 'Davis', 'henry.davis@example.com', 8901234567),
(9, 'Isabel', 'Rodriguez', 'isabel.rodriguez@example.com', 9012345678),
(10, 'Jack', 'Lee', 'jack.lee@example.com', 1122334455);

INSERT INTO CAPACITACION (id_course, name, schedule) VALUES
(1, 'Introduction to Python Programming', 'Monday and Wednesday, 9:00 AM - 11:00 AM'),
(2, 'Web Development with JavaScript', 'Tuesday and Thursday, 2:00 PM - 4:00 PM'),
(3, 'Data Science Fundamentals', 'Monday, Wednesday, and Friday, 1:00 PM - 3:00 PM'),
(4, 'Introduction to Machine Learning', 'Tuesday and Thursday, 10:00 AM - 12:00 PM'),
(5, 'Database Management with SQL', 'Monday and Wednesday, 3:00 PM - 5:00 PM'),
(6, 'Mobile App Development with React Native', 'Tuesday and Thursday, 9:00 AM - 11:00 AM'),
(7, 'Cybersecurity Basics', 'Monday and Wednesday, 10:00 AM - 12:00 PM'),
(8, 'Cloud Computing Fundamentals', 'Tuesday and Thursday, 1:00 PM - 3:00 PM'),
(9, 'UI/UX Design Principles', 'Monday, Wednesday, and Friday, 2:00 PM - 4:00 PM'),
(10, 'Project Management Essentials', 'Tuesday and Thursday, 3:00 PM - 5:00 PM');


use sakila;

SELECT count(DISTINCT film_id) as 'titulos en inventario' FROM inventory;

SELECT rental.rental_id,film.title,count(*) as 'rentada' FROM rental 
LEFT JOIN inventory ON rental.inventory_id=inventory.inventory_id 
LEFT JOIN film on inventory.film_id=film.film_id 
GROUP BY film.title ORDER BY rentada DESC;
    
    