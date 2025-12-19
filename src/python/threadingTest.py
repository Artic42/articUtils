import threading
import time


def func1():
    for i in range(5):
        print(f"Function 1 runned {i} times")
        time.sleep(5)


def func2():
    for i in range(10):
        print(f"Function 2 runned {i} times")
        time.sleep(1)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All done")
