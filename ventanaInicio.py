import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime

### importaciones locales###
from seccionUsuarios import ventanaUsuarios
from seccionCajero import cajero
from carpetaAdministrador.seccionAdministrador import administrador
from funciones import estilo_botones_inicio, estilo_botones_general, tamaño_ventana, ruta_recurso
from database import crear_tabla_productos, tabla_historial_ventas
from carpetaAdministrador.seccionAdministrador import lista_productos
from carpetaAdministrador.seccion_historial_ventas import funcion_historial_ventas

# Inicializar base de datos
crear_tabla_productos()
tabla_historial_ventas()

# ventana principal
ventana_ingreso = tk.Tk()
ventana_ingreso.title("Caja Registradora")
ventana_ingreso.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
tamaño_ventana(ventana_ingreso)

# contenedor barra lateral
barra_lateral = tk.Frame(ventana_ingreso, bg="#1477B5", width=200)
barra_lateral.pack(side="left", fill="y")

# funcion para crear un logo circular
import os  # Asegúrate de tener esto arriba

def crear_imagen_circular(ruta, tamaño):
    ruta_abs = ruta_recurso(ruta)
    img = Image.open(ruta_abs).resize(tamaño).convert("RGBA")
    mascara = Image.new('L', tamaño, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, tamaño[0], tamaño[1]), fill=255)
    img.putalpha(mascara)
    return ImageTk.PhotoImage(img)



# logo en barra lateral de navegacion
imagen_barra_lateral = crear_imagen_circular(ruta_recurso("recursos/imagen_caja_registradora.png"), (80, 80))
label_logo_barra_lateral = tk.Label(barra_lateral, image=imagen_barra_lateral, bg="#1477B5")
label_logo_barra_lateral.pack(pady=20)

# Botones de navegación en barra_lateral
def crear_boton_barra_lateral(texto, comando):
    boton = tk.Button(
        barra_lateral,
        text=texto,
        command=comando
    )
    boton.pack(fill="x", pady=5)
    estilo_botones_inicio(boton)
    return boton

# Botón Usuarios con menú desplegable
def menu_usuarios():
    if contenedor_menu_usuarios.winfo_ismapped():
        contenedor_menu_usuarios.pack_forget()
    else:
        contenedor_menu_usuarios.pack(fill="x")
boton_usuarios = crear_boton_barra_lateral("Usuarios ▾", menu_usuarios)

# contenedor oculto para opciones de usuario
contenedor_menu_usuarios = tk.Frame(barra_lateral, bg="#0f5c8c")

# boton Administrador
boton_admin = tk.Button(
    contenedor_menu_usuarios,
    text="Administrador",
    command=lambda: administrador()
)
boton_admin.pack(fill="x")
estilo_botones_inicio(boton_admin)

# boton Cajero
boton_cajero = tk.Button(
    contenedor_menu_usuarios,
    text="Cajero",
    command=lambda: cajero()
)
boton_cajero.pack(fill="x")
estilo_botones_inicio(boton_cajero)

# Resto de botones de la barra lateral
crear_boton_barra_lateral("Productos", lambda: lista_productos())
crear_boton_barra_lateral("Ventas", lambda: funcion_historial_ventas())
crear_boton_barra_lateral("Reportes", lambda: print("Abrir reportes")) #modificar
crear_boton_barra_lateral("Configuración", lambda: print("Abrir configuración")) #modificar

# header, contiene un titulo breve, la hora y la fecha en la parte superior de la ventana
header = tk.Frame(ventana_ingreso, bg="#ffffff", height=60)
header.pack(side="top", fill="x")
# etiqueta titulo
etiqueta_titulo = tk.Label(header, text="Sistema de Caja Registradora", font=("Arial", 18, "bold"), bg="#ffffff" , fg="#1477B5")
etiqueta_titulo.pack(side="left", padx=20)
# Hora y fecha 
etiqueta_hora = tk.Label(header, font=("Arial", 14), bg="#ffffff", fg="#333333")
etiqueta_hora.pack(side="right", padx=20)
etiqueta_fecha = tk.Label(header, font=("Arial", 14), bg="#ffffff", fg="#333333")
etiqueta_fecha.pack(side="right", padx=20)
# funcion que actualiza a hora y fecha
def actualizar_fecha_hora():
    ahora = datetime.now()
    fecha = ahora.strftime("%d/%m/%Y") #dd/mm/aaaa
    hora = ahora.strftime("%I:%M:%S %p")  # 12 horas con am/pm
    etiqueta_fecha.config(text=f"Fecha: {fecha}")
    etiqueta_hora.config(text=f"Hora: {hora}")
    ventana_ingreso.after(1000, actualizar_fecha_hora)
actualizar_fecha_hora()

###area principal###
area_principal = tk.Frame(ventana_ingreso, bg="#f0f8ff")
area_principal.pack(expand=True, fill="both")
# Bienvenida
label_bienvenida = tk.Label(area_principal,text="Bienvenido a la Caja Registradora",font=("Arial", 20, "bold"),bg="#f0f8ff",fg="#333333")
label_bienvenida.pack(pady=40)
# Imagen principal central
imagen_central = crear_imagen_circular("recursos/imagen_caja_registradora.png", (150, 150))
label_imagen_central = tk.Label(area_principal, image=imagen_central, bg="#f0f8ff")
label_imagen_central.pack(pady=20)
# Botón ingresar grande
boton_ingresar = tk.Button(area_principal,text="Ingresar al Sistema",command=lambda: ventanaUsuarios())
boton_ingresar.pack(pady=30)
estilo_botones_general(boton_ingresar)

###footer###
footer = tk.Frame(ventana_ingreso, bg="#1477B5", height=30)
footer.pack(side="bottom", fill="x")
label_footer = tk.Label(footer, text="Desarrollado por Yeferson Garcia - v1.0", font=("Arial", 10), bg="#1477B5", fg="white")
label_footer.pack(pady=5)

# bucle principal
ventana_ingreso.mainloop() 