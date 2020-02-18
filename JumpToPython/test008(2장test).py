# Q1
hong = {"국어":80, "영어":75, "수학":55}
print(len(hong))
print(hong["국어"])
sum = hong["국어"] + hong["영어"] + hong["수학"]
print(sum)
average = sum / len(hong)
print(average)

# Q2
num = 13
if num % 2 == 1 :
    print("홀수")
else:
    print("짝수")

# Q3
pin = "881120-1068234"
yyyymmdd = pin[0:6]
print(yyyymmdd)
num = pin[0:6] + pin[7:]
print(num)

# Q4
pin = "881120-1068234"
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# Q7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)        # list를 문자열로 만드는 함수 join
print(result)

# Q8
a = (1, 2, 3)
a += (4,)   # 튜플식 더하기
print(a)

# Q9
a = dict()
print(a)
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
#a[[1]] = 'python' 이거 오류임 이유 : 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없기 때문이다.
#print(a)
a[250] = 'python'
print(a)

# Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)   # B의 Value만 나옴

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)   # a 리스트를 집합자료형으로 중복요소 하나로
print(aSet)
b = list(aSet)  # 집합자료형을 리스트자료형으로
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)