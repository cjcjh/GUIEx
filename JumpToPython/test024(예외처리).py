a = [1, 2]
try:
    a[3]
except IndexError as e:
    print(e)


f = open('foo.txt', 'w')
try:
    print('aaaaa')
finally:
    f.close()


#여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[1])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    a = [1,2]
    print(a[1])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError:
    print(e)

try:
    a = [1,2]
    print(a[1])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)


#say_nick('천사')
#say_nick('바보')
