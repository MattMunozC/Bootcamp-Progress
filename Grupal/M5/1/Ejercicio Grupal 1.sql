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
    registry_date date
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
    