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


if __name__ == '__main__':
    for cls in [B, C, D]:
        try:
            raise cls()
        except D as d:
            print(d.txt)
        except C as c:
            print(c.txt)
        except B as b:
            print(b.txt)
