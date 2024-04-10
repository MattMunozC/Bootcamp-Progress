CREATE DATABASE telovendo;
USE telovendo;

CREATE USER admintienda IDENTIFIED BY '123456';

GRANT ALL privileges ON telovendo.* TO admintienda;

CREATE TABLE cliente(
	id_cliente int PRIMARY KEY,
    name_cliente varchar(255),
    surname_cliente varchar(255),
    comuna varchar(255),
    email varchar(255),
    registry_date date,
    
);
CREATE TABLE producto(
	SKU int primary key,
    name_producto varchar(255),
    categoria varchar(255),
    productor varchar(255),
    stock int
);
CREATE TABLE Vendedor(
	RUN int primary key,
    name_vendendor varchar(255),
    surname_vendendor varchar(255),
    birthdate date,
    seccion varchar(255)
);

ALTER TABLE producto ADD COLUMN Precio int;
ALTER TABLE vendedor ADD COLUMN Salario int;
ALTER TABLE cliente ADD COLUMN total_pagado int; 
INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion) VALUES
(12345678, 'John', 'Doe', '1990-05-15', 'Electronics'),
(23456789, 'Jane', 'Smith', '1985-12-20', 'Clothing'),
(34567890, 'Michael', 'Johnson', '1988-08-10', 'Home Appliances'),
(45678901, 'Emily', 'Brown', '1992-03-25', 'Furniture'),
(56789012, 'David', 'Martinez', '1987-07-07', 'Electronics'),
(67890123, 'Jessica', 'Garcia', '1991-11-30', 'Clothing'),
(78901234, 'Daniel', 'Rodriguez', '1984-09-18', 'Home Appliances'),
(89012345, 'Sophia', 'Lopez', '1995-02-05', 'Furniture'),
(90123456, 'William', 'Lee', '1993-06-12', 'Electronics'),
(11223344, 'Olivia', 'Wang', '1994-10-08', 'Clothing'),
(22334455, 'James', 'Kim', '1986-04-17', 'Home Appliances'),
(33445566, 'Emma', 'Nguyen', '1996-07-22', 'Furniture'),
(44556677, 'Alexander', 'Chen', '1989-01-29', 'Electronics'),
(55667788, 'Ava', 'Gonzalez', '1990-12-03', 'Clothing'),
(66778899, 'Benjamin', 'Hernandez', '1983-08-14', 'Home Appliances');

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio)
VALUES
(1, 'Camisa de manga corta', 'Ropa', 'Marca A', 100, 2999),
(2, 'Pantalones vaqueros', 'Ropa', 'Marca B', 75, 4999),
(3, 'Zapatos deportivos', 'Calzado', 'Marca C', 50, 6999),
(4, 'Gorra de béisbol', 'Accesorios', 'Marca D', 200, 999),
(5, 'Chaqueta de cuero', 'Ropa', 'Marca E', 30, 14999),
(6, 'Reloj de pulsera', 'Accesorios', 'Marca F', 150, 9999),
(7, 'Camiseta sin mangas', 'Ropa', 'Marca G', 80, 1999),
(8, 'Botas de senderismo', 'Calzado', 'Marca H', 40, 7999),
(9, 'Bufanda de lana', 'Accesorios', 'Marca I', 120, 3999),
(10, 'Vestido de fiesta', 'Ropa', 'Marca J', 25, 19999),
(11, 'Gafas de sol', 'Accesorios', 'Marca K', 100, 5999),
(12, 'Shorts deportivos', 'Ropa', 'Marca L', 60, 2999),
(13, 'Zapatillas de casa', 'Calzado', 'Marca M', 90, 2499),
(14, 'Sombrero de paja', 'Accesorios', 'Marca N', 110, 1499),
(15, 'Traje de baño', 'Ropa', 'Marca O', 35, 3999);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario)
VALUES
(1, 'Juan', 'González', '1990-05-15', 'Electrónica', 2500000),
(2, 'María', 'López', '1985-10-20', 'Ropa', 2800000),
(3, 'Carlos', 'Martínez', '1988-03-12', 'Deportes', 3000000),
(4, 'Laura', 'Pérez', '1993-07-28', 'Hogar', 2600000),
(5, 'Pedro', 'Rodríguez', '1992-01-05', 'Juguetes', 2700000),
(6, 'Ana', 'García', '1987-09-18', 'Electrodomésticos', 2900000),
(7, 'Luis', 'Fernández', '1991-11-30', 'Tecnología', 3100000),
(8, 'Sofía', 'Díaz', '1989-04-22', 'Hogar', 2700000),
(9, 'Daniel', 'Sánchez', '1986-08-14', 'Juguetes', 2800000),
(10, 'Elena', 'Ramírez', '1995-02-09', 'Deportes', 2900000);

INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado)
VALUES
(1, 'Juan', 'González', 'Santiago', 'juan@example.com', '2023-05-15', 50000),
(2, 'María', 'López', 'Viña del Mar', 'maria@example.com', '2023-06-20', 75000),
(3, 'Carlos', 'Martínez', 'Concepción', 'carlos@example.com', '2023-07-12', 30000),
(4, 'Laura', 'Pérez', 'Valparaíso', 'laura@example.com', '2023-08-28', 90000),
(5, 'Pedro', 'Rodríguez', 'La Serena', 'pedro@example.com', '2023-09-05', 40000),
(6, 'Ana', 'García', 'Antofagasta', 'ana@example.com', '2023-10-18', 60000),
(7, 'Luis', 'Fernández', 'Temuco', 'luis@example.com', '2023-11-30', 80000),
(8, 'Sofía', 'Díaz', 'Rancagua', 'sofia@example.com', '2023-12-22', 55000),
(9, 'Daniel', 'Sánchez', 'Arica', 'daniel@example.com', '2024-01-14', 70000),
(10, 'Elena', 'Ramírez', 'Iquique', 'elena@example.com', '2024-02-09', 35000),
(11, 'Andrés', 'Gómez', 'Puerto Montt', 'andres@example.com', '2024-03-22', 42000),
(12, 'Valentina', 'Hernández', 'Chillán', 'valentina@example.com', '2024-04-05', 48000),
(13, 'Diego', 'Muñoz', 'Quilpué', 'diego@example.com', '2024-05-18', 65000),
(14, 'Camila', 'Silva', 'Talca', 'camila@example.com', '2024-06-30', 53000),
(15, 'Matías', 'Torres', 'Los Ángeles', 'matias@example.com', '2024-07-09', 72000);

SELECT * FROM VENDEDOR WHERE salario>(SELECT AVG(salario) FROM vendedor);

SELECT * FROM producto WHERE precio>(SELECT AVG(precio) FROM producto);

SELECT * from cliente WHERE total_pagado > (SELECT AVG(total_pagado) FROM cliente);

SELECT * FROM VENDEDOR WHERE salario<(SELECT AVG(salario) FROM vendedor);

SELECT * FROM producto WHERE precio<(SELECT AVG(precio) FROM producto);


SELECT name_vendedor,surname_vendedor FROM VENDEDOR WHERE salario>(SELECT AVG(salario) FROM vendedor);

SELECT MAX(precio), MIN(precio) FROM producto;

SELECT SUM(precio) FROM producto;

SELECT comuna, MAX(cantidad) FROM (SELECT comuna,count(*) as cantidad FROM cliente GROUP BY comuna) as comuna_contar;

SELECT * FROM PRODUCTO WHERE STOCK>5;

#Auto_increment hace usa para que incremente automaticamente en 1 cada vez que se ingrese una nueva fila
SELECT * FROM vendedor 
    