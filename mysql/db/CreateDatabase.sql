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