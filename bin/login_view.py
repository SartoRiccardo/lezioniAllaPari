from tkinter import Toplevel, Label, Entry, Button


class LoginView:
    def __init__(self, root):
        self.__root = root
        #self.__control = control

        self.__login = Toplevel(self.__root)
        self.__login.title("Login")
        self.__login.geometry("300x250")
        self.__login.resizable(width="False", height="False")

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
        self.__loginBtn = Button(self.__login, text="Login", width=10, height=1)
        self.__loginBtn.pack()

    def getView(self):
        return self.__login

    def getLoginButton(self):
        return self.__loginBtn

    def getUsername(self):
        return self.__username.get().lower()

    def getPassword(self):
        return self.__password.get()
