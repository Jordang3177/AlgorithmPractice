class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            printFoo()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printBar()