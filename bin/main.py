# Import
from tkinter import *
from login import Login

# Variabili
boolD = True

# Funzioni


if __name__ == '__main__':
    if boolD:
        print("Inizio Programma\n")

    root = Tk()
    root.title("Lezioni alla Pari")
    root.geometry("900x600")
    root.resizable(width="False", height="False")
    root.withdraw()  # Nascondi finestra fino al login

    login = Login(root)  # Apri login

    # something

    root.mainloop()

    if boolD:
        print("\nFine Programma")
