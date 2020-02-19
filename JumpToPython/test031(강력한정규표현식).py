# 문자열 소비가 없는 메타문자
# | : or 과 동일한 인식
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# ^ 처음문자인식
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $ 끝문자인식
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A 는 문자열의 처음과 매치됨
# \Z 는 문자열의 끝과 매치
# \b 는 단어 구분자 (Word boundary)
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  # match됌
print(p.search('one subclass is'))  # class앞에 sub있어서 안됌

# \B : \b의 반대경우 whitespace 로 구분된 단어가 아닌 경우
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  # \b가 되는 경우라 None
print(p.search('the declassified algorithm'))   # \b가 앞뒤 인식으로 안되어 match 됌
print(p.search('one subclass is'))  # 앞에 하나 오류여서 안됌 두개다 오류여야 match됌




# 그루핑
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
print(m.group(0))

# group(0)	매치된 전체 문자열
# group(1)	첫 번째 그룹에 해당되는 문자열
# group(2)	두 번째 그룹에 해당되는 문자열
# group(n)	n 번째 그룹에 해당되는 문자열

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

# 그루핑된 문자열에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())

# 전방 탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# 긍정형 전방 탐색((?=...)) - ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색((?!...)) - ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())


# .*[.].*$  : 이 정규식은 파일 이름 + . + 확장자를 나타내는 정규식
# .*[.][^b].*$  :  확장자가 b라는 문자로 시작하면 안 된다는 의미
# .*[.]([^b]..|.[^a].|..[^t])$ :  | 메타 문자를 사용하여 확장자의 첫 번째 문자가 b가 아니거나 두 번째 문자가 a가 아니거나 세 번째 문자가 t가 아닌 경우를 의미
# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$  :  확장자의 문자 개수가 2개여도 통과되는 정규식

# .*[.](?!bat$).*$  :  확장자가 bat가 아닌 경우에만 통과된다는 의미
# .*[.](?!bat$|exe$).*$  :   exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 간단히 표현

# 문자열 바꾸기 : sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
print(p.sub('colour', 'blue socks and red shoes', count=1))

p = re.compile('(blue|white|red)')
print(p.subn( 'colour', 'blue socks and red shoes'))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

def hexrepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))

s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
