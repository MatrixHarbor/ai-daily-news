import threading

class Fork:
    def __init__(self):
        # add a lock
        self.lock = threading.Lock()

    def acquire_fork(self):
        # true if acquire self.lock
        return self.lock.acquire(blocking=False)

    def release_fork(self):
        # release lock
        self.lock.release()