import download_websites

l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire\nNow, stuck because the lock is already acquired (not released yet))")
l.acquire()
print("acquired lock twice")

# To avoid deadlocks, never acquire more than one lock at a time, or you can use a RLocl (reentrant lock) instead of a Lock (non-reentrant lock)