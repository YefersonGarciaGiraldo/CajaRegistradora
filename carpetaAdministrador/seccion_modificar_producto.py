import tkinter as tk
from tkinter import ttk, messagebox
# importaciones locales
from database import consultar_productos, actualizar_producto
from funciones import placeholder_combobox, estilo_botones_general, tamaño_ventana, placeholder, posicionar, ruta_recurso

# ventana principal
def ventanaModificarProducto():
    ventana_modificar = tk.Toplevel(bg="#f0f2f5")
    ventana_modificar.title("Modificar producto")
    ventana_modificar.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_modificar)

    # Consultar productos
    resultados = consultar_productos()
    productos = [f"{codigo} - {nombre}" for codigo, nombre, precio, cantidad in resultados]

    # Contenedor con borde
    contenedor = tk.Frame(ventana_modificar, bg="#f0f8ff", bd=2, relief="groove")
    posicionar(contenedor, x=0.5, y=0.5, width=0.5, height=0.5, anchor=tk.CENTER)

    # Etiqueta de instruccion
    titulo = tk.Label(contenedor, text="Seleccione un producto:", bg="#f0f8ff", fg="#1477B5" , font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Combobox de productos
    combo = ttk.Combobox(contenedor, values=productos, font=("Arial", 14), width=35)
    combo.pack(pady=5)
    placeholder_combobox(combo, "Seleccione el producto a modificar.")

    # Filtrar productos
    def filtrar(event):
        valor = combo.get()
        if valor.strip() == "" or valor == "Buscar por código o nombre...":
            combo['values'] = productos
        else:
            filtrados = [p for p in productos if valor.lower() in p.lower()]
            combo['values'] = filtrados

    combo.bind('<KeyRelease>', filtrar)

# Campos de edición
    # nombre
    etiqueta_nombre = tk.Label(contenedor, text="Nuevo nombre:", bg="#f0f8ff", fg="#1477B5", font=("Arial", 14, "bold"))
    etiqueta_nombre.pack(pady=5)
    entry_nombre = tk.Entry(contenedor, font=("Arial", 12), width=45)
    entry_nombre.pack(pady=2)
    placeholder(entry_nombre, "Ej: Producto")
    # precio
    etiqueta_precio = tk.Label(contenedor, text="Nuevo precio:", bg="#f0f8ff",fg="#1477B5", font=("Arial", 14, "bold"))
    etiqueta_precio.pack(pady=5)
    entry_precio = tk.Entry(contenedor, font=("Arial", 12), width=45)
    entry_precio.pack(pady=2)
    placeholder(entry_precio, "Ej: 1200")
    # cantidad
    etiqueta_cantidad = tk.Label(contenedor, text="Nueva cantidad:", bg="#f0f8ff",fg="#1477B5", font=("Arial", 14, "bold"))
    etiqueta_cantidad.pack(pady=5)
    entry_cantidad = tk.Entry(contenedor, font=("Arial", 12), width=45)
    entry_cantidad.pack(pady=2)
    placeholder(entry_cantidad, "Ej: 15")

    # Función actualizar
    def modificar_producto():
        seleccionado = combo.get()
        if not seleccionado or " - " not in seleccionado or seleccionado == "Buscar por código o nombre...":
            messagebox.showwarning("Atención", "Seleccione un producto válido")
            return
        codigo = seleccionado.split(" - ")[0]
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        if not nombre or not precio or not cantidad:
            messagebox.showwarning("Atención", "Complete todos los campos")
            return
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser número y cantidad un entero")
            return
        filas = actualizar_producto(nombre, codigo, precio, cantidad)
        if filas > 0:
            messagebox.showinfo("Éxito", "Producto actualizado correctamente")
            ventana_modificar.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto")

    # Botón actualizar
    boton_actualizar = tk.Button(contenedor,text="Actualizar producto",command=modificar_producto)
    boton_actualizar.pack(pady=15)
    estilo_botones_general(boton_actualizar)

    return ventanaModificarProducto