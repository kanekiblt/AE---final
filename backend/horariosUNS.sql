CREATE DATABASE IF NOT EXISTS asignacion_labs
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE asignacion_labs;

CREATE TABLE Profesor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    disponibilidad JSON  
);


CREATE TABLE Software (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);


CREATE TABLE Laboratorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capacidad INT NOT NULL,
    disponibilidad JSON
);

-- Tabla intermedia ManyToMany: Laboratorio-Software
CREATE TABLE LaboratorioSoftware (
    laboratorio_id INT NOT NULL,
    software_id INT NOT NULL,
    PRIMARY KEY (laboratorio_id, software_id),
    FOREIGN KEY (laboratorio_id) REFERENCES Laboratorio(id) ON DELETE CASCADE,
    FOREIGN KEY (software_id) REFERENCES Software(id) ON DELETE CASCADE
);

CREATE TABLE Curso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    profesor_id INT,
    peso INT NOT NULL DEFAULT 1,
    software_requerido_id INT,
    duracion_hora INT NOT NULL DEFAULT 1,
    total_alumnos INT NOT NULL DEFAULT 1,
    prerequisito_id INT NULL,
    FOREIGN KEY (profesor_id) REFERENCES Profesor(id) ON DELETE SET NULL,
    FOREIGN KEY (software_requerido_id) REFERENCES Software(id) ON DELETE SET NULL,
    FOREIGN KEY (prerequisito_id) REFERENCES Curso(id) ON DELETE SET NULL
);


CREATE TABLE HorarioAsignado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT NOT NULL,
    laboratorio_id INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    hora_inicio TIME NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES Curso(id) ON DELETE CASCADE,
    FOREIGN KEY (laboratorio_id) REFERENCES Laboratorio(id) ON DELETE CASCADE
);