CREATE DATABASE IF NOT EXISTS cine_db;
USE cine_db;

# Create table usuarios
CREATE TABLE IF NOT EXISTS usuarios(
	usuario_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    a_paterno VARCHAR(30) NOT NULL,
    a_materno VARCHAR(30) NOT NULL,
	correo VARCHAR(30) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    is_admin BOOL NOT NULL
) ENGINE = InnoDB;

# Create table horario
CREATE TABLE IF NOT EXISTS fecha(
	fecha_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL
) ENGINE = InnoDB;

# Create table clasificacion
CREATE TABLE IF NOT EXISTS clasificacion(
	clasificacion_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    clasificacion VARCHAR(5) NOT NULL,
    descr VARCHAR(200) NOT NULL
) ENGINE = InnoDB;

# Create table idioma
CREATE TABLE IF NOT EXISTS idioma(
	idioma_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descr VARCHAR(5) NOT NULL
) ENGINE = InnoDB;

# Create table administrador
CREATE TABLE IF NOT EXISTS administrador(
	administrador_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    a_paterno VARCHAR(30) NOT NULL,
    a_materno VARCHAR(30) NOT NULL,
    puesto VARCHAR(20) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    telefono VARCHAR(13) NOT NULL
) ENGINE = InnoDB;

# Create table asientos
CREATE TABLE IF NOT EXISTS asiento(
	asiento_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fila INT NOT NULL,
    columna INT NOT NULL
) ENGINE = InnoDB;

# Create table asientos
CREATE TABLE IF NOT EXISTS sala(
	sala_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    asiento_id INT,
    
    CONSTRAINT fkasiento_id FOREIGN KEY(asiento_id)
		REFERENCES asiento(asiento_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;

# Create table pelicula
CREATE TABLE IF NOT EXISTS pelicula(
	pelicula_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    clasificacion_id INT,
    titulo VARCHAR(30) NOT NULL,
    fecha DATE NOT NULL,
    sinopsis VARCHAR(200) NOT NULL,
    
    CONSTRAINT fkclasificacion_id FOREIGN KEY(clasificacion_id)
		REFERENCES clasificacion(clasificacion_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;

# Create table proyeccion
CREATE TABLE IF NOT EXISTS proyeccion(
	proyeccion_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pelicula_id INT,
    idioma_id INT,
    sala_id INT,
    fecha_id INT,
    hora VARCHAR(6) NOT NULL,
    
    CONSTRAINT fkpelicula_id FOREIGN KEY(pelicula_id)
		REFERENCES pelicula(pelicula_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
	CONSTRAINT fkidioma_id FOREIGN KEY(idioma_id)
		REFERENCES idioma(idioma_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
        
	CONSTRAINT fksala_id FOREIGN KEY(sala_id)
		REFERENCES sala(sala_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

	CONSTRAINT fkfecha_id FOREIGN KEY(fecha_id)
		REFERENCES fecha(fecha_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;

# Create table ticket
CREATE TABLE IF NOT EXISTS ticket(
	ticket_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    proyeccion_id INT,
    asiento VARCHAR(10),
    costo FLOAT NOT NULL,	
    
	CONSTRAINT fktproyeccion_id FOREIGN KEY(proyeccion_id)
		REFERENCES proyeccion(proyeccion_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;

# Create table compras
CREATE TABLE IF NOT EXISTS compras(
	compra_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    ticket_id INT,
    costo_total FLOAT NOT NULL,
    
	CONSTRAINT fkusuario_id FOREIGN KEY(usuario_id)
		REFERENCES usuarios(usuario_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	
    CONSTRAINT fkticket_id FOREIGN KEY(ticket_id)
		REFERENCES ticket(ticket_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;