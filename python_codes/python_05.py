from multiprocessing import Process

import time

def worker(num):
    print(f"Worker {num} is starting")
    time.sleep(2)
    print(f"Worker {num} is done")


if __name__ == "__main__":
    workers = [Process(target=worker,args = (f" {i+1}",)) for i in range(4)]


    for p in workers:
        p.start()

    for p in workers:
        p.join()

    print("All workers are done")
    print("Main process is done")