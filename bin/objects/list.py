from tkinter import Listbox, END, SINGLE


class List:
    def __init__(self, root, array=[]):
        self.__root = root

        self.__list = Listbox(self.__root, selectmode=SINGLE)
        self.__list.config(width=40)
        self.__list.pack()

        self.__lessons = [x for x in array]
        for item in array:
            self.__list.insert(END, str(item))

    def getList(self):
        return self.__list

    def getSelectedElement(self, e=None):
        if self.__list.curselection() is ():
            return None
        else:
            return self.__lessons[self.__list.curselection()[0]]

    def setSelectedItem(self, i):
        self.__list.activate(i)

    def delete(self, i):
        if 0 <= i < len(self.__lessons):
            self.__list.delete(i)
            self.__lessons.pop(i)

    def add(self, lesson, i=None):
        if i is None:
            i = len(self.__lessons)
        self.__list.insert(i, str(lesson))
        self.__lessons.insert(i, lesson)
