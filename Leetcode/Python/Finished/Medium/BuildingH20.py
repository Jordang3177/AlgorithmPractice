import threading

class H2O:
    def __init__(self):
        self.h1lock = threading.Lock()
        self.h2lock = threading.Lock()
        self.olock = threading.Lock()
        self.olock.acquire()
        self.h2lock.acquire()
        self.hfound = False


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        if not self.hfound:
            self.h1lock.acquire()
        else:
            self.h2lock.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hfound = not self.hfound
        if self.hfound:
            self.h2lock.release()
        else:
            self.olock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.olock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h1lock.release()