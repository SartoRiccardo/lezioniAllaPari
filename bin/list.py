from tkinter import Listbox, END, EXTENDED, BOTH

class List():
    def __init__(self, root, list="", test=""):
        self.__root = root

        self.__list = Listbox(self.__root, selectmode=EXTENDED)
        self.__list.config(width=40)
        self.__list.pack(fill=BOTH, expand=1)

        for item in list:
            self.__list.insert(END, str(item))
