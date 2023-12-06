import time
import logging
import download_websites
import concurrent.futures

"""
Race conditions occur when multiple threads happens to access a shared resource (data) at the same time.
To prevent race conditions, we can use a lock to ensure that only one thread can access the resource at a time.
"""

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_value = self.value
        local_value += 1
        time.sleep(0.1)
        self.value = local_value
        logging.info("Thread %s: finishing update", name)

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock [DEBUG]", name)
        with self._lock:
            # self.acquire()
            # inside this 'with' the thread (self) acquires the lock at the starting by calling .acquire()
            logging.debug("Thread %s has lock [DEBUG]", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock [DEBUG]", name)
            # inside this 'with' the thread (self) releases the lock at the ending by calling .release()
            # self.release()
        logging.debug("Thread %s after release [DEBUG]", name)
        logging.info("Thread %s: finishing update", name)
            
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    print("Simple update:")
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
    
    
    logging.getLogger().setLevel(logging.DEBUG)
    print("\nLocked update:")
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
    
    
    
