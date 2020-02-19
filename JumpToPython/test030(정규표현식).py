# 정규 표현식 살펴보기
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규 표현식 시작하기
# 메타문자 : . & $ * + ? { } [ ] \ | ( )

# 문자클래스 []
# [a-zA-Z] : 알파벳 모두  # 하이픈(-) : 범위지정
# [0-9] : 숫자
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

# Dot(.)
# a.b
# "a + 모든문자 + b"
# 즉 a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치된다는 의미이다.

# 반복(*)
# ca*t	ct	    Yes	"a"가 0번 반복되어 매치
# ca*t	cat	    Yes	"a"가 0번 이상 반복되어 매치 (1번 반복)
# ca*t	caaat	Yes	"a"가 0번 이상 반복되어 매치 (3번 반복)

# 반복(+)
# ca+t
# "c + a(1번 이상 반복) + t"
# ca+t	ct	    No	"a"가 0번 반복되어 매치되지 않음
# ca+t	cat	    Yes	"a"가 1번 이상 반복되어 매치 (1번 반복)
# ca+t	caaat	Yes	"a"가 1번 이상 반복되어 매치 (3번 반복)

# 반복 ({m,n}, ?)
# {3,}처럼 사용하면 반복 횟수가 3 이상인 경우이고 {,3}처럼 사용하면 반복 횟수가 3 이하를 의미
# ca{2}t
# ca{2}t	cat 	No	"a"가 1번만 반복되어 매치되지 않음
# ca{2}t	caat	Yes	"a"가 2번 반복되어 매치
#
# ca{2,5}t   # a가 2~5번까지 인정
# ca{2,5}t	cat	    No	"a"가 1번만 반복되어 매치되지 않음
# ca{2,5}t	caat	Yes	"a"가 2번 반복되어 매치
# ca{2,5}t	caaaaat	Yes	"a"가 5번 반복되어 매치

# ?
# ab?c   # 2가지 경우이다
# "a + b(있어도 되고 없어도 된다) + c"
# ab?c	abc	Yes	"b"가 1번 사용되어 매치
# ab?c	ac	Yes	"b"가 0번 사용되어 매치




# re 모듈
import re
p = re.compile('ab*')
print(p)


# 정규식을 사용한 문자열 검색
# match()	문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
p = re.compile('[a-z]+')
m = p.match("python")
print(m)    # match='python'
m = p.match("3 python")
print(m)    # none

#p = re.compile('정규표현식')
#m = p.match("조사할 문자열")
if m:
    print('Match found: ', m.group())
else:
    print('No match')

m = p.search("python")
print(m)    # 책과 결과물이 다른데???
m = p.search("3 python")
print(m)

result = p.findall("life is too short")
print(result)   # 문자열의 [a-z]+ 정규식과 매치해서 리스트로

result = p.finditer("life is too short")
print(result)
for r in result: print(r)


# match 객체의 메서드
# method  목적
# group()	매치된 문자열을 돌려준다.
# start()	매치된 문자열의 시작 위치를 돌려준다.
# end()	매치된 문자열의 끝 위치를 돌려준다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())


# 컴파일 옵션
# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

import re
p = re.compile("^python\s=w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))


# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
&[#]            # Start of a numeric entity reference
(
    0[0-7]+     # Octal form
    | [0-9]+    # Decimal form
    | x[0-9a-fA-F]+ # Hexadecimal form
    )
    ;           # Trailing semicolon
""", re.VERBOSE)    # re.VERBOSE 옵션 : 문자열에 사용된 whitespace 컴파일할 때 제거


# 백슬래시 문제
p = re.compile('\\section') # 백슬래시 2개 사용하여 이스케이프 처리 4개 1개변경 된거도있음




