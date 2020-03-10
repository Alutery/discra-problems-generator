#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Тестовое задание 11.
Решите задание, введите ответ в виде числа с клавиатуры.
Имеется две колоды из 6 карт каждая. Карты, содержащиеся в каждой колоде, одинаковые. 
В первой колоде фиксирован порядок карт. 
Количество способов, которыми можно уложить карты во второй колоде таким образом, 
чтобы при одновременном открывании верхних карт обеих колод, получилось ровно 4 совпадения, равно ____.
'''
import sys
from math import factorial
import argparse

# required: sudo pip3 install python-docx 
from docx import Document


def D(k):
    tmp = 0
    for i in range(k+1):
        tmp += (-1) ** i * factorial(k) / factorial(i)
    return tmp

# сочетаниями из n объектов по k
def C(k, n):
    return factorial(n) // factorial(n-k) // factorial(k)


class Generator:

    def __init__(self):
        self.doc = None
        self.min_n = None
        self.max_n = None

    # для обработки аргументов командной строки
    def createParser (self):
        parser = argparse.ArgumentParser()
        parser.add_argument ('--min', nargs='?', default=0, type=int, help='Минимальный возможный ответ (по умолчанию 0)')
        parser.add_argument ('--max', nargs='?', default=25000000, type=int, help='Максимальный возможный ответ (по умолчанию 25000000)')
        parser.add_argument ('-f', '--file', default='moduleTest_11', help='Наименование файла документа docx (! без .docx, по умолчанию moduleTest_11)')
    
        return parser

    # проверка принадлежности ответа заданному диапазону
    def check(self, n):
        return True if (n <= self.max_n and n >= self.min_n) else False

    # получть задания по заданному количеству карт
    def get_tasks(self, n, k):
        text = f'Имеется две колоды из {n} карт каждая. Карты, содержащиеся в каждой колоде, одинаковые. В \
    первой колоде фиксирован порядок карт. Количество способов, которыми можно уложить карты во второй колоде \
    таким образом, чтобы при одновременном открывании верхних карт обеих колод, получилось ровно {k} совпадения, равно ____.\n\n'

        culc = f'C({k}, {n}) * D({n-k})'
        text += culc + '\n\nAnswer: '
        answer = eval(f'C({k}, {n})') * D(n - k)
        if not self.check(answer):
            return None
        text += str(int(answer))

        return text + '\n'

    def generate_tasks(self):
        count = 1
        for i in range(6, 11):
            for j in range(1, 5):
                task = self.get_tasks(i, j)
                if task:
                    self.doc.add_paragraph(str(count) + '. ' + task)
                    count+=1
            
    def generate(self):
        parser = self.createParser()
        namespace = parser.parse_args(sys.argv[1:])

        self.min_n = namespace.min
        self.max_n = namespace.max

        self.doc = Document()
        self.generate_tasks()
        self.doc.save(namespace.file + '.docx')


if __name__ == '__main__':
    Generator().generate()