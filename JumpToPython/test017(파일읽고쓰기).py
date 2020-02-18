# 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:/test/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)   # data를 파일 객체(f)에 써라
    print(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
# readline 함수
# readline.py
f = open("C:/test/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# readline_all.py
f = open("C:/test/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# read 함수
f = open("C:/test/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# data 추가모드
f = open("C:/test/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()

# with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
with open("foo.txt", "w") as f:     # with는 close 안해도 자동적으로 close실행됨
    f.write("Life is too short, you need python")


