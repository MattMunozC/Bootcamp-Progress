CREATE DATABASE SPRINT5;
USE SPRINT5;

CREATE USER "usuario" IDENTIFIED BY "123456";
GRANT ALL PRIVILEGES ON SPRINT5.* TO USUARIO;

CREATE TABLE USUARIO(
	id_usuario int primary key auto_increment,
    nombre varchar(255),
    apellido varchar(255),
    edad int,
    correo_electronico varchar(255),
    inicio_sesion int default 1
);

CREATE TABLE OPERADOR(
	id_operador int primary key auto_increment,
    nombre varchar(255),
    apellido varchar(255),
    edad int,
    email varchar(255),
    inicio_sesion int default 1
);

CREATE TABLE SOPORTE(
	id_usuario int,
    id_operador int,
    fecha datetime default NOW(),
    calificacion int,
    primary key(id_usuario,id_operador,fecha),
    foreign key(id_usuario) references usuario(id_usuario),
    foreign key(id_operador) references operador(id_operador)
);

INSERT INTO USUARIO (nombre, apellido, edad, email, inicio_sesion)
VALUES 
    ('John', 'Doe', 30, 'john.doe@example.com', 57),
    ('Jane', 'Smith', 25, 'jane.smith@example.com', 23),
    ('Michael', 'Johnson', 40, 'michael.johnson@example.com', 85),
    ('Emily', 'Brown', 35, 'emily.brown@example.com', 12),
    ('David', 'Wilson', 28, 'david.wilson@example.com', 96);
    
INSERT INTO OPERADOR (nombre, apellido, edad, email, inicio_sesion)
VALUES 
    ('Alice', 'Johnson', 35, 'alice.johnson@example.com', 42),
    ('Bob', 'Smith', 30, 'bob.smith@example.com', 17),
    ('Carol', 'Williams', 45, 'carol.williams@example.com', 75),
    ('Daniel', 'Brown', 28, 'daniel.brown@example.com', 91),
    ('Eva', 'Jones', 33, 'eva.jones@example.com', 63);
    
INSERT INTO SOPORTE (id_usuario, id_operador, calificacion) VALUES (1, 1, 5),
                                                               (2, 3, 4),
                                                               (3, 2, 3),
                                                               (4, 5, 2),
                                                               (5, 4, 1),
                                                               (2, 1, 5),
                                                               (3, 4, 3),
                                                               (1, 5, 4),
                                                               (4, 3, 2),
                                                               (5, 5, 1);

#3 OPERACIONES CON MEJOR EVALUACION
SELECT * FROM SOPORTE ORDER BY calificacion DESC LIMIT 3;
#3 OPERACIONES CON MENOR EVALUACION
SELECT * FROM SOPORTE ORDER BY calificacion ASC LIMIT 3;

#OPERADOR QUE MÁS HA SOPORTADO
SELECT operador.id_operador, CONCAT(OPERADOR.nombre," ", OPERADOR.apellido) as nombre_completo ,count(*) as operaciones 
	FROM SOPORTE LEFT JOIN OPERADOR ON SOPORTE.id_operador=OPERADOR.id_operador 
    GROUP BY OPERADOR.id_operador 
    ORDER BY operaciones DESC LIMIT 1;

#MENOS VECES USADO LA APP    
SELECT * FROM USUARIO ORDER BY inicio_sesion ASC LIMIT 1;

#AGREGAR 10 AÑOS A LOS 3 PRIMEROS
UPDATE USUARIO SET edad=edad+10 LIMIT 3;

#CAMBIAR NOMBRE
ALTER TABLE USUARIO CHANGE COLUMN correo_electronico email varchar(255);

#TODOS LOS OPERADORES MAYORES A 20

SELECT * FROM USUARIO WHERE edad>20;



