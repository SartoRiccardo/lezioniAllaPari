from tkinter import *
from tkinter import messagebox
from exceptions import EmptyFieldException


class LoginView:
    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__login = Toplevel(self.__root)
        self.__login.grab_set()  # Blocca root
        self.__login.title("Login")
        self.__login.geometry("300x250")
        self.__login.resizable(width="False", height="False")
        self.__login.protocol("WM_DELETE_WINDOW", self.closeAll)  # Controllo su chiusura della finestra

        self.__login.bind("<Return>", self.__checkLogin)  # Premuto tasto "Invio", controlla login

        # Username
        Label(self.__login, text="Esegui il login\n").pack()
        Label(self.__login, text="Username").pack()
        self.__username = Entry(self.__login, justify='center')
        self.__username.focus()
        self.__username.pack()

        # Password
        Label(self.__login, text="\nPassword").pack()
        self.__password = Entry(self.__login, show='•', justify='center')
        self.__password.pack()

        # Login
        Label(self.__login, text="").pack()
        Button(self.__login, text="Login", width=10, height=1, command=self.__checkLogin).pack()

    def __checkLogin(self, event=None):
        """
        Controlla login inserito
        :param event: Evento (lasciare)
        """
        user = self.__username.get().lower()
        password = self.__password.get()

        try:
            userLogged = self.__control.login(user, password)
            self.__control.logInAs(userLogged)

        except (EmptyFieldException, TypeError) as err:
            if isinstance(err, EmptyFieldException):
                messagebox.showinfo("Errore", "Riempire tutti i campi")
            elif isinstance(err, TypeError):
                messagebox.showinfo("Errore", "Credenziali errate")

    def mainloop(self):
        self.__login.mainloop()

    def quit(self):
        self.__root.deiconify()  # Mostra root

        self.__login.grab_release()  # Sblocca root
        self.__login.quit()  # Tornare in esecuzione root
        self.__login.destroy()  # Chiudi finestra

    def closeAll(self):
        sys.exit(0)
