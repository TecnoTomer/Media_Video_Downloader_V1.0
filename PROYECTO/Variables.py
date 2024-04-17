import tkinter as tk 
from tkinter import font
import getpass

##########################
        #VENTANA
##########################
#Variables inicializador de ventana
root = tk.Tk() #inicializar tk ventana root

titulo = "Media Downloader V1.0"
icono_v = "lib/data/icon.ico"

#VIDEOS INFORMACION
Pendiente = "Pendiente"
Terminado = "Terminado"
cantidad = 0

entry_lik = ""
enlace = ""
fila = 0

##########################
        #DATA
##########################
Usuario = getpass.getuser()

##########################
      #VENTANA FUENTES
##########################
ruta_fuente = "lib/data/fuente/poppins.ttf"
poppins_negrita = font.Font(family="Popins", weight="bold")
poppins = font.Font(family="Popins")

##########################
      #DOCUMENTOS
##########################
Youtube_logo = "lib/data/Youtube_logo.png"
Youtube_logo1 = "lib/data/Youtube_logo1.png"
Campo_busqueda = "lib/data/bar_search.png"
lupa = "lib/data/search.png"
lupa1 = "lib/data/search1.png"
D_seleccion = "lib/data/D_selecion.png"
D_seleccion1 = "lib/data/D_selecion1.png"
D_todo = "lib/data/D_Todo.png"
D_todo1 = "lib/data/D_Todo1.png"
recicle = "lib/data/recile.png"
recicle1 = "lib/data/recile1.png"

data_excel = "lib/data/y_data.xlsx"
yotube_link = "https://www.youtube.com"

##########################
      #VENTANA COLORES
##########################
#Youtube paleta 
Y_boton = '#F53939'
Y_backgroun = '#080B1E'

#barra superior
c_barras = "#FFFFFF"
c_selecion = "#C7C7C9"

