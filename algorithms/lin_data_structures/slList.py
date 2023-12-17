"""
Односвязный список
"""


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next


class slList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        self.head = Node(data=data, next=self.head)

    def push_back(self, data):
        tmp = self.head
        prev = None
        while tmp is not None:
            prev = tmp
            tmp = tmp.next
        if prev is not None:
            prev.next = Node(data=data, next=None)
        else:
            self.head = Node(data=data, next=None)

    def pop_back(self):
        if self.head is not None:
            tmp = self.head
            prev = None
            while tmp is not None and tmp.next is not None:
                prev = tmp
                tmp = tmp.next
            if prev is not None:
                prev.next = None
            else:
                head = None

    def pop_front(self):
        if self.head is not None:
            self.head = self.head.next

    def push_after(self, pos, x):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None:
            tmp.next = Node(data=x, next=tmp.next)

    def pop_after(self, pos):
        tmp = self.head
        for i in range(pos):
            if tmp is not None:
                tmp = tmp.next

        if tmp is not None and tmp.next is not None:
            tmp.next = tmp.next.next
