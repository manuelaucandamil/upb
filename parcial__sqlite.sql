
CREATE TABLE clientes (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre TEXT,
corrreo_electronico TEXT,
telefono INTEGER
)
INSERT INTO clientes ("Nombre", "corrreo_electronico", "telefono")
VALUES ("manuela", "manuelaucandamil@hotmail.com", "3218155950")

INSERT INTO clientes ("Nombre", "corrreo_electronico", "telefono")
VALUES ("andres", "andres123@hotmail.com", "3104950555")


CREATE TABLE Productos (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre_del_producto TEXT,
precio REAL,
stock_disponible INTEGER
)

INSERT INTO Productos (Nombre_del_producto, precio, stock_disponible)
VALUES('cuaderno', 1000, 20)
INSERT INTO Productos (Nombre_del_producto, precio, stock_disponible)
VALUES ('colores', 2000, 30)
INSERT INTO Productos (Nombre_del_producto, precio, stock_disponible)
VALUES('lapicero', 1500, 40)
SELECT * FROM Productos

CREATE TABLE Pedidos (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre_de_los_productos_comprados TEXT,
Nombre_del_cliente TEXT,
fecha TEXT,
total_de_la_compra NUMERIC
)


INSERT INTO Pedidos (Nombre_de_los_productos_comprados, Nombre_del_cliente, fecha, total_de_la_compra)
VALUES ('colores' ,'manuela','08/03/25', '2000')

SELECT * FROM clientes
SELECT * FROM Pedidos WHERE Nombre_del_cliente='manuela'
SELECT * FROM Pedidos
