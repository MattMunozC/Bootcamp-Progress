use telovendo;

CREATE TABLE USUARIO(
	id int primary key auto_increment,
    username varchar(255),
    rut int,
    name_user varchar(255),
    surname_user varchar(255)
);

CREATE TABLE CUENTA(
	id int primary key auto_increment,
    id_user int,
    TLV_coins int,
    foreign key (id_user) references usuario(id)
);
CREATE TABLE transactiones(
	id int primary key auto_increment,
    id_source int,
    id_destination int,
	transact_date datetime default NOW(),
    foreign key (id_source) references usuario(id),
    foreign key (id_destination) references usuario(id)
);
INSERT INTO USUARIO (username,rut,name_user,surname_user) values
	('usuario A', 12344525,"juan","perez"),
    ('usuario B', 9428231,"maria","jaque"),
    ('usuario C',51294123,"roberto","reyero"),
    ('usuario D',13999234,"pedro","pareiro");
    
INSERT INTO CUENTA (id_user,TLV_coins) values
	(1,200),
    (2,200),
    (3,500),
    (4,200);
    

START TRANSACTION;

#TRANSFERENCIA ENTER A Y B
UPDATE CUENTA SET TLV_coins=TLC_coins+200 WHERE id_user=2;
UPDATE CUENTA SET TLV_coins=TLC_coins-200 WHERE id_user=1;
INSERT INTO transacciones values (1,2);
#A queda con 0
#B queda con 400
#C queda con 500
#D queda con 200
ROLLBACK;

START TRANSACTION;

UPDATE CUENTA SET TLV_coins=TLC_coins-150 WHERE id_user=2;
UPDATE CUENTA SET TLV_coins=TLC_coins+150 WHERE id_user=3;
INSERT INTO transacciones values (2,3);

#A queda con 200
#B queda con 50
#C queda con 650
#D queda con 200

ROLLBACK;

START TRANSACTION;

UPDATE CUENTA SET TLV_coins=TLC_coins-500 WHERE id_user=3;
UPDATE CUENTA SET TLV_coins=TLC_coins+500 WHERE id_user=4;
INSERT INTO transacciones values (3,4);

#A queda con 200
#B queda con 200
#C queda con 0
#D queda con 700
COMMIT;

START TRANSACTION;

UPDATE CUENTA SET TLV_coins=TLC_coins-200 WHERE id_user=4;
UPDATE CUENTA SET TLV_coins=TLC_coins+200 WHERE id_user=1;
INSERT INTO transacciones values (4,1);

#A queda con 400
#B queda con 200
#C queda con 0
#D queda con 500