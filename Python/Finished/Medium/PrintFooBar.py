import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = threading.Lock()
        self.barlock = threading.Lock()
        self.foolock.acquire()

    def foo(self, printFoo):
        for i in range(self.n):
            self.barlock.acquire()
            printFoo()
            self.foolock.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.foolock.acquire()
            printBar()
            self.barlock.release()