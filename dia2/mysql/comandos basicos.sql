--SENTENCIAS DDL
-- CREATE TABLE
use db_g6;
CREATE TABLE alumno (
    id INT not null PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(255),
    email VARCHAR(100)
);

-- ALTER TABLE
ALTER TABLE alumno
ADD COLUMN nota INT DEFAULT 0;

-- DROP TABLE
DROP TABLE empresa;

create table empresa (
    id INT not null PRIMARY KEY AUTO_INCREMENT,
    ruc VARCHAR(11) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    direccion VARCHAR(255)
);

--SENTENCIAS DML
-- INSERT
use db_g6;
INSERT INTO alumno (nro_documento, nombre, email) VALUES
('12345678', 'Juan Perez', 'juan.perez@example.com');

INSERT INTO alumno (nro_documento, nombre, email) VALUES
('12345678', 'Juan Perez', 'juan.perez@example.com'),
('87654321', 'Maria Gomez', 'maria.gomez@example.com'),
('11223344', 'Carlos Ruiz', 'carlos.ruiz@example.com'),
('44332211', 'Ana Torres', 'ana.torres@example.com'),
('55667788', 'Luis Fernandez', 'luis.fernandez@example.com'),
('88776655', 'Sofia Martinez', 'sofia.martinez@example.com'), 
('99887766', 'Diego Lopez', 'diego.lopez@example.com'),
('66778899', 'Elena Sanchez', 'elena.sanchez@example.com'),
('33445566', 'Jorge Ramirez', 'jorge.ramirez@example.com'),
('22113344', 'Laura Diaz', 'laura.diaz@example.com');

--ACTUALIZAR REGISTROS

UPDATE alumno SET
email =  CONCAT(LOWER(REPLACE(nombre," ",".")),'@gmail.com') 

--select
select nombre, email from alumno where id > 5;
select * from alumno ORDER BY  id desc;

delete from alumno where id = 10;