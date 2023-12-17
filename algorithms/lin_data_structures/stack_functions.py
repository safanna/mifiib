"""
Pеализовать очередь с поддержкой максимума, минимума и суммы элементов, с использованием двух стеков.
Стек можете реализовать как с помощью встроенных в язык библиотек, так и написанных самостоятельно.
"""


class MyQueue:
    def __init__(self):
        self.minA = []
        self.minB = []
        self.maxA = []
        self.maxB = []
        self.stackA = []
        self.stackB = []
        self.sum = 0

    def isEmpty(self):
        return not (self.stackA and self.stackB)

    def push(self, v):
        self.sum += v
        if not self.stackA:
            self.stackA.append(v)
            self.minA.append(v)
            self.maxA.append(v)
        else:
            self.stackA.append(v)
            self.minA.append(min(self.minA[-1], v))
            self.maxA.append(max(self.maxA[-1], v))

    def pop(self):
        if self.stackB:
            self.sum -= self.stackB[-1]
            self.maxB.pop()
            self.minB.pop()
            return self.stackB.pop()
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

                self.minA.pop()
                self.maxA.pop()
                if self.minB:
                    self.minB.append(min(self.minB[-1], self.stackB[-1]))
                    self.maxB.append(max(self.maxB[-1], self.stackB[-1]))
                else:
                    self.minB.append(self.stackB[-1])
                    self.maxB.append(self.stackB[-1])
            if not self.stackB:
                return -1
            self.sum -= self.stackB[-1]

            self.maxB.pop()
            self.minB.pop()
            return self.stackB.pop()

    def min(self):
        if self.minA and self.minB:
            return min(self.minA[-1], self.minB[-1])
        elif self.minA:
            return self.minA[-1]
        elif self.minB:
            return self.minB[-1]

    def max(self):
        if self.maxA and self.maxB:
            return max(self.maxA[-1], self.maxB[-1])
        elif self.maxA:
            return self.maxA[-1]
        elif self.maxB:
            return self.maxB[-1]

    def sum(self):
        return self.sum


a = MyQueue()
a.push(4)
a.push(6)
a.push(9)
a.push(1)
a.push(3)
print(a.pop())
print(a.min())
print(a.max())
print(a.pop())
print(a.pop())
print(a.max())