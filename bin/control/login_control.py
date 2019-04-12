from objects.user import User
from view.login_view import LoginView
from exceptions import EmptyFieldException
from control.io_manager import login


class LoginControl:
    def __init__(self, root):
        self.__view = LoginView(root, self)
        self.__loggedUser = None

        self.__view.mainloop()

    def login(self, user: str, password: str):
        """
        Guarda se le credenziali sono corrette
        :param user: l'username dell'utente
        :param password: la password dell'utente
        :return: un oggetto User, None se i dati inseriti non sono validi
        """
        if user == "":
            raise EmptyFieldException("Username should not be an empty string")
        if password == "":
            raise EmptyFieldException("Password should not be an empty string")

        return login(user, password)

    def logInAs(self, user: User):
        """
        Effettua la procedura di login
        :param user: l'utente loggato
        """
        if not isinstance(user, User):
            raise TypeError("Expected user, got {} instead".format(type(user).__name__))
        self.__loggedUser = user
        self.__view.quit()

    def getLoggedUser(self):
        return self.__loggedUser

    def setLoggedUser(self, user: User):
        if not isinstance(user, User):
            raise TypeError("Expected User, got {} instead".format(type(user).__name__))
        self.__loggedUser = user
