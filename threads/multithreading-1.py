import threading
import time


def print_current_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s %s" % (threadName, time.ctime(time.time())))
        print(threading.current_thread().name)


try:
    t1 = threading.Thread(target=print_current_time, args=("Thread-1", 1))
    t2 = threading.Thread(target=print_current_time, args=("Thread-2", 2))

    t1.name = "John Doe"
    t1.start()
    t2.name = "Kim Jones"
    t2.start()
except:
    print("Error: unable to start threads")

print(threading.active_count())
print(threading.enumerate())





