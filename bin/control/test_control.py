from view.test_view import TestView


class TestControl:
    def __init__(self, root, testId, userId):
        self.__testId = testId
        self.__userId = userId

        tv = TestView(root, self.__testId, self)
