import threading


# Multithreading private data
mydata = threading.local()


def private_cube(number):
    mydata.x = number
    print(threading.currentThread().getName() + ' said: cube of the number {} is {}'.format(mydata.x, mydata.x ** 3))


numbers = range(1, 4)
threads = []

for number in numbers:
    thr = threading.Thread(target=private_cube, args=(number,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()