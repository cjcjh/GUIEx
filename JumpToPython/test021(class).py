# 계산기

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

#a = FourCal()
#b = FourCal()
a = FourCal(4, 2)
b = FourCal(3, 8)   #__init__ 했으니 setdata 필요없음
#a.setdata(4, 2)
#b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
a = MoreFourCal(4, 2)
print(a.pow())