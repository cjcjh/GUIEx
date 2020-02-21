# Q1 문자열 바꾸기
a = "a:b:c:d"
a = a.split(":")
print(a)
a = "#".join(a)
print(a)

# Q2 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a['C'] = 70
print(a)

# Q3 리스트의 더하기와 extend 함수
a = [1, 2, 3]
a = a + [4, 5]
print(a)
a = [1, 2, 3]
a.extend([4, 5])
print(a)
# + 와 extend 의 차이
# + 하게되면 a의 저장 주소가 바뀐다. id(a) 확인가능
# extend 하게되면 a의 저장 주소 유지된다.

# Q4 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
A_sum = 0
for i in range(len(A)):
    if A[i] >= 50:
        A_sum += A[i]
print('합 :', A_sum)

# Q5 피보나치 함수
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

n = input('피보나치 함수 개수 : ')
for i in range(int(n)):
    print(fib(i), end=', ')


# Q6 숫자의 총합 구하기
S = input("숫자들 콤마구분하여 입력하기 : ")
S = S.split(',')
total = 0
for i in S:
    total += int(i)
print(total)


# Q7 한 줄 구구단
n = input('구구단을 출력할 숫자를 입력하세요(2~9) : ')
n = int(n)  # 문자열을 입력 받았으니 숫자 계산을 위해 int로 변경
for i in range(1, 10):
    print(n * i, end=' ')
print('')


# Q8 역순 저장
f = open('abc.txt', 'w')
f.write("""AAA
BBB
CCC
DDD
EEE""")
f.close()

f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()
f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  # 한줄 단어 좌우공백지우기, 줄수똑같게하려고
    f.write(line)
    f.write('\n')
f.close()


# Q9 평균값 구하기
f = open('sample.txt', 'w')
f.write("""70
60
55
75
95
90
80
80
85
100
""")
f.close()

f_sum = 0
f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    f_sum += int(line)  # int로 정수 입력이 필요

f_avg = f_sum / len(lines)  # 줄수이니 len 필요
f = open('sample.txt', 'a')
f.write(str(f_avg)) # 정수를 문자열로
f.close()


# Q10 사칙연산 계산기
class Calculator():
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numberList)

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())


# Q11 모듈 사용 방법
import sys
sys.path.append("./")
import mymod


# Q12 오류와 예외 처리
result = 0
try:
    [1, 2, 3][3]    # 여기서 바로 index Error 발생하여 끝 +3 +4
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)


# Q13 DashInsert 함수
data = input("검색 수 : ")
numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):   # enumerate : 자료형(list tuple 문자열) 입력 받아 인덱스 값을 포함하는 객체를 돌려줌
    result.append(str(num)) # value값 추가
    if i < len(numbers)-1:  # 최종열까지 비교
        is_odd = num % 2 == 1   # 홀수니? == 1 홀수 아니면 짝수
#       is_odd = numbers[i] % 2 == 1    위에 줄과 같음
        is_next_odd = numbers[i+1] % 2 == 1 # 다음수 너 홀수니??
        if is_odd and is_next_odd:  # 연속 홀수니???
            result.append("-")
        elif not is_odd and not is_next_odd:    #연속 짝수니???
            result.append("*")

print("".join(result))      # 리스트 표현이 아니라 한단어로 나오게


# Q14 문자열 압축하기
data = input("문자열 입력해줘 : ")
def compress_string(data):
    _c = ""   # 다음문자
    cnt = 0     # 반복 수
    result = ""  # 분석완료한 문자열
    for c in data:  # 문자열(data)에 c 분석해
        if c != _c:     # 현재문자와 다음문자 틀리니?
            _c = c      # 다음문자 현재문자와 같게
            if cnt:     # cnt 가 True 니???
                result += str(cnt)  # result에 측정동일수 추가해줘
            result += c # 다른 문자 추가
            cnt = 1     # count = 1
        else:    # 현재문자 다음문자 동일하다
            cnt += 1
    result += str(cnt)  # 마지막 문자 개수 추가
    return result

print(compress_string(data))


# Q15 Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:   # 중복된 값이 있니 없니
            result.append(num)
        else:   # 중복된 값이 있다면
            return False
    return len(result) == 10    # 입력된 길이가 맞니? 맞으면 True

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))


# Q16 모스 부호 해독
dic = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


# Q17 기초 메타 문자
import re
p = re.compile('a[.]{3,}b')   # a(1번) .(3번이상) b(1번)
print(p.match("acccb"))
print(p.match("a.......b"))
print(p.match("aaab"))
print(p.match("a.cccb"))


# Q18 문자열 검색
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end()) # 문자열 처음나온 p = 2, 마지막 n = 8


# Q19 그루핑
import re
s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####",s)
print(result)


# Q20 전방탐색
import re
pat = re.compile(".*[@].*[.](?=com$|net$).*$")
print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))