import threading
import time


def func1(sec):
    time.sleep(sec)
    print(sec)


def func2():
    time.sleep(3)
    print(2)


def func3():
    time.sleep(2)
    print(3)


task1 = threading.Thread(target=func1, args=(1,))
task1.start()

task2 = threading.Thread(target=func2)
task2.start()

task3 = threading.Thread(target=func3)
task3.start()

task1.join()
task2.join()
task3.join()

print("done")
