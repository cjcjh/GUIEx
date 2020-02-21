# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        if val < 100:
            self.value += val
        else:
            print('100이상의 값은 안돼')

        if self.value > 100:
            self.value = 100

class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

# Q3
print(all([1, 2, abs(-3)-3]))   # False
# all([1, 2, 0]) 0이 하나 있으니 False
print(chr(ord('a')) == 'a')     # True
# ord('a') = 97, char(97) = a, a == 'a' : True

# Q4
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# Q5
print(hex(234))
print(int(0xea))

# Q6
print(list(map(lambda x: x*3, [1, 2, 3, 4])))

# Q7
l = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(l))
print(min(l))

# Q8
print(round(17/3, 4))

# Q9
import sys
numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력
# python 파일명.py 1 2 3 4 5 6 7 8 9 10  이런 명령행임
result = 0
for number in numbers:
    result += int(number)
print(result)

# Q10
import os
os.chdir("C:/Users")
result = os.popen("dir")
print(result.read())

# Q11
import glob
print(glob.glob("C:/Users/BIT/PycharmProjects/GUIEx/*.py"))

# Q12
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# Q13
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)