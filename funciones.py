import tkinter as tk
import os
import sys
### FUNCIONES QUE SE USAN EN TODOS LOS ARCHIVOS ###

#simular un placeholder en un Entry
def placeholder(entry, texto):
    entry.insert(0, texto)
    entry.config(fg="grey")
    entry.focus()
    def on_entry_click(event):
        if entry.get() == texto:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def on_focusout(event):
        if entry.get() == "":
            entry.insert(0, texto)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focusout)

# simular placeholder para combobox
def placeholder_combobox(combo, texto):
    combo.set(texto)
    combo.configure(foreground='grey')

    def on_focus_in(event):
        if combo.get() == texto:
            combo.set("")
            combo.configure(foreground='black')

    def on_focus_out(event):
        if combo.get() == "":
            combo.set(texto)
            combo.configure(foreground='grey')

    combo.bind("<FocusIn>", on_focus_in)
    combo.bind("<FocusOut>", on_focus_out)

# Función para posicionar widgets y contenedores usando .place con porcentajes
# Permite especificar posición y tamaño relativos
def posicionar(widget, x=0, y=0, width=None, height=None, anchor= "nw"):
    kwargs = {"relx": x, "rely": y, "anchor": anchor} 
    if width is not None:
        kwargs["relwidth"] = width
    if height is not None:
        kwargs["relheight"] = height
    widget.place(**kwargs)
 
# simula el hoover en los botones, trabaja dentro de las funciones para estilo de botones
def hover_boton (boton, color_hover="#113E5A", color_salida="#1477B5", fg_hover="white", fg_salida="white"):
    def on_enter(event):
        boton.config(bg=color_hover, fg=fg_hover)
    def on_leave(event):
        boton.config(bg=color_salida, fg=fg_salida)
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)

# funcion para estilo  de los botones de la ventana principal
def estilo_botones_inicio(boton):
    boton.config(
        font=("Arial", 12, "bold"),
        bg="#1477B5",
        fg="white",
        activebackground="#0f5c8c",
        activeforeground="white",
        bd=0,
        relief="flat",
        cursor="hand2",
    )
    hover_boton(boton)

# funcion estilos botones general
def estilo_botones_general(boton):
    boton.config(
    font=("Arial", 14,"bold"),
    bg="#1477B5",
    fg="white",
    activebackground="#0f5c8c",
    activeforeground="white",
    relief= "flat",
    cursor="hand2",
    width=20,
    height= 1,
    )
    hover_boton(boton)

# funcion para abrir ventana maximizada con barra superior visible
def tamaño_ventana(ventana, color="#f0f8ff"):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    ventana.geometry(f"{screen_width}x{screen_height - 40}+0+0")
    ventana.config(bg=color)
    ventana.focus_set()
#minimizar ventana con escape
    def salir_modo_grande(event=None):
        print("Escape presionado")
        # Reset visual para asegurar que no esté en fullscreen ni maximizada
        ventana.overrideredirect(False)
        ventana.state("normal")
        # Nuevo tamaño y ubicación centrada
        ancho = 1000
        alto = 600
        x = int((screen_width - ancho) / 2)
        y = int((screen_height - alto) / 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana.update_idletasks()
    ventana.bind("<Escape>", salir_modo_grande)

# funcion para agregarle icono a cada ventana, compatible con .exe
def ruta_recurso(rel_path):
    try:
        base_path = sys._MEIPASS 
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)
