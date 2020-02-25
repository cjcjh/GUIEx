def foo (id , name):
    print(id, name)
    id = name
    print(id)
    name = id
    print(name)
    return (id, name)

id = 3
name = "kim"

id, name = foo(id, name)

print("id = ", id, ", name = ", name)

a = [1, 2, 3, 4, 56, 3, 4, 34]
def maybeBubbleSort(list1):
    sorted = False
    while (not sorted) :
        sorted = True
        for i in range(1, len(list1)):
            if (a[i-1] > a[i]):
                a[i-1], a[i] = a[i], a[i-1]
                sorted = False

def is_palindrome(s):  # 기러기 탐지
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -i -1]:
            return False
    return True

# 문자열 객체 사용 함수
# upper() : 소문자 -> 대문자
# lower() : 대문자 -> 소문자
# capitalize() : 첫 글자 대문자로
# isalpha() : 문자열이 전부 알파벳인가?
# isdigit() : 문자열이 전부 숫자인가?
# startswith(prefix) : 문자열이 prefix로 시작하는가?
# endswith(suffix) : 문자열이 suffix로 끝나는가?
# find(str1) : 문자열 안에 str1이 나타나는 첫 위치 반환
# find(str1, start) : str1부터 start나오는 인덱스 위치 반환
# find(str1, start, end) : start부터 end-1 사이에서 str1 인덱스 위치 반환
# replace(str1, str2) : 문자열 바꾸기
# rstrip() : 주어진 문자열에서 오른쪽 공백을 제거
# lstrip() : 주어진 문자열에서 왼쪽 공백을 제거
# strip() : 주어진 문자열에서 양 옆 공백을 제거
# split() : 문자열의 (공백 문자로 분리된) 단어들을 포함한 리스트 생성
# split(sep) : sep 기준으로 문자열 나누기 , " " : 등
# join(list1) : a.join(b)경우 b에 있는 각각의 문자들 사이에 a를 넣음

s = "abcdef"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.isalpha())
print(s.isdigit())
s2 = "1234"
print(s2.isdigit())
print(s.startswith("ef"))
print(s.endswith("ef"))
s = s.replace("de", "123")
print(s)

s = "12ab34cd"
print(s.find("ab"))
print(s.find("z"))
print(s.find("ab", 4))  # index(4)뒤에 ab있니?? 없으니 -1 나옴
print(s.find("ab", 1)) # index(1)뒤에 ab있니?? 있으니 2
print(s.find("ab", 1, 6))  # index(1~6)에 ab 있니?? 있으니 2

s = "   abc def   "
print(s.rstrip())
print(s.lstrip())
print(s)
print(s.strip())
s1 = s.strip()
print(s1)
print(s1.split())
s2 = "ab cd ef gh"
l2 = s2.split() # split 기본은 공백기준으로 나눔
print(l2)
s3 = "2019/12/13"
print(s3.split("/"))
s1 = "1234"
s2 = "abc"
print(s1.join(s2))  # s1을 s2 문자사이에 join해

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
emptyset = set()
randomset = {4, 6, 2, 7, 5, 2, 3}
print(odds)
print(evens)
emptyset = set()        # set화하는 것
print(randomset)
for num in odds: #
    print(num)
# s.add(v) : 원소 v를 집합 s에 추가
# s.remove(v) : 원소 v를 집합 s에서 제거
# s.pop() : 무작위 원소를 집합 s에서 제거 후 원소를 반환
# s.intersection(k) : 집합 s, k의 공통 원소를 반환(s n k)
# s.union(k) : 집합 s, k의 합집합을 반환 (s u k)
# s.difference(k) : 집합 k에 있는 원소들을 s에서 뺀 집합을 반환
randomset.add(9)
print(randomset)
randomset.remove(7)
print(randomset)
print(randomset.pop())
print(randomset)
print(randomset.intersection(odds))  # odds = 1, 3, 5, 7, 9 교집합
print(randomset.union(evens))   # evens = 2, 4, 6, 8, 10 합집합
print(randomset)
print(randomset.difference(odds))   #  randomset에 있고 odds에 없는 것 3, 4, 5, 6, 9 중에 홀수가 아닌 것
print(odds.difference(randomset)) # odds(1, 3, 5, 7, 9)에 randomset에 없는 숫자
print(randomset.difference(odds, evens)) # odds와 evens의 합집합을 빼면 randomset이 0~10사이에 있으니 공집합 set()나옴
