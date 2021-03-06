from tkinter import Toplevel, BOTH
from tk_html_widgets import HTMLLabel


class LessonView:
    """ Deprecated """
    def __init__(self, root, title, content):
        self.__root = root
        self.__title = title
        self.__content = content

        self.__view = Toplevel(self.__root)
        self.__view.title(self.__title)
        self.__view.geometry("700x600")
        self.__view.minsize(width=400, height=400)

        self.__html = HTMLLabel(self.__view, html=self.__content)
        self.__html.pack(fill=BOTH, expand=True, padx=20, pady=10)

        self.__view.mainloop()
