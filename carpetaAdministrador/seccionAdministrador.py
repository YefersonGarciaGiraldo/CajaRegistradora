# import libreria tkinter
import tkinter as tk

# imports locales necesarias para la ventana
from funciones import posicionar,estilo_botones_general, tamaño_ventana, ruta_recurso
from carpetaAdministrador.seccionAgregarProducto import ventana_agregar
from carpetaAdministrador.listaProductos import lista_productos
from carpetaAdministrador.seccionEliminarProducto import ventana_eliminar_producto
from carpetaAdministrador.seccion_historial_ventas import funcion_historial_ventas
from carpetaAdministrador.seccion_modificar_producto import ventanaModificarProducto

# ventana administrador
def administrador():
    ventana_administrador = tk.Toplevel()
    ventana_administrador.title("Ha ingresado como administrador")
    ventana_administrador.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_administrador)

# contenedor principal para centrar
    contenedor_principal = tk.Frame(ventana_administrador, bg="#F0F8FF")
    posicionar(contenedor_principal,x=0.5,y=0.5,width=0.8, height=0.8, anchor=tk.CENTER)
    
# etiqueta bienevenida administrador
    etiqueta_admin = tk.Label(
    contenedor_principal, 
    text="Bienvenido, ingresaste como administrador", 
    font=("Arial", 14, "bold"), 
    fg="#333333",
    bg="#F0F8FF"
    )
    etiqueta_admin.pack(pady=40)

# contenedor secundario para botones
    contenedor_administrador = tk.Frame(contenedor_principal, bg="#F0F8FF")
    posicionar(contenedor_administrador, x=0.5,y=0.5,width=0.3, height= 0.6, anchor= tk.CENTER)

# botón agregar producto
    boton_agregar_producto = tk.Button(contenedor_administrador,text="Agregar Producto",command=lambda: ventana_agregar())
    boton_agregar_producto.pack(pady=10)
    estilo_botones_general(boton_agregar_producto)

# botón eliminar producto
    boton_eliminar_producto = tk.Button(contenedor_administrador,text="Eliminar Producto",command=lambda: ventana_eliminar_producto())
    boton_eliminar_producto.pack(pady=10)
    estilo_botones_general(boton_eliminar_producto)

# botón modificar producto
    boton_modificar_producto = tk.Button(contenedor_administrador,text="Modificar Producto",command=lambda: ventanaModificarProducto())
    boton_modificar_producto.pack(pady=10)
    estilo_botones_general(boton_modificar_producto)

# botón lista de productos disponibles
    boton_productos_disponibles= tk.Button(contenedor_administrador,text="Productos Disponibles",command=lambda: lista_productos())
    boton_productos_disponibles.pack(pady=10)
    estilo_botones_general(boton_productos_disponibles)

# botón mostrar historial de ventas
    boton_historial_ventas = tk.Button(contenedor_administrador,text="Historial de Ventas",command=lambda: funcion_historial_ventas())
    boton_historial_ventas.pack(pady=10)
    estilo_botones_general(boton_historial_ventas)
    return administrador