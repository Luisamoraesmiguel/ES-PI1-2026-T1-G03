-- Criação do banco de dados principal do sistema de votação
CREATE DATABASE IF NOT EXISTS tabela_bd;
USE tabela_bd;

-- Tabela de eleitores: armazena os dados cadastrais de cada eleitor
CREATE TABLE eleitores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    cpf VARCHAR(100) NOT NULL UNIQUE,       -- CPF cifrado com Cifra de Hill
    titulo CHAR(12) NOT NULL UNIQUE,
    mesario CHAR(2) NOT NULL,               -- 'S' para mesário, 'N' para eleitor comum
    chave_de_acesso VARCHAR(50) UNIQUE NOT NULL,
    votou CHAR(2) NOT NULL                  -- 'S' se já votou, 'N' se ainda não votou
);

-- Tabela de candidatos: armazena os dados de cada candidato registrado
CREATE TABLE candidatos (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Num_votacao INT NOT NULL UNIQUE,        -- Número digitado na urna pelo eleitor
    Partido VARCHAR(10) NOT NULL
);

-- Tabela de votos: registra cada voto computado com protocolo único
CREATE TABLE votos (
    Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Candidato INT,
    Datahora DATETIME NOT NULL,
    Protocolo_votacao VARCHAR(20) NOT NULL UNIQUE  -- Protocolo cifrado gerado no momento do voto
);

-- Relaciona cada voto ao candidato correspondente
ALTER TABLE votos
ADD FOREIGN KEY (Candidato) REFERENCES candidatos(id);

ALTER TABLE votos
MODIFY Protocolo_votacao VARCHAR(20) NOT NULL;

ALTER TABLE votos
MODIFY Candidato INT NOT NULL;

-- Restringe os valores aceitos nas colunas de controle dos eleitores
ALTER TABLE eleitores
MODIFY mesario CHAR(1) NOT NULL CHECK (mesario IN ('S', 'N'));

ALTER TABLE eleitores
MODIFY votou CHAR(1) NOT NULL CHECK (votou IN ('S', 'N'));

-- Tabela de auditoria: registra ações realizadas no sistema para rastreabilidade
CREATE TABLE auditoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),           -- Nome ou identificador de quem executou a ação
    acao VARCHAR(250),              -- Descrição da ação realizada
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP  -- Data e hora automáticas do registro
);
