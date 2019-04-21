class Stack():
    def __init__(self):
        self.__storage = []
        self.__head = -1

    def push(self, item):
        self.__storage.append(item)
        self.__head += 1

    def pop(self):
        a = self.__storage[self.__head]
        self.__storage.pop()
        self.__head -= 1
        return a

    def is_empty(self):
        return self.__head <= - 1