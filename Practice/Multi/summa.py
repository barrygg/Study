import threading


# Working with threading
def sum(*args):
    number = 0
    string = str()
    array = list()

    for arg in args:
        if type(arg) is int:
            number += arg
        elif type(arg) is str:
            string += arg
        elif type(arg) is list:
            array += arg
    if number != 0:
        print(threading.currentThread().getName() + ' said: Sum is {}'.format(number))
    if string != str():
        print(threading.currentThread().getName() + ' said: Sum is {}'.format(string))
    if array != list():
        print(threading.currentThread().getName() + ' said: Sum is {}'.format(array))

numbers = 1, 2, 3, 4
strings = 'one', 'two', 'three', 'four'
arrays = [1, 2], [3, 4]

threads = []
for data in numbers, strings, arrays:
    addition = threading.Thread(target=sum, args=data)
    addition.start()
    threads.append(addition)

for thr in threads:
    thr.join()



