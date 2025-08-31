import sqlite3

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}) - Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._crear_tabla()

    def _crear_tabla(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT UNIQUE NOT NULL,
                                cantidad INTEGER NOT NULL,
                                precio REAL NOT NULL
                              )''')
            conn.commit()

    def agregar_producto(self, nombre, cantidad, precio):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                           (nombre, cantidad, precio))
            conn.commit()

    def eliminar_producto(self, id_producto):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conn.commit()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if cantidad is not None:
                cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id_producto))
            if precio is not None:
                cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id_producto))
            conn.commit()

    def buscar_producto(self, nombre):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
            return cursor.fetchall()

    def mostrar_productos(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos")
            return cursor.fetchall()
