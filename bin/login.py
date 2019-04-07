from tkinter import *
from tkinter import messagebox

class Login():
    def __init__(self, root, user):
        self.__file = "config/login.csv"

        self.__root = root
        self.__user = user

        self.__login = Toplevel(self.__root)
        self.__login.title("Login")
        self.__login.geometry("300x250")
        self.__login.resizable(width="False", height="False")
        self.__login.protocol("WM_DELETE_WINDOW", self.closeAll)  # Controllo su chiusura della finestra

        self.__login.bind("<Return>", self.__checkLogin)  # Premuto tasto "Invio", controlla login

        # Username
        Label(self.__login, text="Esegui il login\n").pack()
        Label(self.__login, text="Username").pack()
        self.__username = Entry(self.__login, justify='center')
        self.__username.pack()

        # Password
        Label(self.__login, text="\nPassword").pack()
        self.__password = Entry(self.__login, show='•', justify='center')
        self.__password.pack()

        Label(self.__login, text="").pack()
        Button(self.__login, text="Login", width=10, height=1, command=self.__checkLogin).pack()

        self.__login.mainloop()

    def __checkLogin(self, event=""):
        '''
        Controlla login inserito
        :param event: Evento (lasciare)
        :return: Boolean
        '''
        user = self.__username.get().lower()
        password = self.__password.get()

        if(user == "" or password == ""):
            messagebox.showinfo("Errore", "Riempire tutti i campi")
        else:
            file = open(self.__file, "r")
            file.readline()
            for line in file:
                line = line.replace("\n","")
                line = line.split(";")
                if(str(line[3]).lower() == str(user) and str(line[4]) == str(password)):
                    self.__user.setName(line[1])  # Nome
                    self.__user.setSurname(line[2])  # Cognome
                    self.__user.setUsername(line[3])  # Username
                    self.__user.setState(line[0])  # Username
                    for classe in line[5:]:  # Classi
                        self.__user.addClass(classe)

                    self.__login.quit()  # Importante per far tornare in esecuzione root
                    self.__login.destroy()  # Chiudi finestra

                    self.__root.grab_release()  # Sblocca root (non funziona, ma lo lascio)
                    self.__root.deiconify()  # Mostra root
                    return True
            messagebox.showinfo("Errore", "Username o Password errati")

    def closeAll(self):
        sys.exit(0)
