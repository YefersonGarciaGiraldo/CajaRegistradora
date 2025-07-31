<!-- SISTEMA DE CAJA REGISTRADORA -->

<!-- INTRODUCCIÓN 

Este sistema permite gestionar productos, registrar ventas,
visualizar historial, actualizar productos, y exportar a excel 
desde una interfaz gráfica amigable construida con Tkinter. 
Está pensado para pequeñas tiendas o negocios que necesiten 
un control básico de ventas sin conexión a internet. 
Funcional tanto para administradores como para cajeros.
-->

<!-- CARACTERISTICAS PRINCIPALES 

Gestión de usuarios (Administrador y Cajero) 
Registro, actualización y eliminación de productos
Registro de ventas con fecha y hora
Historial de ventas con búsqueda y exportación a Excel
Buscador dinámico en productos
-->

<!-- TECNOLOGIAS USADAS 

Python (backend) 
Tkinter (interfaz gráfica)
SQLite (base de datos local)
openpyxl (exportar historial a Excel) 
-->

<!--INSTALACIÓN para desarrolladores

1. 
Clona el repositorio:
"git clone https://github.com/YefersonGarciaGiraldo/cajaRegistradora.git"

2.
Instala la dependencia desde tu consola: 
"pip install openpyxl"
3.
Ejecuta el programa:
"python ventanaInicio.py"

(Asegurate de tener Python 3.8 o superior)
-->

<!--INSTALACIÓN para usuarios no programadores
1.
Descarga: 
"CajaRegistradora.exe"

2.
Haz doble click para abrir el sistema

3.
Usa la interfa sin instalar nada más

(Si ves un error de antivirus, marca la app como segura. No contiene virus.)
-->

<!-- ESTRUCTURA DEL PROYECTO

caja_registradora/
├── carpetaAdministrador/
│   ├── seccion_historial_ventas.py
│   ├── listaProductos.py
│   ├── seccion_modificar_productos.py
│   ├── seccionAdministrador.py
│   └── seccionEliminarProductos/
├── recursos/
│   ├── imagen_caja_registradora.png
│   └── icono_caja_registradora.ico
├── database.py
├── funciones.py
├── seccionCajero.py
├── seccionUsuarios.py
├── productos.db
└── ventanaInicio.py
-->

<!-- 
AUTOR:
Yeferson Alexander García Giraldo

CORREO:
yeff.dev@gmail.com

GIT HUB:
https://github.com/YefersonGarciaGiraldo
 --># CajaRegistradora
