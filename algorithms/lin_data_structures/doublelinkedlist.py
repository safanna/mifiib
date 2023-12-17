"""
реализовать двусвязный список, хранящий значения типа int.
Требуется поддержать операции get, set, pushFront (вставка в начало листа),
pushBack (вставка в конец), popFront (удаление с начала), popBack (удаление с конца),
front (элемент в начале), back (элемент в конце).
"""


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class dlList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_head = Node(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

        if not self.tail:
            self.tail = new_head

    def push_back(self, data):
        new_tail = Node(data=data, prev=self.tail)
        if self.tail:
            self.tail.next = new_tail
        self.tail = new_tail

        if not self.head:
            self.head = new_tail

    def pop_back(self):
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    def pop_front(self):
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def back(self):
        return self.head.data

    def front(self):
        return self.tail.data

    def get(self, idx):
        tmp = self.head
        for i in range(idx):
            if tmp != None:
                tmp = tmp.next

        if tmp != None:
            return tmp.data
        else:
            return -1

    def set(self, idx, val):
        tmp = self.head
        for i in range(0..idx):
            print(i)
            if tmp != None:
                tmp = tmp.next
        if tmp != None:
            tmp.data = val
