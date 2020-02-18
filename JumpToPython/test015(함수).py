# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

def add(a, b):  # a, b : 매개변수
    return a + b
print(add(3, 4)) # 3, 4 : 인수

def say():  #입력값이 없는 함수
    return 'Hi'
a = say()
print(a)

#여러 개의 입력값을 받는 함수 만들기
def add_many(*args):    # *args 는 임의로 정한 변수이다. *pey *python 처럼 아무 이름이나 써도 된다.
    result = 0
    for i in args:
        result = result + i
    return  result
print(add_many(1,2,3,4,5,6,7))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
add1 = add_mul('add', 1,2,3,4,5)
print(add1)
mul1 = add_mul('mul', 1,2,3,4,5)
print(mul1)

# 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)               # 둘다 모두 딕셔너리로 만들어져서 출력된다.
print_kwargs(name='foo', age=3)

# 함수의 결괏값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
result1, result2 = add_and_mul(3,4)
print(result1, result2)


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응용", 27, False)

# #def say_myself(name, man=True, old): ->오류남:초기화시키고 싶은 매개변수는 항상 뒤에놔야 오류가 안남
#     print("나의 이름은 %s입니다." % name)
#     print("나의 나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다")

# lambda 함수 = def와 동일한 역힐
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
add = lambda a, b: a+b
result = add(3, 4)
print(result)

