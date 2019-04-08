from tkinter import *
from tkinter import messagebox
from exceptions import EmptyFieldException


class LoginView:
    def __init__(self, root, control):
        self.__root = root
        self.__control = control

        self.__root.grab_set()  # Blocca root
        self.__root.withdraw()  # Nascondi finestra fino al login

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

    def __checkLogin(self, event=None):
        """
        Controlla login inserito
        :param event: Evento (lasciare)
        :return: Boolean
        """
        user = self.__username.get().lower()
        password = self.__password.get()

        try:
            usr = self.__control.login(user, password)

            if usr is None:
                messagebox.showinfo("Errore", "Credenziali sbagliate")
            else:
                self.__control.logInAs(usr)

        except EmptyFieldException:
            messagebox.showinfo("Errore", "Riempire tutti i campi")

    def mainloop(self):
        self.__root.mainloop()

    def quit(self):
        self.__root.grab_release()  # Sblocca root
        self.__root.deiconify()  # Mostra root

        self.__login.quit()  # Importante per far tornare in esecuzione root
        self.__login.destroy()  # Chiudi finestra

    def closeAll(self):
        sys.exit(0)
