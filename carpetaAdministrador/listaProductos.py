import tkinter as tk
from tkinter import ttk
# importaciones locales
from database import consultar_productos
from funciones import tamaño_ventana, posicionar, ruta_recurso
# ventana principal
def lista_productos():
    ventana = tk.Toplevel()
    ventana.title("Lista de Productos")
    ventana.conbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana)

    # Título
    titulo = tk.Label(ventana, text="Productos Disponibles", font=("Arial", 18, "bold"), fg="#1477B5", bg="#f0f8ff")
    titulo.pack(pady=10)

    # Contenedor principal
    contenedor = tk.Frame(ventana, bg="#f0f8ff", bd=2, relief="groove")
    posicionar(contenedor, x=0.5, y=0.5, anchor=tk.CENTER)
    contenedor.place(relwidth=0.9, relheight=0.75)
# barra de busqueda
    # instruccion
    instruccion = tk.Label(contenedor,text="Barra de busqueda", fg="#1477B5", bg="#f0f8ff")
    instruccion.pack(pady=1)
    # Barra de búsqueda
    search_var = tk.StringVar()
    entry_busqueda = tk.Entry(contenedor, textvariable=search_var, font=("Arial", 12))
    entry_busqueda.pack(pady=10)
#  tabla  
    # Tabla de productos disponibles
    columnas = ("Código", "Nombre", "Precio", "Cantidad")
    tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=20)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150, anchor="center")
    tabla.pack(fill="both", expand=True, padx=10, pady=5)
    # Estilo para resaltar sin stock
    style = ttk.Style()
    style.configure("Red.Treeview", foreground="black", font=("Arial", 11))
    style.map("Treeview", background=[("selected", "#ccccff")])
    # Consultar y cargar productos
    productos = consultar_productos()

    def cargar_productos(filtrados):
        for row in tabla.get_children():
            tabla.delete(row)
        for index, p in enumerate(filtrados):
            color = "#ffdddd" if p[3] == 0 else ("#f9f9f9" if index % 2 == 0 else "white")
            tags = ("sin_stock" if p[3] == 0 else "normal")
            tabla.insert("", "end", values=p, tags=tags)
        tabla.tag_configure("sin_stock", background="#cf1212")
        tabla.tag_configure("normal", background="#f9f9f9")

    cargar_productos(productos)

    # Función de filtrado
    def filtrar(*args):
        termino = search_var.get().lower()
        filtrados = [p for p in productos if termino in str(p[0]).lower() or termino in str(p[1]).lower()]
        cargar_productos(filtrados)
    search_var.trace_add("write", filtrar)
    return ventana