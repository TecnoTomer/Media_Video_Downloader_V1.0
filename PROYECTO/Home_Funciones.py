import tkinter as tk
import Variables
import subprocess
import Botones_Funciones
import Youtube_Funciones

def al_cerrar_ventana():
	Variables.root.destroy()

def screen_holding():
	subprocess.run(["lib/Screen_Holding.exe"])

def Barra_superior():
	#BARRA SUPERIOR
	barra_opcion = tk.Frame(Variables.root, bg=Variables.c_barras)
	barra_opcion.pack(side='top', fill='x')

	#BOTON YOUTUBE
	b_home = tk.Label(barra_opcion, text='YouTube', bg=Variables.c_barras, width=10, font=(Variables.poppins, 10))
	b_home.pack(side='left', padx=0)
	b_home.bind("<Button-1>", Botones_Funciones.cambio_ventana(Youtube_Funciones.Centro_youtube, Centro_p))
	Botones_Funciones.selecion_boton(b_home)
	
	#USER DATA LABEL
	b_ayuda = tk.Label(barra_opcion, text=f'{Variables.Usuario}', bg=Variables.c_barras)
	b_ayuda.pack(side='right', padx=10)

def crear_windows_principal():
	Variables.root.title(Variables.titulo)
	Variables.root.iconbitmap(Variables.icono_v)

	Variables.root.geometry(f"{700}x{400}")
	Variables.root.resizable(0,0)

	Barra_superior()
	
	global Centro_p
	Centro_p = tk.Frame(Variables.root, bg="blue")
	Centro_p.pack(side="top", fill="both", expand=True)

	Variables.root.protocol("WM_DELETE_WINDOW", al_cerrar_ventana)
	Variables.root.mainloop()