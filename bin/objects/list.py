from tkinter import Frame, Listbox, Scrollbar, SINGLE, BOTH, LEFT, RIGHT, W, Y, END


class List:
    def __init__(self, root, array=[]):
        self.__root = root

        self.__frame = Frame(self.__root)

        self.__scrollBar = Scrollbar(self.__frame)

        self.__list = Listbox(self.__frame, font=18, selectmode=SINGLE, width=10, yscrollcommand=self.__scrollBar.set)
        self.__list.config(width=40)
        self.__list.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)

        self.__lessons = []
        self.setList(array)

        self.__scrollBar.config(command=self.__list.yview)
        self.__scrollBar.pack(side=RIGHT, fill=Y)

        self.__frame.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)

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
