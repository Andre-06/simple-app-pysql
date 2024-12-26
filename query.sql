DROP TABLE clientes;

CREATE TABLE IF NOT EXISTS clientes (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL
);

INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('João', 'Silva', 'joao.silva@example.com', '12345678901');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Maria', 'Oliveira', 'maria.oliveira@example.com', '23456789012');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Pedro', 'Santos', 'pedro.santos@example.com', '34567890123');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Ana', 'Souza', 'ana.souza@example.com', '45678901234');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Lucas', 'Pereira', 'lucas.pereira@example.com', '56789012345');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Fernanda', 'Lima', 'fernanda.lima@example.com', '67890123456');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Rafael', 'Martins', 'rafael.martins@example.com', '78901234567');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Juliana', 'Costa', 'juliana.costa@example.com', '89012345678');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Gustavo', 'Ramos', 'gustavo.ramos@example.com', '90123456789');
INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES ('Carla', 'Fernandes', 'carla.fernandes@example.com', '01234567890');
