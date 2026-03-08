import threading
import time

def worker():
    for i in range(1,4):
        print(f"Worker {i} is starting")
        time.sleep(2)
        print(f"Worker {i} is done")

def master():
    for i in range(1,4):
        print(f"Master {i} is starting")
        time.sleep(1)
        print(f"Master {i} is done")
        


t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=master)

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads are done")
print("Main thread is done")