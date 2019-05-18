from tkinter import Listbox, Scrollbar, RIGHT, SINGLE, END, Y


class List:
    def __init__(self, root, array=[]):
        self.__root = root

        self.__scrollBar = Scrollbar(self.__root)
        self.__scrollBar.pack(side=RIGHT, fill=Y)

        self.__list = Listbox(self.__root, selectmode=SINGLE, yscrollcommand=self.__scrollBar.set)
        self.__list.config(width=40)
        self.__list.pack()

        self.__lessons = []
        self.setList(array)

        self.__scrollBar.config(command=self.__list.yview)

    def getObjectList(self):
        return self.__list

    def setList(self, array=[]):
        self.__deleteAll()

        self.__lessons = [x for x in array]
        for item in array:
            self.__list.insert(END, str(item))

    def getSelectedElement(self, e=None):
        if self.__list.curselection() is ():
            return None
        else:
            return self.__lessons[self.__list.curselection()[0]]

    def setSelectedItem(self, i):
        self.__list.activate(i)

    def __deleteAll(self):
        self.__list.delete(0, END)
