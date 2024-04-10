CREATE DATABASE example4;
USE example4;

CREATE TABLE user_register(
	id_user int PRIMARY KEY, # 
    name_t1 varchar(255),
    surname varchar(255),
    password_t1 varchar(255),
    time_zone varchar(255) DEFAULT 'UTC-3',
    gender varchar(255),
    cellphone int #un numero de celular no tiene valores alphanumericos, así que no hay necesidad para hacerlo varchar
);

CREATE TABLE registry(
	id_ingreso int PRIMARY KEY,
    id_user int,
    entry datetime DEFAULT current_timestamp, #es una fecha, así que es un fecha con tiempo
    FOREIGN KEY (id_user) REFERENCES user_register(id_user)
);

CREATE TABLE counter(
	id_register int PRIMARY KEY auto_increment, #un registro requiere un identificador pero este es automatico asi se mantiene consistente
    id_user int,
    login int, #numero de veces que se conecta por lo que es un entero
    FOREIGN KEY (id_user) references user_register(id_user)
);

INSERT INTO user_register (id_user, name_t1, surname, password_t1, time_zone, gender, cellphone)
VALUES
(1, 'Alice', 'Smith', 'password123', 'UTC-3', 'Female', 1234567890),
(2, 'Bob', 'Johnson', 'securepass', 'UTC-5', 'Male', 987654321),
(3, 'Charlie', 'Brown', 'pass123', 'UTC-3', 'Male', 555555555),
(4, 'David', 'Williams', '123456', 'UTC-4', 'Male', 111222333),
(5, 'Emma', 'Taylor', 'qwerty', 'UTC-3', 'Female', 999888777),
(6, 'Frank', 'Wilson', 'abc123', 'UTC-4', 'Male', 444333222),
(7, 'Grace', 'Anderson', 'p@ssw0rd', 'UTC-3', 'Female', 777888999),
(8, 'Henry', 'Martinez', 'password', 'UTC-5', 'Male', 666777888);

INSERT INTO registry (id_ingreso, id_user, entry)
VALUES
(1, 1, '2024-04-04 08:00:00'),
(2, 2, '2024-04-04 08:15:00'),
(3, 3, '2024-04-04 08:30:00'),
(4, 4, '2024-04-04 08:45:00'),
(5, 5, '2024-04-04 09:00:00'),
(6, 6, '2024-04-04 09:15:00'),
(7, 7, '2024-04-04 09:30:00'),
(8, 8, '2024-04-04 09:45:00');

INSERT INTO counter (id_user, login)
VALUES
(1, 10),
(2, 15),
(3, 20),
(4, 25),
(5, 30),
(6, 35),
(7, 40),
(8, 45);

DROP TABLE counter;