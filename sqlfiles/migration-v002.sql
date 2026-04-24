USE ynov_ci;

CREATE TABLE IF NOT EXISTS utilisateur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(25) NOT NULL,
    prenom VARCHAR(25) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO utilisateur (nom, prenom, email) VALUES
('Yaroslav', 'Andrushchak', 'yaroslav@example.com'),
('Alice', 'Example', 'alice@example.com'),
('Test', 'Test', 'test@test.com'),
('Bob', 'Test2', 'test2@test.com');