#Una transaccion es un conjunto de operaciones en una base de datos que se ejecutan en bloque como un todo,
#es decir, se ejecuta todo dentro de una transaccion o nada en lo absoluto
#un Ejemplo de transaccion se puede dar en una compra donde se puede apartar el producto para el usuario 
#pero en caso de que la compra se rechace los cambios no se verán realizados en la base de datos

#el beneficio principal de ejecutar en transacciones es que en caso de algún error a lo largo de la transaccion
#los cambios realizados no afectan los datos

#Las transacciones tienen las propiedades ACID
#Atomicidad: Se ejecuta todo o nada. no hay puntos medios
#Consistencia: la base de datos se mantiene consistente antes y después de la transacción
#Aislamiento: Los efectos de una transacción son invisibles para otra transacción
#Durabilidad: Los cambios de una transaccion presisten

#las sentencias indican el principio y el fin de una transaccion, START TRANSACTION indica el incio de la transaccion 
#mientras que COMMIT y ROLLBACK indican el fin de la transaccion, COMMIT indica el fin exitoso de la transacción y
#ROLLBACK indica el fin de la transacción deshaciendo todo los cambios realizados.

#Una transaccion finaliza con un COMMIT o un ROLLBACK que indican el fin de la transaccion

#CREAMOS LA BASE DE DATOS
CREATE DATABASE inv_32;

#CREAMOS EL USUARIO
CREATE USER TestSubject identified by '1234567';
GRANT ALL ON inv_32.* TO TestSubject;


use inv_32;

#CREAMOS LAS TABLAS
CREATE TABLE user_normal(
	user_id int PRIMARY KEY,
	name_user varchar(255),
    surname varchar(255),
    email varchar(255)
);
CREATE TABLE user_special(
	user_id int PRIMARY KEY,
	name_user varchar(255),
    surname varchar(255),
    email varchar(255)
);

#INICIAMOS UNA TRANSACCION PARA AÑADIR LOS EJEMPLOS
START transaction;
INSERT INTO user_normal(user_id, name_user, surname, email) 
VALUES (1, 'John', 'Doe', 'john.doe@example.com');

INSERT INTO user_normal(user_id, name_user, surname, email) 
VALUES (2, 'Jane', 'Smith', 'jane.smith@example.com');

INSERT INTO user_normal(user_id, name_user, surname, email) 
VALUES (3, 'Alexander', 'Brown', 'alexander.brown@example.com');

INSERT INTO user_normal(user_id, name_user, surname, email) 
VALUES (4, 'Emma', 'Jones', 'emma.jones@example.com');

INSERT INTO user_normal(user_id, name_user, surname, email) 
VALUES (5, 'Sam', 'Williams', 'sam.williams@example.com');

#GUARDAMOS LOS CAMBIOS
COMMIT;

SELECT * FROM user_normal;

#INICIAMOS TRANSACCIONES PARA BORRAR
START transaction;
INSERT INTO user_special SELECT * FROM user_normal WHERE user_normal.user_id=5;
DELETE FROM user_normal WHERE user_normal.user_id=5;
COMMIT;

START transaction;
INSERT INTO user_special SELECT * FROM user_normal WHERE user_normal.user_id=7;
DELETE FROM user_normal WHERE user_normal.user_id=6;
COMMIT;

START transaction;
INSERT INTO user_special SELECT * FROM user_normal WHERE user_normal.user_id=7;
DELETE FROM user_normal WHERE user_normal.user_id=7;
ROLLBACK; #ESTA TRANSACCION SERÁ REVERTIDA



