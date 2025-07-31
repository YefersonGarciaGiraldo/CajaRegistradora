import tkinter as tk
from tkinter import ttk, messagebox
# importaciones locales
from funciones import posicionar, tamaño_ventana, estilo_botones_general, placeholder_combobox, ruta_recurso
from database import consultar_productos, eliminar_producto_data

# ventana principal
def ventana_eliminar_producto():
    ventana_eliminar = tk.Toplevel(bg="#f0f8ff")
    ventana_eliminar.title("Eliminar Producto")
    ventana_eliminar.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_eliminar)

    # Contenedor para centrar
    contenedor_eliminar = tk.Frame(ventana_eliminar, bg="#f0f8ff", bd=2, relief="groove")
    posicionar(contenedor_eliminar, x=0.5, y=0.5, width=0.5, height=0.4, anchor=tk.CENTER)

    # Título e instrucción
    label_codigo = tk.Label(contenedor_eliminar,text="Seleccione el producto a eliminar:",bg="#f0f8ff",fg="#1477B5",font=("Arial", 16, "bold"))
    label_codigo.pack(pady=(30, 10))

    # Obtener productos
    resultados = consultar_productos()
    productos = [f"{codigo} - {nombre}" for codigo, nombre, precio, cantidad in resultados]

    # Combobox
    combo_eliminar = ttk.Combobox(contenedor_eliminar,values=productos,font=("Arial", 14),width=45)
    combo_eliminar.pack(pady=20)
    placeholder_combobox(combo_eliminar, "Seleccione el producto")

    # Filtrar productos
    def filtrar(event):
        valor = combo_eliminar.get()
        if valor == "":
            combo_eliminar['values'] = productos
        else:
            filtrados = [p for p in productos if valor.lower() in p.lower()]
            combo_eliminar['values'] = filtrados
    combo_eliminar.bind("<KeyRelease>", filtrar)

    # Función eliminar
    def eliminar_producto():
        seleccion = combo_eliminar.get()
        if seleccion and " - " in seleccion:
            codigo = seleccion.split(" - ")[0]
            resultado = eliminar_producto_data(codigo)
            if resultado > 0:
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                actualizar_lista()
            else:
                messagebox.showerror("Error", "No se encontró un producto con ese código.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione o ingrese un código válido.")

    # Botón eliminar
    boton_eliminar = tk.Button(contenedor_eliminar,text="Eliminar Producto",command=eliminar_producto)
    boton_eliminar.pack(pady=30)
    estilo_botones_general(boton_eliminar)

    # Actualizar lista después de eliminar
    def actualizar_lista():
        nonlocal productos
        resultados_actualizados = consultar_productos()
        productos = [f"{codigo} - {nombre}" for codigo, nombre, precio, cantidad in resultados_actualizados]
        combo_eliminar['values'] = productos
        combo_eliminar.set("Seleccione o ingrese el código")
        combo_eliminar.configure(foreground='grey')
    return ventana_eliminar