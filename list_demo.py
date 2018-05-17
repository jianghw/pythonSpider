import os
from collections import deque


def list_method():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11]
    lst.index(2, 12)
    lst.append(13)
    lst.pop()
    lst.pop(2)
    lst.index(2)
    lst.count(6)
    lst.sort()
    lst.reverse()
    a = lst.copy()


def deque_list():
    queue = deque([1, 2, 3, 4, 5])
    queue.append(6)
    queue.append(7)
    queue.append(8)
    print(queue)


def range_list():
    a = []
    for x in range(10):
        a.append(x ** 2)
    print(x)
    print(a)
    b = list(map(lambda y: y ** 2, range(10)))
    print(b)
    c = [z ** 2 for z in range(10)]
    print(c)


def range_list_for():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    a = [[row[i] for row in matrix] for i in range(4)]
    print(a)
    b = []
    for i in range(4):
        b.append([row[i] for row in matrix])
    print(b)
    c = []
    for i in range(4):
        d = []
        for row in matrix:
            print('%s-->%s' % (i, row[i]))
            d.append(row[i])
        c.append(d)
    print(c)


def set_math():
    a = set('abcdef')
    b = set('abcxyz')
    c = a - b
    print(c)
    d = a | b
    print(d)
    e = a & b
    print(e)
    f = a ^ b
    print(f)


def dict_new():
    d = {'abc': 123, 'defg': 456}
    print(d)
    c = dict(abc=123, defg=456)
    print(c)
    e = dict([('abc', 123), ('efg', 456)])
    print(e)


class LocalGlobal:
    def do_local(self):
        a = 'local'

    def do_nonlocal(self):
        # nonlocal a
        a = 'nonlocal'

    def do_global(self):
        global a
        a = 'global'

    a = 'test'


class B(Exception):
    def __init__(self):
        self.txt = 'b'

    pass


class C(B):
    def __init__(self):
        self.txt = 'c'

    pass


class D(C):
    def __init__(self):
        self.txt = 'd'

    pass


def extend_class():
    for cls in [B, C, D]:
        try:
            raise cls()
        except D as d:
            print(d.txt)
        except C as c:
            print(c.txt)
        except B as b:
            print(b.txt)


def process_id():
    print('process id is {}'.format(os.getpid()))
    pid = os.fork()
    if pid == 0:
        print('{}-->{}'.format(os.getpid(), os.getppid()))
    else:
        print('{}->{}'.format(os.getpid(), pid))


list_a = []


def deco(func):
    print('run deco is {}'.format(func))
    list_a.append(func)
    return func


@deco
def f1():
    print('f1')


@deco
def f2():
    print('f2')


def f3():
    print('f3')


def decorators_demo():
    print('main')
    print('list', list_a)
    f1()
    f2()
    f3()


def get_averager():
    list_num = []
    count_num = 2

    def averager(value):
        list_num.append(value)
        nonlocal count_num
        count_num += value
        total = sum(list_num)
        return total / len(list_num), count_num

    return averager


if __name__ == '__main__':
    av = get_averager()
    print(type(av))
    print(av(10))
    print(av(20))
    print(av(30))
    print(av(40))
    print(av.__code__.co_freevars)
