print(abs(3))   # abs는 절댓값돌려주는 함수
print(abs(-3))
print(abs(-1.2))

print(all([1,2,3]))
print(all([1,2,3,0])) # all 은 하나라도 거짓이면 False

print(any([1,2,3,0])) # any는 모두 거짓일 때 False
print(any([0, ""]))

print(chr(97))  # char는 아스키 코드 값을 입력받아
print(chr(48))  # 그 코드에 해당하는 문자를 출력

print(dir([1, 2, 3])) #객체가 자체적으로 가지고 있는 변수나 함수보여줌
print(dir({'1':'a'}))

print(divmod(7, 3)) # 7/3 몫과 나머지를 튜플형태로 돌려주는 함수

# enumerate : 열거하는 함수
# 순서가 있는 자료형(리스트, 튶,ㄹ 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1+2'))  # 실행 가능한 문자열을 입력받아 실행
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# filter( 함수, 반복가능한 자료형 요소 )
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(hex(234))     #정수값 -> 16진수로
print(hex(3))

a = 3
print(id(3))
print(id(a))
b = a
print(id(b)) # id(object) 객체 입력받아 객체의 고유 주소값 돌려줌

#a = input() #사용자 입력을 받는 함수
#b = input('Enter : ')

print(int('3'))     #int 숫자나 소수점숫자 등을 정수형태로
print(int(3.4))
print(int('11', 2)) # 2진수로표현된 11 10진수 값으로 3
print(int('1A', 16)) # 16진수로 표현된 1A의 10진수 값으로 26

class Person: pass
a = Person()
print(isinstance(a, Person))    #isinstance(인스턴스, 클래스이름)
b = 3   # b는 클래스 인스턴스가 아니니 False
print(isinstance(b, Person))

print(len('python')) #입력값 s의 길이
print(len([1,2,3]))
print(len((1, 'a')))

print(list('python')) #반복 가능한 자료형 s 받아 리스트로 돌려줌
print(list((1, 2, 3)))

# map(f, iterable) 함수(f), 반복가능한(iterable) 자료형
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1, 2, 3, 4])
print(result)

def two_times2(x): return x*2
print(list(map(two_times2, [1, 2, 3, 4]))) # 맵 결과 list로

print(max([1,2,3])) # 반복 가능한 자료형 입력받아 최댓값 돌려줌
print(max("python"))
print(min([1,2,3])) # 최솟값 돌려줌
print(min('python'))

print(oct(34))  # 정수 형태의 숫자를 8진수 문자열로 바꿈
print(oct(12345))

# open(filename, [mode])
# w	쓰기 모드로 파일 열기
# r	읽기 모드로 파일 열기
# a	추가 모드로 파일 열기
# b	바이너리 모드로 파일 열기
# f = open("binary_file", "rb")   #바이너리 읽기모드
# fread = open("read_mode.txt", 'r')
# fread2 = open("read_mode.txt")  #기본값으로 읽기모드임
# fappend = open("append_mode.txt", 'a')  # 추가 모드

print(ord('a')) #문자의 아스키 코드 값을 돌려주는 함수
print(ord('0'))
print(pow(2, 4)) # x의 제곱한 결괏값을 돌려주는 함수
print(pow(3, 3))

# range([start], stop[,step])
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2))) #세번째 인수는 숫자 사이의 거리
print(list(range(0, -10, -1)))

print(round(4.6))   # 숫자를 입력받아 반올림해주는 함수
print(round(4.2))
print(round(5.678, 2))  #실수 소수점 2자리까지만 반올림가능

print(sorted([3, 1, 2]))    #입력값 정렬한 후 돌려줌
print(sorted(['a', 'c', 'b']))
print(sorted('zero'))

print(str(3))   #문자열 형태로 객체를 변환
print(str('hi'))
print(str('hi'.upper()))

print(sum([1,2,3])) # 입력받은 리스트, 튜플 모든 요소 합하고 돌려줌
print(sum((4,5,6)))

print(tuple("abc")) # 반복 가능한 자료형 입력받아 튜플 형태로 변형
print(tuple([1,2,3]))
print(tuple((1,2,3)))

print(type('abc'))  #type은 입력값의 자료형이 무엇인지 알려줌
print(type([]))
print(type(open('test', 'w')))

print(list(zip([1,2,3], [4,5,6]))) # 동일한 개수로 이루어진 자료형 묶음
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip("abc", "def")))




