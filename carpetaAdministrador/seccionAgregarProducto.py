import tkinter as tk
from tkinter import messagebox
# importaciones locales
from database import agregar_producto
from funciones import posicionar, tamaño_ventana, placeholder, estilo_botones_general, ruta_recurso

# ventana principal
def ventana_agregar():
    ventana_agregar_producto = tk.Toplevel(bg="#f0f8ff")
    ventana_agregar_producto.title("Agregar Producto")
    ventana_agregar_producto.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_agregar_producto)

    # contenedor para centrar
    contenedor_agregar = tk.Frame(ventana_agregar_producto, bg="#f0f8ff", bd=2, relief="groove")
    posicionar(contenedor_agregar, x=0.5, y=0.5, width=0.5, height=0.85, anchor=tk.CENTER)

    # Título principal
    titulo = tk.Label(contenedor_agregar, text="Registro de Nuevo Producto", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#1477B5")
    titulo.pack(pady=(20, 10))

    # etiqueta de Código
    etiqueta_codigo = tk.Label(contenedor_agregar, text="Código del Producto:", bg="#f0f8ff", fg="#1477B5", font=("Arial", 12, "bold"))
    etiqueta_codigo.pack(anchor="w", padx=40, pady=(15, 5))
    # entry de codigo
    entrada_codigo = tk.Entry(contenedor_agregar, font=("Arial", 12), width=40, relief="solid", bd=1)
    entrada_codigo.pack(pady=5)
    placeholder(entrada_codigo, "Ej: A001")

    #etiqueta nombre
    etiqueta_nombre = tk.Label(contenedor_agregar, text="Nombre del Producto:", bg="#f0f8ff", fg="#1477B5", font=("Arial", 12, "bold"))
    etiqueta_nombre.pack(anchor="w", padx=40, pady=(15, 5))
    # entry nombre
    entrada_nombre = tk.Entry(contenedor_agregar, font=("Arial", 12), width=40, relief="solid", bd=1)
    entrada_nombre.pack(pady=5)
    placeholder(entrada_nombre, "Ej: Producto")

    #etiqueta precio
    etiqueta_precio = tk.Label(contenedor_agregar, text="Precio del Producto:", bg="#f0f8ff", fg="#1477B5", font=("Arial", 12, "bold"))
    etiqueta_precio.pack(anchor="w", padx=40, pady=(15, 5))
    # entry precio
    entrada_precio = tk.Entry(contenedor_agregar, font=("Arial", 12), width=40, relief="solid", bd=1)
    entrada_precio.pack(pady=5)
    placeholder(entrada_precio, "Ej: 5500")

    #etiqueta cantidad
    etiqueta_cantidad = tk.Label(contenedor_agregar, text="Cantidad en Stock:", bg="#f0f8ff", fg="#1477B5", font=("Arial", 12, "bold"))
    etiqueta_cantidad.pack(anchor="w", padx=40, pady=(15, 5))
    # entry cantidad
    entrada_cantidad = tk.Entry(contenedor_agregar, font=("Arial", 12), width=40, relief="solid", bd=1)
    entrada_cantidad.pack(pady=5)
    placeholder(entrada_cantidad, "Ej: 15")

    # funcion para guardar el nuevo producto
    def registrar_producto():
        try:
            codigo = entrada_codigo.get()
            nombre = entrada_nombre.get()
            precio = float(entrada_precio.get())
            cantidad = int(entrada_cantidad.get())
            resultado = agregar_producto(codigo, nombre, precio, cantidad)
            if resultado:
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
                entrada_codigo.delete(0, tk.END)
                entrada_nombre.delete(0, tk.END)
                entrada_precio.delete(0, tk.END)
                entrada_cantidad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "El código del producto ya existe.")
        except ValueError:
            messagebox.showerror("Error", "Precio o cantidad inválidos.")

    #boton para agregar el nuevo producto
    boton_agregar = tk.Button(contenedor_agregar, text="Agregar Producto", command=registrar_producto, cursor="hand2")
    boton_agregar.pack(pady=25)
    estilo_botones_general(boton_agregar)
    ventana_agregar_producto.bind('<Return>', lambda event: registrar_producto())

    return ventana_agregar_producto