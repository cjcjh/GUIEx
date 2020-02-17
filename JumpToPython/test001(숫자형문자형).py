print("{0:!<10}".format("hie")) # 왼쪽 정렬
print("{0:!>10}".format("hie")) # 오른쪽 정렬
print("{0:!^10}".format("hiee")) # 가운데 정렬

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')  # f문자열 포매팅

d = {'name':'홍길동', 'age':30}  #딕셔너리
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f'{"python":!^12}')

print(",".join('abcd'))   # 문자열 삽입 join

a = 'hi'
print(a.upper())    # 소문자 -> 대문자
b = 'HI'
print(b.lower())    # 대문자 -> 소문자
c = '  hi  '
print(c.lstrip())   # 왼쪽공백지우기 : lstrip
print(c.rstrip())   # 오른쪽 공백지우기 : rstrip
print(c.strip())    # 양쪽 공백지우기 : strip

a = "Life is too short"
print(a)
a.replace("Life", "Your leg")
print(a)   # a에 replace한거 입력하지 않았음
print(a.replace("Life", "Your leg"))
print(a)
print(a.split())  # 문자열 나누기 : split
b = "Life.is.too.short"
print(b.split('.')) # 기호를 기준으로 문자열 나눔


