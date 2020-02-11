import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cur = 0
        self.zeroLock = threading.Lock()
        self.evenLock = threading.Lock()
        self.oddLock = threading.Lock()
        self.evenLock.acquire()
        self.oddLock.acquire()


    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.zeroLock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.evenLock.release()
            else:
                self.oddLock.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.evenLock.acquire()
            printNumber(i)
            self.zeroLock.release()


    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.zeroLock.release()

class MyThread(threading.Thread):

    def __init__(self, obj, name):
        threading.Thread.__init__(self)
        self.obj = obj
        self.my_name = name

    def run(self):
        if self.my_name == 'z':
            self.obj.zero(self.print_number)
        elif self.my_name == 'o':
            self.obj.odd(self.print_number)
        elif self.my_name == 'e':
            self.obj.even(self.print_number)

    def print_number(self, x):
        print('print_number', self.my_name, x)


if __name__ == '__main__':
    obj = ZeroEvenOdd(20)
    a = MyThread(obj, 'z')
    b = MyThread(obj, 'o')
    c = MyThread(obj, 'e')

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()

    print('Done')
