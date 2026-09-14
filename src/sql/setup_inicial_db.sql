
-- Criação da tabela produtos
CREATE TABLE produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

-- Inserção de produtos fictícios para teste inicial
INSERT INTO produtos (nome_produto, valor) VALUES ('Caneta Azul', 2.50);
INSERT INTO produtos (nome_produto, valor) VALUES ('Caderno 100 folhas', 15.90);