# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다.
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
# import (모듈내임)
# mod1.py 로 저장했다면
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
import mod1
import mod2
from mod1 import add, sub
#from mod1 import *

print(add(1, 4))
print(sub(4, 2))

PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r ** 2)    # 원의 넓이 계산
print(Math.solv(PI, 5))

print(mod1.add(3,4))
print(mod2.add(mod2.PI, 4.4))
