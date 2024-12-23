import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"time: {time.time() - self.start_time:.1f}")

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        print(f"time: {time.time() - start_time:.1f}")

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1.5)

    with cm_timer_2():
        time.sleep(2.5)