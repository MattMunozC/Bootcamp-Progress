CREATE DATABASE Music_system;

USE Music_system;

CREATE TABLE time_period(
	id_period int auto_increment PRIMARY KEY,
    characteristics text,
    beginning date,
    ending date
);

CREATE TABLE genre(
	id_genre int auto_increment PRIMARY KEY,
    characteristics text,
    origins text
);

CREATE TABLE artist(
	id_artist int auto_increment PRIMARY KEY,
    birthday date,
    deathday date,
    artist_history text,
    genre int,
    FOREIGN KEY (genre) REFERENCES genre(id_genre)
);

CREATE TABLE artistic_style(
	id_style int auto_increment PRIMARY KEY,
    style_name varchar(255)
);

CREATE TABLE technique(
	id_technique int auto_increment PRIMARY KEY,
    technique_name varchar(255)
);

CREATE TABLE technique_style(
	id_style int NOT NULL,
    id_technique int NOT NULL,
    FOREIGN KEY (id_style) REFERENCES artistic_style(id_style),
    FOREIGN KEY (id_technique) REFERENCES technique(id_technique),
    CONSTRAINT PK primary key (id_style,id_technique)
);

CREATE TABLE known_work(
	id_work int auto_increment PRIMARY KEY,
    style int,
    artist int,
    release_date date,
    FOREIGN KEY (style) REFERENCES artistic_style(id_style),
    FOREIGN KEY (artist) REFERENCES artist(id_artist)
);

CREATE TABLE known_work_technique(
	id_work int NOT NULL,
    id_technique int NOT NULL,
    FOREIGN KEY (id_work) REFERENCES known_work(id_work),
    FOREIGN KEY (id_technique) REFERENCES technique(id_technique),
    CONSTRAINT pk PRIMARY KEY (id_work, id_technique)
);
