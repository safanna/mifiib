"""
Реализовать очередь с помощью двух стеков.
Доказать амортизированную оценку работы queue, реализованную с помощью двух стеков:
Все операции, кроме случая, когда требуется переносить данные из одного стека в другой,
выполняются за то же время что и в стеке, то есть за .
Для оценивания времени, которое тратим на перенос, воспользуемся методом монеток.
Каждый раз при добавлении элемента будем класть на него монетку и тратить её,
когда этот элемент требуется перенести во второй стек.
Таким образом, амортизированная оценка метода pop остается.
"""


class Queue(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def push(self,element):
        self.instack.append(element)

    def pop(self):
        if self.isEmpty():
            return -1
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def is_empty(self):
    	return not (self.instack or self.outstack)

