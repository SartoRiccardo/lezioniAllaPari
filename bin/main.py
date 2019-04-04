# Import
from tkinter import *
from login import Login
from user import User
from view import View

# Variabili
boolD = True

# Funzioni
def close():
    sys.exit(0)

if __name__ == '__main__':
    if boolD:
        print("Inizio Programma\n")

    root = Tk()
    root.title("Lezioni alla Pari")
    root.geometry("800x500")
    root.minsize(800, 500)
    #root.resizable(width="False", height="False")
    root.protocol("WM_DELETE_WINDOW", close)  # Controllo su chiusura della finestra

    root.grab_set()  # Blocca root (non funziona, ma lo lascio)
    root.withdraw()  # Nascondi finestra fino al login

    user = User()

    login = Login(root, user)  # Apri login

    view = View(root, user)  # GUI

    # ...

    root.mainloop()

    if boolD:
        print("\nFine Programma")
