import tkinter as tk
import sqlite3
from datetime import datetime
# importaciones locales
from database import buscar_producto
from funciones import placeholder, posicionar, estilo_botones_general, tamaño_ventana, ruta_recurso

# stock temporal con el que trabajara la caja mientras se confirma la compra
# clave: codigo, valor: cantidad reservada
stock_temporal = {}

# ventana principal
def cajero():
    ventana_cajero = tk.Toplevel()
    ventana_cajero.title("Ha ingresado como cajero")
    ventana_cajero.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_cajero)

    # funcion para simular divisiones de campos en la interfaz de caja
    def decorar_contenedor(contenedor):
        contenedor.config(bg="#f0f8ff", highlightbackground="black", highlightthickness=1)

    # Variables globales dentro de la función
    productos_vendidos = []
    total_compra = tk.StringVar(value="$ 0")
    numero_productos = tk.DoubleVar(value=0.0)

# contenedor rellenar campos del producto (codigo,cantidad)
    contenedor_rellenar_campos = tk.Frame(ventana_cajero)
    posicionar(contenedor_rellenar_campos, x=0, y=0, width=0.7, height=0.4)
    decorar_contenedor(contenedor_rellenar_campos)
    # etiqueta codigo
    etiqueta_codigo = tk.Label(contenedor_rellenar_campos,text="CODIGO",bg="#f0f8ff",font=("Arial", 14, "bold"),anchor="w")
    posicionar(etiqueta_codigo, x=0.06, y=0.1, anchor=tk.CENTER)
    # entry codigo
    entrada_codigo = tk.Entry(contenedor_rellenar_campos, font=("Arial", 20), bg="#ffffff", width=55)
    posicionar(entrada_codigo,x=0.483, y=0.22, anchor=tk.CENTER)
    placeholder(entrada_codigo, "Codigo del producto")
    entrada_codigo.focus()
    # etiqueta cantidad
    etiqueta_cantidad = tk.Label(contenedor_rellenar_campos,text="CANTIDAD",bg="#f0f8ff",font=("Arial", 14, "bold"),anchor="w")
    posicionar(etiqueta_cantidad, x=0.07, y=0.42, anchor=tk.CENTER)
    # entry cantidad
    entrada_cantidad = tk.Entry(contenedor_rellenar_campos, font=("Arial", 20), bg="#ffffff", width=55)
    placeholder(entrada_cantidad, "Cantidad")
    posicionar(entrada_cantidad, x= 0.483, y=0.54, anchor=tk.CENTER)

#contenedor para verificar el producto
    contenedor_verificar_producto = tk.Frame(ventana_cajero,bg="#f0f8ff",highlightbackground="black",highlightthickness=1)
    posicionar(contenedor_verificar_producto, x=0.7, y=0, width=0.3, height=1.0, anchor="nw")
    # se define una variable para usarla dentro de la etiqueta de verificacion
    producto_var = tk.StringVar()
    # titulo
    etiqueta_titulo = tk.Label(contenedor_verificar_producto,font=("Arial", 14, "bold"),text="Verificación del producto:",bg="#f0f8ff",fg="#1477B5")
    posicionar(etiqueta_titulo, x=0.5, y=0.08, anchor=tk.CENTER)
    #etiqueta que muestra los datos verificados
    etiqueta_producto = tk.Label(contenedor_verificar_producto,textvariable=producto_var,font=("Arial", 12),bg="#ffffff",justify="left",anchor="nw",width=38,  height=10,  highlightbackground="black",highlightthickness=1)
    posicionar(etiqueta_producto, x=0.5, y=0.3, anchor=tk.CENTER)

# contenedor para la lista de compras del cliente
    contenedor_lista_compras = tk.Frame(ventana_cajero)
    posicionar(contenedor_lista_compras, x=0, y=0.3, width=0.7, height=0.5, anchor="nw")
    decorar_contenedor(contenedor_lista_compras)
    # list box para mostrar los productos de la lista de compras
    lista_compras = tk.Listbox(contenedor_lista_compras, font=("Arial", 12),highlightbackground="black",highlightthickness=1 )
    lista_compras.pack(expand=True, fill="both", padx=10, pady=10)

# contenedor para el total de la compra
    contenedor_total_venta = tk.Frame(ventana_cajero)
    posicionar(contenedor_total_venta, x=0, y=0.8, width=1, height=0.2, anchor="nw")
    decorar_contenedor(contenedor_total_venta)
    # etiqueta texto "total"
    label_total = tk.Label(contenedor_total_venta, text="Total: ", font=("Arial", 30, "bold"), bg="#f0f8ff")
    posicionar(label_total,x=0.1,y=0.5, anchor=tk.CENTER)
    # etiqueta que muestra la suma total
    label_numero_total = tk.Label(contenedor_total_venta, textvariable=total_compra, font=("Arial", 20, "bold"), bg="#ffffff",highlightbackground="black",highlightthickness=1 )
    posicionar(label_numero_total, x=0.85 ,y=0.5,anchor=tk.CENTER)

    # funcion que verifica que el producto registrado este existente y en stock
    def verificar_producto(event=None):
        codigo = entrada_codigo.get()
        producto = buscar_producto(codigo)
        if producto:
            codigo, nombre, precio, stock_db = producto
            reservado = stock_temporal.get(codigo, 0)
            stock_disponible = stock_db - reservado
            producto_var.set(f"Codigo: {codigo}\nProducto: {nombre}\nPrecio: ${precio:.2f}\nStock: {stock_disponible}")
        else:
            producto_var.set("Producto no encontrado")

    # funcion que registra el producto temporalmente, lo muestra en la lista de compras, y suma el total
    def registrar_producto(event=None):
        codigo = entrada_codigo.get()
        cantidad = entrada_cantidad.get()

        if not cantidad.isdigit():
            producto_var.set("Cantidad inválida")
            return 

        producto = buscar_producto(codigo)
        if producto:
            codigo, nombre, precio, stock_db = producto
            cantidad = int(cantidad)

            reservado = stock_temporal.get(codigo, 0)
            stock_disponible = stock_db - reservado

            if cantidad <= stock_disponible:
                subtotal = cantidad * precio
                productos_vendidos.append((codigo, cantidad, subtotal))
                lista_compras.insert(tk.END, f"{nombre} x{cantidad} = ${subtotal:.2f}")
                stock_temporal[codigo] = reservado + cantidad 
                numero_productos.set(numero_productos.get() + 1)
                nuevo_total = sum(sub for _, _, sub in productos_vendidos)
                total_compra.set("$ {:,}".format(int(nuevo_total)).replace(",", "."))

                producto_var.set(f"Producto: {nombre}\nPrecio: ${precio:.2f}\nStock restante: {stock_disponible - cantidad}")
                entrada_codigo.delete(0, tk.END)
                entrada_cantidad.delete(0, tk.END)
            else:
                producto_var.set("Stock insuficiente")
        else:
            producto_var.set("Producto no encontrado")

    # funcion que guarda la compra total en la base de datos
    def guardar_venta_db():
        if not productos_vendidos:
            producto_var.set("No hay productos para guardar.")
            return

        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with sqlite3.connect("productos.db") as conn:
            cursor = conn.cursor()
            for codigo, cantidad, _ in productos_vendidos:
                producto = buscar_producto(codigo)
                if producto:
                    _, nombre, _, _ = producto
                    # Actualizar stock real
                    cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?", (cantidad, codigo))
                    # Insertar en la tabla ventas incluyendo el nombre
                    cursor.execute(
                        "INSERT INTO ventas (codigo, nombre, cantidad, fecha) VALUES (?, ?, ?, ?)",
                        (codigo, nombre, cantidad, fecha_actual)
                    )
            conn.commit()
        # Limpiar campos al guardar venta
        lista_compras.delete(0, tk.END)
        productos_vendidos.clear()
        stock_temporal.clear()
        numero_productos.set(0)
        total_compra.set(0)
        producto_var.set("Venta guardada correctamente.")

# boton verificar producto
    boton_verificar = tk.Button(contenedor_verificar_producto, text="Verificar producto", font=("Arial", 14), command=verificar_producto)
    estilo_botones_general(boton_verificar)
    posicionar(boton_verificar, x=0.5, y=0.5, anchor=tk.CENTER)

    # funcion para verificar y registrar el producto a la vez
    def registrar_y_verificar(event=None):
        registrar_producto()
        verificar_producto()
        
# boton registrar producto
    boton_registrar = tk.Button(contenedor_verificar_producto, text="Registrar producto", font=("Arial", 14), command=registrar_y_verificar)
    estilo_botones_general(boton_registrar)
    posicionar(boton_registrar, x=0.5, y=0.6, anchor=tk.CENTER)
    ventana_cajero.bind('<Return>', registrar_y_verificar)
    
# boton guardar venta
    boton_calcular_total = tk.Button(contenedor_verificar_producto, text="Guardar venta", font=("Arial", 14), command=guardar_venta_db)
    estilo_botones_general(boton_calcular_total)
    posicionar(boton_calcular_total, x=0.5, y=0.7, anchor=tk.CENTER)