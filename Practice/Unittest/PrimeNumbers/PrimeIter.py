class NonValidInput(Exception):
    def __init__(self, text):
        self.txt = text


# Итератор по простым числам

class PrimeIter:
    def __init__(self, max):
        self.cur = 0
        self.max = max
        self.number = 1
        if not isinstance(self.max, int) or self.max < 0:
            raise NonValidInput('Wrong type of argument')
    def check_prime(self, number):
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
                break
            i += 1
        else:
            return True
    def __iter__(self):
        return self
    def __next__(self):
        self.number += 1
        if self.cur == self.max:
            raise StopIteration
        elif self.check_prime(self.number):
            self.cur += 1
            return self.number
        else:
            return self.__next__()




