# multi threaded
import time
from download_websites import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//4,))
t2 = Thread(target=countdown, args=(COUNT//4,))
t3 = Thread(target=countdown, args=(COUNT//4,))
t4 = Thread(target=countdown, args=(COUNT//4,))

start = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end = time.time()

print('Time taken in seconds -', end - start)
