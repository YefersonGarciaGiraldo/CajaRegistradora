import tkinter as tk
# importaciones locales
from funciones import posicionar,estilo_botones_general, tamaño_ventana, ruta_recurso
from seccionCajero import cajero
from carpetaAdministrador.seccionAdministrador import administrador

#ventana principal
def ventanaUsuarios():
    ventana_usuarios = tk.Toplevel()
    ventana_usuarios.title("Usuarios")
    ventana_usuarios.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_usuarios)

# contenedor principal
    contenedor_principal = tk.Frame(ventana_usuarios, bg="#F0F8FF")
    posicionar(contenedor_principal,x=0.5, y=0.5,anchor=tk.CENTER)
    contenedor_principal.pack(expand=True)

# etiqueta de entrada
    usuarios_label = tk.Label(contenedor_principal,text= "SELECCIONE UN USUARIO DE INGRESO",font= ("Arial", 20, "bold"),bg="#F0F8FF",fg="#3B3A3A")
    usuarios_label.pack(pady=20)

# boton ingreso administrador
    boton_admin = tk.Button(contenedor_principal,text="ADMINISTRADOR",command=lambda: (administrador(), ventana_usuarios.destroy()))
    boton_admin.pack(pady=10)
    estilo_botones_general(boton_admin)

# boton ingreso cajero
    boton_cajero = tk.Button(contenedor_principal,text="CAJA",command=lambda: (cajero(), ventana_usuarios.destroy()))
    boton_cajero.pack(pady=10)
    estilo_botones_general(boton_cajero)