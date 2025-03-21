import sqlite3

conn = sqlite3.connect('Inventario.db')
cursor = conn.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS productos(
#                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     codigo TEXT UNIQUE,
#   	                nombre TEXT,
#   	                cantidad REAL,
#   	                precio REAL
#                      )""")

# datos_producto = [("P001","vodka grey goose", "150", "260000"),
#     ("P002","ron zacapa xo", "50", "895000"),
#     ("P003","tequila herradura extra añejo", "20", "1500900"),
#     ("P004","whisky don perignon", "250", "155500"),
#      ("P005","absenta feur de lis", "250", "146900"),
#      ("P006","ginebra gin mare", "100", "329000"),
#      ("P007","cerveza chimay blue", "500", "27000"),
#      ("P008","coctel blue screen", "70", "50000"),
#      ("P009","coctel 404 error", "75", "47000"),
#      ("P010","coctel ia uprising", "50", "60000"),
#      ("P011","aguardiente jubilo tradicional", "80", "292500"),
#      ("P012","vino don melchor sauvilgon", "50", "750000"),
#      ("P013","agua fine", "500", "35000"),
#      ("P014","aperol", "100", "105000"),
#      ("P015","jarabe lava curacao", "70", "150000"),
#      ("P016","tonica fever tree package", "90", "41300")
#  ]
# cursor.executemany("INSERT INTO productos  VALUES (NULL,?, ?, ?, ?)", datos_producto)


def agregar_producto(codigo, nombre, cantidad, precio):
    try:
        cursor.execute('INSERT INTO productos (codigo, nombre, cantidad, precio) VALUES (?,?, ?, ?)', (codigo,nombre, cantidad, precio))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al agregar producto: {e}")

def mostrar_inventario():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    for producto in productos:
        print(f"Codigo: {producto[1]}, Nombre: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}")

def actualizar_producto(nombre, cantidad, precio):
    if existe_producto(nombre):
        try:
            cursor.execute('UPDATE productos SET cantidad = ?, precio = ? WHERE nombre = ?', (cantidad, precio, nombre))
            conn.commit()
            print(f"Producto '{nombre}' actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar producto: {e}")
    else:
        print(f"Producto '{nombre}' no encontrado.")

def buscar_producto(nombre):
    cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
    producto = cursor.fetchone()
    if producto:
        print(f"Codigo: {producto[1]}, Nombre: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}")
    else:
        print("Producto no encontrado.")

def eliminar_producto(nombre):
    cursor.execute('DELETE FROM productos WHERE nombre = ?', (nombre,))
    conn.commit()

def existe_producto(nombre):
    cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
    producto = cursor.fetchone()
    return producto is not None