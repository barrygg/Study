import time


# Context manager measuring function's execution time
class TimeManager:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(str(time.time() - self.start))

def myenum_1(items=[i for i in range(1,100)]):
        result = []
        j = 0
        for i in items:
            tup = (j, i)
            result.append(tup)
            j +=1
        return result

def myenum_2(items=[i for i in range(1,100)]):
        result = []
        for i in range(len(items)):
            tup = (i, items[i])
            result.append(tup)
        return result

with TimeManager():
    myenum_1()
    time.sleep(1)


with TimeManager():
    myenum_2()
    time.sleep(1)





