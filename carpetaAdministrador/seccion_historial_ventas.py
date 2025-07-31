import tkinter as tk
from tkinter import ttk, messagebox
import openpyxl
# importaciones locales
from database import historial_ventas
from funciones import posicionar, estilo_botones_general, tamaño_ventana, placeholder, ruta_recurso

# ventana principal
def funcion_historial_ventas():
    ventana_historial = tk.Toplevel()
    ventana_historial.title("Historial de Ventas")
    ventana_historial.iconbitmap(ruta_recurso("recursos/icono_caja_registradora.ico"))
    tamaño_ventana(ventana_historial)
    
    # Contenedor principal
    contenedor = tk.Frame(ventana_historial, bg="#f0f8ff")
    posicionar(contenedor, x=0.5, y=0.5, anchor=tk.CENTER)
    contenedor.place(relwidth=0.9, relheight=0.75)

    # Título
    titulo = tk.Label(contenedor, text="Historial de Ventas", font=("Arial", 22, "bold"), bg="#f0f8ff", fg="#1477B5")
    posicionar(titulo, x=0.5, y=0.07, anchor=tk.CENTER)

    # Barra de búsqueda
    entry_busqueda = tk.Entry(contenedor, font=("Arial", 12), width=40)
    posicionar(entry_busqueda, x=0.5, y=0.15, anchor=tk.CENTER)
    placeholder(entry_busqueda, "Buscar por código o nombre...")

    # Tabla
    columnas = ("codigo", "producto", "cantidad", "fecha")
    tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=15)
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
    tabla.column("codigo", width=80)
    tabla.column("producto", width=200)
    tabla.column("cantidad", width=80)
    tabla.column("fecha", width=120)
    posicionar(tabla, x=0.5, y=0.55, width=0.9, height=0.7, anchor=tk.CENTER)
    scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    posicionar(scrollbar, x=0.95, y=0.55, height=0.7, anchor="w")

    # Obtener y guardar todas las ventas
    ventas = historial_ventas()
    ventas_original = ventas.copy() if ventas else []

    def mostrar_resultados(filtrados):
        tabla.delete(*tabla.get_children())
        for index, v in enumerate(filtrados):
            tabla.insert("", "end", values=(v[1], v[2], v[3], v[4]))

    def filtrar_historial(event=None):
        texto = entry_busqueda.get().lower()
        filtrados = [
            v for v in ventas_original
            if texto in str(v[1]).lower() or texto in str(v[2]).lower()
        ]
        mostrar_resultados(filtrados)
    entry_busqueda.bind("<KeyRelease>", filtrar_historial)
    if not ventas:
        messagebox.showinfo("Información", "No hay ventas registradas.")
        ventana_historial.destroy()
        return
    mostrar_resultados(ventas_original)

# Exportar a Excel
    def exportar_excel():
        ventas = historial_ventas()
        if not ventas:
            messagebox.showinfo("Información", "No hay ventas para exportar.")
            return
        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Historial Ventas"
            ws.append(["Código", "Producto", "Cantidad", "Fecha"])
            for venta in ventas:
                ws.append(venta[1:])
            wb.save("historial_ventas.xlsx")
            messagebox.showinfo("Éxito", "Historial exportado a historial_ventas.xlsx")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")

    # Botón exportar
    boton_excel = tk.Button(contenedor, text="Exportar a Excel", command=exportar_excel)
    posicionar(boton_excel, x=0.3, y=0.95, anchor=tk.CENTER)
    estilo_botones_general(boton_excel)

    # Botón cerrar
    boton_cerrar = tk.Button(contenedor, text="Cerrar", command=ventana_historial.destroy)
    posicionar(boton_cerrar, x=0.7, y=0.95, anchor=tk.CENTER)
    estilo_botones_general(boton_cerrar)
