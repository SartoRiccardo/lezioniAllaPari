# Import
from tkinter import *
from login import Login
from user import User

# Variabili
boolD = True

# Funzioni


if __name__ == '__main__':
    if boolD:
        print("Inizio Programma\n")

    root = Tk()
    root.title("Lezioni alla Pari")
    root.geometry("800x500")
    root.minsize(800, 500)
    #root.resizable(width="False", height="False")
    root.grab_set()  # Blocca root (non funziona, ma lo lascio)
    root.withdraw()  # Nascondi finestra fino al login

    user = User()

    login = Login(root, user)  # Apri login

    Label(root, text="Nome: " + user.getName()).pack()
    Label(root, text="Cognome: " + user.getSurname()).pack()
    Label(root, text="Username: " + user.getUsername()).pack()




    root.mainloop()

    if boolD:
        print("\nFine Programma")
