# 불 자료형이란 참과 거짓을 나타내는 자료형이다. True & False
a = True
b = False
print(type(a))  # bool
print(type(b))  # bool
print( 1 == 1 )
print( 2 > 1 )
print( 2 < 1 )

a = [1, 2, 3, 4]
while a:
    print(a.pop())

print(a)
print(bool('python'))   # T
print(bool(''))         # F
print(bool([1,2,3]))    # T
print(bool([]))         # F
print(bool(0))          # F
print(bool(3))          # T