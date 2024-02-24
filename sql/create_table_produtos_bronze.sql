CREATE TABLE produtos_bronze (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preço FLOAT NOT NULL,
    categoria VARCHAR(255) NOT NULL
);
