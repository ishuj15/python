import time
from multiprocessing import Process
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
start = time.time()
ask_user()
complex_cal()
print(f'Single thread total time{time.time() - start}')

# Multi process
process=Process(target=complex_cal)

if __name__ == "__main__":
    process.start()
    start = time.time()

    ask_user()
    process.join()


print(f'Two process:{time.time() - start}')