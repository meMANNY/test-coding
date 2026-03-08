import threading 

import time

def worker():

    print(f"{threading.current_thread().name} is starting")
    count = 0
    for _ in range(10000000):
        count += 1
    print(f"{threading.current_thread().name} is done")

thread1 = threading.Thread(target=worker, name="Thread-1")
thread2 = threading.Thread(target=worker, name="Thread-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()
print(f"total time: { end - start:.2f} seconds")

