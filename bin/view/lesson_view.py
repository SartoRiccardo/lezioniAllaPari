from tkinter import *
from tkinterhtml import HtmlFrame

class LessonView:
    def __init__(self, root, title, content):
        self.__root = root
        self.__title = title
        self.__content = content

        self.__view = Toplevel(self.__root)
        self.__view.title(self.__title)
        self.__view.geometry("700x600")
        self.__view.minsize(width=500, height=500)

        self.__web = HtmlFrame(self.__view, horizontal_scrollbar="auto")
        self.__web.set_content(self.__content)
        self.__web.pack(expand=1, fill=BOTH)

        self.__view.mainloop()
