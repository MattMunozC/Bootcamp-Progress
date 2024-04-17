CREATE DATABASE TeloVendo5;
USE TeloVendo5;
CREATE USER "ADMIN" identified by "123456";
GRANT ALL privileges ON * TO "ADMIN";
CREATE TABLE cliente(
	id_cliente int primary key auto_increment,
    saldo int
);
CREATE TABLE direccion(
	id_direccion int primary key auto_increment,
    id_cliente int,
    adress text,
    localidad varchar(255),
    region varchar(255),
    zip_code int,
    latitud int,
    longitud int,
    nombre varchar(255),
    foreign key (id_cliente) references cliente(id_cliente)
);

CREATE TABLE fabrica(
	id_fabrica int primary key auto_increment,
    nombre varchar(255),
    telefono int,
    total_articulos int default 0
);
CREATE TABLE articulo(
	id_articulo int primary key auto_increment,
    nombre varchar(255),
    stock int,
    descripcion text,
    id_fabrica int,
    foreign key (id_fabrica) references fabrica(id_fabrica)
);

DELIMITER //

CREATE TRIGGER nuevo_producto AFTER INSERT ON articulo 
FOR EACH ROW
BEGIN 
	UPDATE fabrica 
		SET total_articulos=(SELECT count(*) FROM articulo WHERE id_fabrica=NEW.id_fabrica)
		WHERE fabrica.id_fabrica=NEW.id_fabrica;
END;
//
DELIMITER ;


CREATE TABLE pedido(
	id_pedido int primary key auto_increment
);

CREATE TABLE pedido_cabecera(
	id_pedido int primary key,
    id_cliente int,
    id_direccion int,
    fecha_pedido date,
    foreign key (id_pedido) references pedido(id_pedido),
    foreign key (id_cliente) references articulo(id_articulo),
    foreign key (id_direccion) references direccion(id_direccion)
);
CREATE TABLE pedido_cuerpo(
    id_pedido int,
    id_articulo int,
    cantidad int,
	primary key (id_pedido,id_articulo),
    foreign key (id_pedido) references pedido(id_pedido),
    foreign key (id_articulo) references articulo(id_articulo)
);



INSERT INTO FABRICA VALUES(1,"TeLoVendo",1234567,0);

SELECT * FROM FABRICA;

INSERT INTO ARTICULO VALUES(1,"Gameboy",10,"Consola de 1987",1);
INSERT INTO ARTICULO VALUES(2,"Nintendo Switch",10,"Consola de 2017",1);