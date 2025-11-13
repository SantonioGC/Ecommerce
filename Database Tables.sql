CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    fecha_nacimiento DATE,
    activo BOOLEAN DEFAULT TRUE,
    tipo_usuario VARCHAR(20) DEFAULT 'cliente',
    creado TIMESTAMP DEFAULT NOW(),
);

CREATE TABLE categorias
(
id SERIAL PRIMARY KEY,
nombre VARCHAR(100) UNIQUE NOT NULL,
descripcion TEXT
);

CREATE TABLE productos
(
id SERIAL PRIMARY KEY,
nombre VARCHAR(255) NOT NULL,
descripcion TEXT,
precio DECIMAL(10,2) NOT NULL,
stock INT DEFAULT 0,
categoria_id INT REFERENCES categorias(id),
imagen_url VARCHAR(500),
activo BOOLEAN DEFAULT TRUE,
creado TIMESTAMP DEFAULT NOW()
);


CREATE TABLE direcciones
(
id SERIAL PRIMARY KEY,
usuario_id INT REFERENCES usuarios(id),
direccion TEXT NOT NULL,
ciudad VARCHAR(100),
codigo_postal VARCHAR(20),
principal BOOLEAN DEFAULT FALSE
);

CREATE TABLE pedidos
(
id SERIAL PRIMARY KEY,
usuario_id INT REFERENCES usuarios(id),
direccion_id INT REFERENCES direcciones(id),
estado VARCHAR(50) DEFAULT 'pendiente',
total DECIMAL(10,2) NOT NULL,
fecha_pedido TIMESTAMP DEFAULT NOW(),
fecha_actualizado TIMESTAMP DEFAULT NOW()
);

CREATE TABLE pedido_items
(
id SERIAL PRIMARY KEY,
pedido_id INT REFERENCES pedidos(id),
producto_id INT REFERENCES productos(id),
cantidad INT NOT NULL,
precio_unitario DECIMAL(10,2) NOT NULL
);

CREATE TABLE carrito
(
id SERIAL PRIMARY KEY,
usuario_id INTEGER REFERENCES usuarios(id),
producto_id INTEGER REFERENCES productos(id),
cantidad INTEGER DEFAULT 1,
agregado_en TIMESTAMP DEFAULT NOW()
);

CREATE TABLE reseñas 
(
id SERIAL PRIMARY KEY,
usuario_id INTEGER REFERENCES usuarios(id),
producto_id INTEGER REFERENCES productos(id),
puntuacion INTEGER CHECK (puntuacion >= 1 AND puntuacion <= 5),
comentario TEXT,
fecha TIMESTAMP DEFAULT NOW()
);


CREATE TABLE pagos 
(
id SERIAL PRIMARY KEY,
pedido_id INTEGER REFERENCES pedidos(id),
monto DECIMAL(10,2) NOT NULL,
metodo_pago VARCHAR(50),
estado VARCHAR(50) DEFAULT 'pendiente',
transaccion_id VARCHAR(255),
fecha_pago TIMESTAMP DEFAULT NOW()
);


CREATE TABLE inventario 
(
id SERIAL PRIMARY KEY,
producto_id INTEGER REFERENCES productos(id),
cantidad INTEGER NOT NULL,
movimiento VARCHAR(50),
fecha_movimiento TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sesiones 
(
id SERIAL PRIMARY KEY,
usuario_id INTEGER REFERENCES usuarios(id),
token VARCHAR(500) UNIQUE NOT NULL,
expiracion TIMESTAMP NOT NULL,
activa BOOLEAN DEFAULT TRUE
);
