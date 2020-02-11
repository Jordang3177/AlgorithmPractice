import threading

class Foo(object):

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()

        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def first(self, printFirst):

        printFirst()
        self.lock1.release()

    def second(self, printSecond):

        self.lock1.acquire()

        printSecond()
        self.lock2.release()

    def third(self, printThird):

        self.lock2.acquire()

        printThird()