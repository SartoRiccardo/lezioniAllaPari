from tkinter import *
from tkinter import messagebox

class Login():
    def __init__(self, root):
        self.__file = "config/login.csv"

        self.__root = root

        self.__login = Toplevel(root)
        self.__login.title("Login")
        self.__login.geometry("300x250")
        self.__login.resizable(width="False", height="False")
        self.__login.protocol("WM_DELETE_WINDOW", self.closeAll)  # Controllo su chiusura della finestra

        Label(self.__login, text="Esegui il login").pack()
        Label(self.__login, text="").pack()
        Label(self.__login, text="Username").pack()

        self.__user = Entry(self.__login, justify='center')
        self.__user.pack()

        Label(self.__login, text="").pack()
        Label(self.__login, text="Password").pack()

        self.__password = Entry(self.__login, show='-', justify='center')
        self.__password.pack()

        Label(self.__login, text="").pack()
        Button(self.__login, text="Login", width=10, height=1, command=self.checkLogin).pack()

        self.__login.mainloop()

    def checkLogin(self):
        user = self.__user.get()
        password = self.__password.get()

        if(user == "" or password == ""):
            messagebox.showinfo("Errore", "Riempire tutti i campi")
        else:
            file = open(self.__file, "r")
            for line in file:
                line = line.replace("\n","")
                line = line.split(";")
                if(str(line[3]) == str(user) and str(line[4]) == str(password)):
                    self.__root.deiconify()  # Mostra root
                    self.__login.destroy()  # Distruggi finestra
                    breakf
            messagebox.showinfo("Errore", "Username o Password errati")

    def closeAll(self):
        self.__root.destroy()
