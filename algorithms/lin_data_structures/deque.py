"""
Написать дек для целых чисел c использованием двусвязного списка.
"""


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.insert(0,item)

    def pop_back(self):
        return self.items.pop()

    def pop_front(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)