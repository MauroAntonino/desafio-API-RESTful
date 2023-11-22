CREATE DATABASE IF NOT EXISTS Desafio;

USE Desafio;

CREATE TABLE IF NOT EXISTS User 
( 
    id VARCHAR(100) PRIMARY KEY,  
    email VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    image_url VARCHAR(100) NOT NULL,
    is_confirmed BOOLEAN NOT NULL,
    UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS Movie
( 
    name VARCHAR(100) PRIMARY KEY,  
    rating FLOAT NOT NULL,
    year INT NOT NULL,
    UNIQUE (name)
);

REPLACE INTO Movie (name, rating, year)
VALUES ("A Lista de Schindler", 9.0, 1993);
REPLACE INTO Movie (name, rating, year)
VALUES ("Um Sonho de Liberdade", 9.3, 1994);
REPLACE INTO Movie (name, rating, year)
VALUES ("O Poderoso Chefao", 9.2, 1972);
REPLACE INTO Movie (name, rating, year)
VALUES ("Batman: O Cavaleiro das Trevas", 9.0, 2008);
REPLACE INTO Movie (name, rating, year)
VALUES ("O Poderoso Chefao: Parte II ", 9.0, 1974);
REPLACE INTO Movie (name, rating, year)
VALUES ("12 Homens e Uma Sentenca", 9.0, 1957);
REPLACE INTO Movie (name, rating, year)
VALUES ("O Senhor dos Aneis", 9.0, 2003);
REPLACE INTO Movie (name, rating, year)
VALUES ("Pulp Fiction", 8.9, 1994);
REPLACE INTO Movie (name, rating, year)
VALUES ("O Senhor dos Aneis: A Sociedade do Anel", 8.8, 2001);
REPLACE INTO Movie (name, rating, year)
VALUES ("Tres Homens em Conflito", 8.8, 1966);

CREATE TABLE IF NOT EXISTS BestMovie
( 
    name VARCHAR(100) PRIMARY KEY,  
    rating FLOAT NOT NULL,
    year INT NOT NULL,
    UNIQUE (name)
);

REPLACE INTO BestMovie (name, rating, year)
VALUES ("O Rei Leão", 9.8, 2011);
REPLACE INTO BestMovie (name, rating, year)
VALUES ("Vingadores: Ultimato", 9.7, 2019);
REPLACE INTO BestMovie (name, rating, year)
VALUES ("O Resgate do Soldado Ryan", 9.9, 1998);
REPLACE INTO BestMovie (name, rating, year)
VALUES ("Gladiador", 9.8, 2000);
REPLACE INTO BestMovie (name, rating, year)
VALUES ("Toy Story 3", 9.6, 2010);
REPLACE INTO BestMovie (name, rating, year)
VALUES ("Divertida Mente", 9.9, 2015);

