import time
import threading
import multiprocessing



# Wrappers, multithread, multiprocess; sieve of eratospenes is for comparison
def sieve_eratosphenes(n):
     a = [x for x in range(n + 1)]
     a[1] = 0
     result = []
     i = 2
     while i <= n:
         if a[i] != 0:
             result.append(a[i])
             for j in range(i, n+1, i):
                 a[j] = 0
         i += 1
     return result


def timer(func): # wrapper-timer
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print("Spent: {} seconds".format(time.time()-t))
        return res
    return tmp


def prime_number(m, n): # almost right function checking prime numbers
    if m % 2 == 0:
        m += 1
    result = []
    for i in range(m, n + 1, 2):
        j = 3
        while True:
            if i % j == 0:
                break
            if (j * j) > i:
                result.append(i)
                break
            j += 1
    return result

@timer
def prime_single():
    for a, b  in zip(begin, end):
        prime_number(a, b)


@timer
def prime_multithreads():
    threads = []
    for a, b  in zip(begin, end):
        thr = threading.Thread(target = prime_number, args = (a, b))
        thr.start()
        threads.append(thr)
    for thr in threads:
        thr.join()


@timer
def prime_multiproc():
    proc = []
    for a, b  in zip(begin, end):
       p = multiprocessing.Process(target=prime_number, args=(a, b))
       p.start()
       proc.append(p)
    for p in proc:
        p.join()


# Многопроцессность даёт выигрыш во времени при длине интервала > 12000 при 3 интервалах
# или при длине интервала 10000 при числе интервалов > 4
# При длине интервала 100000 и количестве 3: выигрыш в два раза
# Нормально реализованное решето Эратосфена даёт выигрыш в 10 раз на этом интервале
# Мультипоточность не даёт заметного выигрыша в скорости как при длинных, так и при коротких интервалах
# по сравнению с одним потоком. Но результат не чистый, так как второй и третий поток вынуждены искать
# делители в диапазоне [3, sqrt(begin)] и проверять делимость

# if __name__ == '__main__':
#    prime_single()
#    print('Multithreads:')
#    prime_multithreads()
#    print('Multiprocesses:')
#    prime_multiproc()
#    print('Sieve of Eratosphenes:')
#    sieve_eratosphenes = timer(sieve_eratosphenes)
#    sieve_eratosphenes(end[2])




