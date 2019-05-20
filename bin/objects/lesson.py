from objects.element import Element


class Lesson(Element):
    def __init__(self, id, title, start, end, owner, *classrooms):
        super(Lesson, self).__init__(id, title, start, end, owner)

        for c in classrooms:
            self.addClass(c)
