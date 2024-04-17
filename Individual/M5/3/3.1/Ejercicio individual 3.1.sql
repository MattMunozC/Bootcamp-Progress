CREATE DATABASE inv_31;
USE inv_31;


CREATE TABLE PROFESORES(
	rut int primary key,
    nombre varchar(255),
    apellido varchar(255),
    salario int,
    fecha_contratacion date
);

CREATE TABLE CURSOS(
	id_cursos int primary key auto_increment,
    nombre text,
    costo_realizacion int,
    precio int,
    profesor int,
    foreign key (profesor) references PROFESORES(rut)
);


INSERT INTO PROFESORES VALUES (12345678, 'Juan', 'Pérez', 2000000, '2023-05-10');
INSERT INTO PROFESORES VALUES (87654321, 'María', 'González', 1800000, '2022-09-15');
INSERT INTO PROFESORES VALUES (11223344, 'Pedro', 'Sánchez', 2200000, '2024-01-20');
INSERT INTO PROFESORES VALUES (99887766, 'Luis', 'Martínez', 1900000, '2023-11-05');
INSERT INTO PROFESORES VALUES (55443322, 'Ana', 'López', 2100000, '2022-06-30');
INSERT INTO PROFESORES VALUES (78901234, 'Carolina', 'Rodríguez', 1950000, '2024-03-12');
INSERT INTO PROFESORES VALUES (45678901, 'Carlos', 'Hernández', 2050000, '2023-08-25');
INSERT INTO PROFESORES VALUES (34567890, 'Sofía', 'Díaz', 1980000, '2022-12-18');
INSERT INTO PROFESORES VALUES (21098765, 'Miguel', 'Torres', 2250000, '2024-02-08');
INSERT INTO PROFESORES VALUES (98765432, 'Gabriela', 'Soto', 1850000, '2023-04-03');
INSERT INTO PROFESORES VALUES (65432109, 'Eduardo', 'Chavez', 2300000, '2022-10-28');
INSERT INTO PROFESORES VALUES (33445566, 'Fernanda', 'Alvarez', 1920000, '2024-01-15');
INSERT INTO PROFESORES VALUES (77665544, 'Diego', 'Vargas', 1985000, '2023-07-20');
INSERT INTO PROFESORES VALUES (11222344, 'Patricia', 'Molina', 2040000, '2022-11-11');
INSERT INTO PROFESORES VALUES (88990011, 'Andrea', 'Rojas', 2105000, '2024-04-05');
INSERT INTO PROFESORES VALUES (66778899, 'Javier', 'Gómez', 1975000, '2023-09-30');
INSERT INTO PROFESORES VALUES (99827766, 'Alejandro', 'Peralta', 2150000, '2022-07-16');
INSERT INTO PROFESORES VALUES (22334455, 'Camila', 'Flores', 1910000, '2024-02-28');
INSERT INTO PROFESORES VALUES (55667788, 'Paula', 'Ortega', 2020000, '2023-01-07');
INSERT INTO PROFESORES VALUES (11523344, 'Hernán', 'Silva', 2080000, '2022-08-14');

INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Programación en Python', 150000, 250000,  12345678);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Diseño Gráfico Avanzado', 180000, 280000, 87654321);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Inglés Intermedio', 120000, 200000,  11223344);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Gestión de Proyectos', 200000, 300000, 99887766);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Marketing Digital', 170000, 270000, 55443322);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Contabilidad Básica', 140000, 220000,  78901234);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Desarrollo Web', 180000, 280000,  45678901);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Administración de Empresas', 190000, 290000,  34567890);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Fotografía Digital', 160000, 260000, 21098765);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Programación en Java', 170000, 270000, 98765432);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Redes de Computadoras', 200000, 300000, 65432109);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Marketing de Contenidos', 150000, 250000,  33445566);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Economía Básica', 160000, 260000,  77665544);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Diseño de Interiores', 180000, 280000,  11223344);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Ventas y Negociación', 170000, 270000,  88990011);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Estadística Aplicada', 190000, 290000,  66778899);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Desarrollo de Videojuegos', 200000, 300000,  99887766);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Dibujo Artístico', 160000, 260000,  22334455);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Analítica Web', 150000, 250000,  55667788);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Gestión de Recursos Humanos', 180000, 280000, 11223344);

#3 CURSOS MÁS 
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Introducción a la Inteligencia Artificial', 200000, 320000,  99887766);
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Diseño de Experiencia de Usuario (UX)', 180000, 280000,  22334455);
INSERT INTO CURSOS (nombre, costo_realizacion, precio,  profesor) VALUES ('Gestión Financiera Empresarial', 210000, 330000, 66778899);
 
#3 PROFESORES MÁS
INSERT INTO PROFESORES VALUES (13579246, 'Marcela', 'Gómez', 1950000, '2023-08-10');
INSERT INTO PROFESORES VALUES (24681357, 'Ricardo', 'López', 2100000, '2022-11-25');
INSERT INTO PROFESORES VALUES (36925814, 'Carmen', 'Martínez', 1850000, '2024-04-03');

#CURSO MÁS COSTOSO
SELECT nombre,MAX(precio) FROM CURSOS;

#PROFESOR CON MENOR SALARIO
SELECT CONCAT(CONCAT(nombre," "),apellido) as "nombre completo",MIN(salario) FROM PROFESORES;

#CURSOS MÁS CAROS QUE EL PROMEDIO
select * FROM CURSOS WHERE precio>(SELECT AVG(precio) FROM CURSOS);

#CREAR TABLA CURSOS ECONOMICOS
CREATE TABLE CURSOS_ECONOMICOS AS SELECT * FROM CURSOS WHERE precio<(SELECT AVG(precio) FROM CURSOS);

#AÑADIR COLUMNAS cantidad minima y aportes publicos
ALTER TABLE CURSOS_ECONOMICOS ADD COLUMN Cantidad_minima_estudiantes INT DEFAULT 1;
ALTER TABLE CURSOS_ECONOMICOS ADD COLUMN aportes_publicos INT DEFAULT 100000;

#CAMBIO DE NOMBRE
ALTER TABLE CURSOS_ECONOMICOS CHANGE COLUMN costo_realizacion costo_efectivo INT;
#CAMBIO DE VALORES
UPDATE CURSOS_ECONOMICOS SET costo_efectivo=costo_efectivo-aportes_publicos;

#5 CURSOS MÄS
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Introducción a la Economía', 120000, 200000, 13579246);
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Fundamentos de Finanzas Personales', 100000, 180000, 24681357);
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Marketing para Emprendedores', 150000, 220000, 36925814);
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Negocios Online', 130000, 210000, 13579246);
INSERT INTO CURSOS (nombre, costo_realizacion, precio, profesor) VALUES ('Gestión de Pequeñas Empresas', 140000, 230000, 24681357);

#3 PROFESORES MÁS
INSERT INTO PROFESORES (rut, nombre, apellido, salario, fecha_contratacion) VALUES (12345678, 'María', 'González', 1800000, '2022-09-15');
INSERT INTO PROFESORES (rut, nombre, apellido, salario, fecha_contratacion) VALUES (87654321, 'Juan', 'Pérez', 2000000, '2023-05-10');
INSERT INTO PROFESORES (rut, nombre, apellido, salario, fecha_contratacion) VALUES (98766432, 'Carolina', 'Rodríguez', 1950000, '2024-03-12');