import time
from threading import  Thread
def ask_user():
    start=time.time()
    user_input=input("Enter your name")
    greet=f'Hello, {user_input}'
    print(greet)
    print(f'ask user{time.time() -start}')

def complex_cal():
    start = time.time()
    print("started calculating")
    [x**2 for x in range(20000000)]
    print(f' complex cal{time.time() - start}')

# Single threading
start = time.time()
ask_user()
complex_cal()
print(f'Single thread total time{time.time() - start}')
# Multi threading
thread1= Thread(target=complex_cal)
thread2=Thread(target=ask_user)

start = time.time()
# Instead of creating threads manually u can usk thread pool
# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=2) as pool :
#     pool.submit(complex_cal)
#     pool.submit(ask_user)
#

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two thread total time{time.time() - start}')