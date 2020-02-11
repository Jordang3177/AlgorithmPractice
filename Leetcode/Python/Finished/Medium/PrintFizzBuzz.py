import threading

class FizzBuzz(object):
    def __init__(self, n: int):
        self.n = n
        self.finished = False
        self.fizzlock = threading.Semaphore(0)
        self.buzzlock = threading.Semaphore(0)
        self.fizzbuzzlock = threading.Semaphore(0)
        self.numberlock = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(3, self.n + 1, 3):
            self.fizzlock.acquire()
            if self.finished:
                return
            printFizz()
            self.numberlock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(5, self.n + 1, 5):
            self.buzzlock.acquire()
            if self.finished:
                return
            printBuzz()
            self.numberlock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.fizzbuzzlock.acquire()
            if self.finished:
                return
            printFizzBuzz()
            self.numberlock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.numberlock.acquire()
            if i % 5 == 0 and i % 3 == 0:
                self.fizzbuzzlock.release()
            elif i % 5 == 0:
                self.buzzlock.release()
            elif i % 3 == 0:
                self.fizzlock.release()
            else:
                printNumber(i)
                self.numberlock.release()
        self.numberlock.acquire()
        self.finished = True
        self.fizzlock.release()
        self.buzzlock.release()
        self.fizzbuzzlock.release()


class MyThread(threading.Thread):

    def __init__(self, obj, name):
        threading.Thread.__init__(self)
        self.obj = obj
        self.my_name = name

    def run(self):
        if self.my_name == 'fz':
            self.obj.fizz(self.print_fizz)
        elif self.my_name == 'bz':
            self.obj.buzz(self.print_buzz)
        elif self.my_name == 'fzbz':
            self.obj.fizzbuzz(self.print_fizzbuzz)
        elif self.my_name == 'n':
            self.obj.number(self.print_number)

    def print_number(self, x):
        print(x)
    def print_fizz(self):
        print("Fizz")
    def print_buzz(self):
        print("Buzz")
    def print_fizzbuzz(self):
        print("FizzBuzz")


if __name__ == '__main__':
    obj = FizzBuzz(30)
    a = MyThread(obj, 'fz')
    b = MyThread(obj, 'bz')
    c = MyThread(obj, 'fzbz')
    d = MyThread(obj, 'n')

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print('Done')