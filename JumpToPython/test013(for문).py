# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...
test_list = ['one', 'two', 'three']
for i in test_list:
     print(i)

a = [(1,2), (3,4), (5,6)]   #튜플선언
for (first, last) in a:
    print(first + last)

# range 함수
a = range(10)
print(a)  # range(0, 10) : 0~9

add = 0
for i in range(1, 11):
    add = add + i
    print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        print('땡')
    else:
        print('합격이오')


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="\t")    # 그 다음 줄로 엮어주기 위해 end= 사용
    print('')


a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a2 = [1, 2, 3, 4]
result2 = [num * 3 for num in a2]
print(result2)

result3 = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result3)