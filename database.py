import sqlite3

# crear tabala productos
# Esta función se debe llamar una vez al inicio del programa para asegurarse de que la tabla
# existe antes de realizar cualquier operación con productos.
def crear_tabla_productos():
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                codigo TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL
            )
        """)
        conn.commit()
        print("Tabla productos creada o verificada correctamente.")

# Crear tabla para historial de ventas
# Esta función se debe llamar una vez al inicio del programa para asegurarse de que la tabla
# existe antes de realizar cualquier operación con el historial de ventas.
def tabla_historial_ventas():
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY (codigo) REFERENCES productos(codigo)
            )
        """)
        conn.commit()
        print("Tabla historial de ventas creada o verificada correctamente.")

#  Función para agregar un producto
def agregar_producto(codigo, nombre, precio, cantidad):
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (codigo, nombre, precio, cantidad))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False 

# Función para buscar un producto por código
def buscar_producto(codigo):
    import sqlite3
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre, precio, cantidad FROM productos WHERE codigo = ?", (codigo,))
        return cursor.fetchone()


# Función para consultar todos los productos
def consultar_productos():
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

# Función para actualizar un producto
def actualizar_producto(nombre, codigo, precio, cantidad):
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ? WHERE codigo = ?", (nombre, precio, cantidad, codigo))
        conn.commit()
        return cursor.rowcount

# Función para eliminar un producto
def eliminar_producto_data(codigo):
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        conn.commit()
        return cursor.rowcount

# funcion para ver el historial de ventas
def historial_ventas():
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ventas")
        return cursor.fetchall()