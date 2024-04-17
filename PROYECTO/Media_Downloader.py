import tkinter as tk

import Home_Funciones
import Variables

if __name__ == "__main__":
    try:
        Home_Funciones.screen_holding()
        Home_Funciones.crear_windows_principal()
    except Exception as e:
        print(f"Error {e}")
