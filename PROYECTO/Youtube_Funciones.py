import tkinter as tk
from tkinter import ttk
from pytube import YouTube, Playlist
import webbrowser
import time

import Variables
import Home_Funciones
import Botones_Funciones
import Alertas

def Centro_youtube(frame):
    global Centro_y
    Centro_y = tk.Frame(Home_Funciones.Centro_p, bg=Variables.Y_backgroun)
    Centro_y.pack(side="top", fill="both", expand=True)

    # Crear dos subframes dentro de Centro_y
    global frame1_botones
    frame1_botones = tk.Frame(Centro_y, bg=Variables.Y_backgroun, height=30)
    frame1_botones.pack(side="top", fill="both", expand=True)

    global frame2_treeview
    frame2_treeview = tk.Frame(Centro_y, bg=Variables.Y_backgroun)
    frame2_treeview.pack(side="top", fill="both", expand=True)

    #BOTONES
    logo = Botones_Funciones.search_boton(Variables.Youtube_logo1, Variables.Youtube_logo, 120, 40, 15, 20) #logo youtube
    logo.bind("<Button-1>", lambda event: buscar_video())

    Botones_Funciones.logos(Variables.Campo_busqueda, 530, 40, 140, 20) #barra busqueda de presentacion solamente

    global entry
    entry = Botones_Funciones.Barra_busqueda(frame1_botones, 50, 150, 33) #entry de busqueda

    B_lupa = Botones_Funciones.search_boton(Variables.lupa1, Variables.lupa, 35, 25, 615, 28) #boton busqueda
    B_lupa.bind("<Button-1>", lambda event: B_y_buscar())

    #BOTONES
    def actualizar_calidades(*args): # habilita o desabilida campo calidad si el formato es mp3
        if formato.get() == "Mp4":
            calidades_list.config(state="readonly")  # Habilitar el Combobox de la calidad
        else:
            calidades_list.set("")  # Limpiar la selección de la calidad
            calidades_list.config(state="disabled")

    #Formato
    Texto_Formato = tk.Label(frame1_botones, text="Formato",fg=Variables.c_barras, bg=Variables.Y_backgroun, font=(Variables.poppins)) # por ejemplo, WPA2, WPA3
    Texto_Formato.place(x=66, y=64)
    Lista_Formato = ["Mp4", "Mp3"]
    formato = tk.StringVar()
    formato.trace_add("write", actualizar_calidades) 
    global formato_list
    formato_list = ttk.Combobox(frame1_botones, textvariable=formato, values=Lista_Formato, width=6)  # Modifica el ancho aquí
    formato_list.place(x=130, y=66)

    #Calidad
    Texto_calidad = tk.Label(frame1_botones, text="Calidad",fg=Variables.c_barras, bg=Variables.Y_backgroun, font=(Variables.poppins)) # por ejemplo, WPA2, WPA3
    Texto_calidad.place(x=230, y=64)
    Lista_calidades = ["1080p", "720p", "480p", "360p"]
    calidad = tk.StringVar()
    global calidades_list
    calidades_list = ttk.Combobox(frame1_botones, textvariable=calidad, values=Lista_calidades, width=6)  # Modifica el ancho aquí
    calidades_list.place(x=292, y=66)

    #Botones descargar
    Descargar_seleccion = Botones_Funciones.search_boton(Variables.D_seleccion, Variables.D_seleccion1, 100, 25, 420, 63) #logo youtube
    Descargar_seleccion.bind("<Button-1>", lambda event: Botones_Funciones.obtener_enlace_seleccionado())

    Descargar_todo = Botones_Funciones.search_boton(Variables.D_todo, Variables.D_todo1, 100, 25, 550, 63) #logo youtube
    Descargar_todo.bind("<Button-1>", lambda event: Botones_Funciones.descargar_todo())

    recicle_boton = Botones_Funciones.search_boton(Variables.recicle, Variables.recicle1, 20, 20, 665, 63)
    recicle_boton.bind("<Button-1>", lambda event: Botones_Funciones.clear(Variables.data_excel))

    global panel
    panel = Botones_Funciones.crear_treeview(frame2_treeview, Variables.data_excel)

    return frame

#############################
  #YOUTUBE BOTONES FUNCIONES
#############################
def B_y_buscar(): 
    Variables.entry_lik = entry.get()
    # Da la función al botón de la lupa para buscar
    if not Variables.entry_lik or Variables.entry_lik == "Introduce URL del video o playList": 
        Msg = "Campo de búsqueda vacío, formas de uso:\n\nMetodo #1:\nPara descargar videos o playList, pegue la URL y click en el boton lupa.\n\nMetodo #2:\nPara buscar algun video por nombre escriba el nombre, y click en Boton Youtube.\nuna ves encuentre el video copie la url del video deseado para descargar y repita el metodo #1"
        Alertas.alerta_Amarilla(Variables.titulo, "Error de campo", Msg)
    else:  # Si el Entry tiene algún texto
        titulos(Variables.entry_lik)

def titulos(entry_valor):
    # Muestra la lista de videos encontrados por el título si es una playlist o si es un solo video
    if 'playlist' in entry_valor:
        procesar_playlist(entry_valor)  # Pasamos el valor del Entry como argumento a la función procesar_playlist()
    else:
        procesar_video(entry_valor)  # Pasamos el valor del Entry como argumento a la función procesar_video()

def convertir_segundos_a_formato_tiempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return "{:02d}:{:02d}".format(minutos, segundos_restantes)

def procesar_playlist(entry_valor):
    # Crear objeto Playlist
    playlist = Playlist(entry_valor)
    # Lista para almacenar los títulos y duraciones de los videos encontrados
    videos_encontrados = []

    for video in playlist.videos:
        # Obtener el título del video
        titulo = video.title
        # link de cada video
        enlace = video.watch_url
        # Convertir la duración del video al formato "MM:SS"
        duracion_formato = convertir_segundos_a_formato_tiempo(video.length)
        # Agregar los datos del video a la lista de videos encontrados
        videos_encontrados.append([titulo, duracion_formato, Variables.Pendiente, enlace])

    Variables.cantidad = len(videos_encontrados)
    
    # Crear el block de notas con los títulos y duraciones de los videos
    Botones_Funciones.crear_excel_lista(videos_encontrados, Variables.data_excel)
    
    # Actualizar vista de treeview
    Botones_Funciones.actualizar_treeview(panel, Variables.data_excel)

    Msg = f"Se encontraron {Variables.cantidad} videos"
    Alertas.alerta_ok(Variables.titulo, "Proceso terminado", Msg)


def procesar_video(entry_valor):
    try:
        # Crear objeto YouTube para el video
        yt = YouTube(entry_valor)

        # Obtener el título del video
        titulo = yt.title
        # Obtener la duración del video en segundos
        duracion = yt.length
        # Convertir la duración del video al formato "MM:SS"
        duracion_formato = convertir_segundos_a_formato_tiempo(duracion)
        # Crear una lista con los datos del video
        video_info = [titulo, duracion_formato, Variables.Pendiente, entry_valor]

        # Crear el archivo Excel con los datos del video
        Botones_Funciones.crear_excel_video(video_info, Variables.data_excel)
        # Actualizar lista del treeview
        Botones_Funciones.actualizar_treeview(panel, Variables.data_excel)
        
        Msg = f"Se encontró 1 video"
        Alertas.alerta_ok(Variables.titulo, "Proceso terminado", Msg)
    except Exception as e:
        pass

def buscar_video():
    # Buscar un video enyotube por el nombre y no el link, dando click al boton segundario
    valor = entry.get()
    if valor:
        Botones_Funciones.abrir_link(valor)
    else:
        try:
            webbrowser.open(Variables.yotube_link)
        except Exception as e:
            pass
