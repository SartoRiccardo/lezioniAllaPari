from objects.element import Element
from copy import deepcopy

class Lesson(Element):
    def __init__(self, id, title, start, end, owner, *classrooms):
        super(Lesson, self).__init__(id, title, start, end, owner)

        for c in classrooms:
            self.addClass(c)

    def __str__(self):
        return "{} - Scadenza: {}".format(super().getTitle(), super().getEnd())
