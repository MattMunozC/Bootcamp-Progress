INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado) 
VALUES (16, 'Juan', 'Pérez', 'Santiago', 'juan@example.com', '2024-04-01', 10000);

INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado) 
VALUES (17, 'María', 'López', 'Valparaíso', 'maria@example.com', '2024-04-02', 7500);

INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado) 
VALUES (18, 'Pedro', 'González', 'Concepción', 'pedro@example.com', '2024-04-03', 20000);

INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado) 
VALUES (19, 'Ana', 'Martínez', 'Viña del Mar', 'ana@example.com', '2024-04-04', 15000);

INSERT INTO cliente (id_cliente, name_cliente, surname_cliente, comuna, email, registry_date, total_pagado) 
VALUES (20, 'Luis', 'Rodríguez', 'Antofagasta', 'luis@example.com', '2024-04-05', 5000);

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio) 
VALUES (16, 'Camisa', 'Ropa', 'Fabricante A', 100, 15000);

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio) 
VALUES (17, 'Pantalón', 'Ropa', 'Fabricante B', 80, 25000);

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio) 
VALUES (18, 'Zapatillas', 'Calzado', 'Fabricante C', 120, 35000);

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio) 
VALUES (19, 'Reloj', 'Accesorios', 'Fabricante D', 50, 50000);

INSERT INTO producto (SKU, name_producto, categoria, productor, stock, precio) 
VALUES (20, 'Mochila', 'Accesorios', 'Fabricante E', 70, 40000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (1, 'Juan', 'Pérez', '1990-05-15', 'Electrónica', 800000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (2, 'María', 'López', '1985-08-20', 'Ropa', 750000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (3, 'Pedro', 'González', '1992-02-10', 'Hogar', 850000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (4, 'Ana', 'Martínez', '1988-11-30', 'Deportes', 900000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (5, 'Luis', 'Rodríguez', '1995-04-25', 'Juguetes', 700000);


INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (21456789, 'Juan', 'Pérez', '1990-05-15', 'Electrónica', 800000);


INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (23234567, 'María', 'López', '1985-08-20', 'Ropa', 750000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (19876543, 'Pedro', 'González', '1992-02-10', 'Hogar', 850000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (24567890, 'Ana', 'Martínez', '1988-11-30', 'Deportes', 900000);

INSERT INTO Vendedor (RUN, name_vendendor, surname_vendendor, birthdate, seccion, salario) 
VALUES (21234567, 'Luis', 'Rodríguez', '1995-04-25', 'Juguetes', 700000);

SELECT MIN(salario) FROM vendedor;

SELECT MAX(salario) FROM vendedor;

UPDATE vendedor set salario=salario+(SELECT MIN(salario) FROM vendedor) WHERE salario>0;

DELETE FROM producto WHERE precio=(SELECT MAX(precio) FROM producto);

CREATE TABLE promedio_o_mas as SELECT * FROM cliente WHERE total_pagado>(SELECT AVG(total_pagado) FROM cliente);

UPDATE producto SET precio=100000 WHERE SKU=1;
UPDATE producto SET precio=100000 WHERE SKU=2;
UPDATE producto SET precio=100000 WHERE SKU=3;

update vendedor set name_vendendor="pedro" WHERE RUN=1;
update vendedor set name_vendendor="marisa" WHERE RUN=2;
update vendedor set name_vendendor="jose" WHERE RUN=3;

update cliente set total_pagado=1000000 WHERE id_cliente=1;

SELECT name_vendendor as nombre, surname_vendendor as apellido from vendedor where salario>(SELECT AVG(salario) FROM vendedor);
SELECT * FROM cliente where total_pagado=(SELECT MAX(total_pagado) FROM cliente);