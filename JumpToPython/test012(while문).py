# while문을 반복문이라 부른다.
# while문의 기본 구조이다.
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# break 멈추기
# continue : 맨 처음으로 돌아가기

a = 1
while a <= 10:
    print(a)
    a += 1
    if a % 3 == 0: a+= 1