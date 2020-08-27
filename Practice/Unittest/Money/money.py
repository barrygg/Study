class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop
        self.sum = self.rub * 100 + self.kop

    def __add__(self, other):
        return Money((self.sum + other.sum) // 100, (self.sum + other.sum) % 100)

    def __sub__(self, other):
        return Money((self.sum - other.sum) // 100, (self.sum - other.sum) % 100)

    def __truediv__ (self, n):
        m = n * 100
        r = int(self.sum / m)
        k = self.sum / n - r * 100
        return Money(r, int(k))

    def __gt__(self, other):
        if self.sum > other.sum:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.sum < other.sum:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.sum >= other.sum:
            return True
        else:
            return False

    def __le__(self, other):
        if self.sum <= other.sum:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.sum == other.sum:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.sum != other.sum:
            return True
        else:
            return False

    def getmoney(self):
        return(f"{self.rub} rub,{self.kop} kop")

    def getcourse(self, course):
        self.course = course
        return (self / course).getmoney()
