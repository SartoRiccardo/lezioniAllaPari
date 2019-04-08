from tkinter import messagebox, sys
from login_view import LoginView


class LoginControl:
    __CREDENTIALS = "config/login.csv"

    def __init__(self, root, user):
        self.__root = root
        self.__user = user

        self.__view = LoginView(self.__root)
        self.__view.getView().protocol("WM_DELETE_WINDOW", self.closeAll)  # Controllo su chiusura della finestra

        self.__view.getView().bind("<Return>", self.__login)  # Premuto tasto "Invio", controlla login
        self.__view.getLoginButton().config(command=self.__login)

        self.__view.getView().mainloop()

    def __login(self, event=""):
        """
        Guarda se le credenziali sono corrette
        :param user: Username
        :param password: Password
        :return: un oggetto User, None se i dati inseriti non sono validi
        """
        user = self.__view.getUsername()
        password = self.__view.getPassword()

        if user == "" or password == "":
            messagebox.showinfo("Errore", "Riempire tutti i campi")
        else:
            file = open(LoginControl.__CREDENTIALS, "r")
            file.readline()
            for line in file:
                line = line.replace("\n", "").split(";")
                if str(line[3]).lower() == str(user) and str(line[4]) == str(password):

                    self.__user.setName(line[1])  # Nome
                    self.__user.setSurname(line[2])  # Cognome
                    self.__user.setUsername(line[3])  # Username
                    self.__user.setState(line[0])  # Stato
                    for classroom in line[5:]:
                        self.__user.addClass(classroom)

                    self.__close()
                    return
            messagebox.showinfo("Errore", "Username o Password errati")

    def __close(self):
        self.__view.getView().quit()  # Importante per far tornare in esecuzione root
        self.__view.getView().destroy()  # Chiudi finestra

        self.__root.grab_release()  # Sblocca root (non funziona, ma lo lascio)
        self.__root.deiconify()  # Mostra root

    def closeAll(self):
        sys.exit(0)
