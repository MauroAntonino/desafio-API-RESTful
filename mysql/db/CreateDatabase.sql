USE Desafio;

CREATE TABLE User 
( 
    id VARCHAR(100) PRIMARY KEY,  
    email VARCHAR(100) NOT NULL, 
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    image_url VARCHAR(100) NOT NULL,
    UNIQUE (email)
);

CREATE TABLE Movie
( 
    name VARCHAR(100) PRIMARY KEY,  
    rating FLOAT NOT NULL,
    year INT NOT NULL,
    UNIQUE (name)
);

INSERT INTO Movie (name, rating, year)
VALUES ("A Lista de Schindler", 9.0, 1993);
INSERT INTO Movie (name, rating, year)
VALUES ("Um Sonho de Liberdade", 9.3, 1994);
INSERT INTO Movie (name, rating, year)
VALUES ("O Poderoso Chefao", 9.2, 1972);
INSERT INTO Movie (name, rating, year)
VALUES ("Batman: O Cavaleiro das Trevas", 9.0, 2008);
INSERT INTO Movie (name, rating, year)
VALUES ("O Poderoso Chefao: Parte II ", 9.0, 1974);
INSERT INTO Movie (name, rating, year)
VALUES ("12 Homens e Uma Sentenca", 9.0, 1957);
INSERT INTO Movie (name, rating, year)
VALUES ("O Senhor dos Anéis", 9.0, 2003);
INSERT INTO Movie (name, rating, year)
VALUES ("Pulp Fiction", 8.9, 1994);
INSERT INTO Movie (name, rating, year)
VALUES ("O Senhor dos Aneis: A Sociedade do Anel", 8.8, 2001);
INSERT INTO Movie (name, rating, year)
VALUES ("Tres Homens em Conflito", 8.8, 1966);