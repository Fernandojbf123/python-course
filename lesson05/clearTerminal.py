import os
import platform

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Comando para Windows
    else:
        os.system("clear")  # Comando para Linux/MacOS