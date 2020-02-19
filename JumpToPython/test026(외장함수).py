import sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import os
# os는 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
import shutil
# shutil은 파일을 복사해 주는 파이썬 모듈
import glob
# 특정 디렉터리에 있는 파일 이름 알 때 사용하는 모듈
import tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈
import time
# 시간과 관련된 time 모듈 함수 많다.
import calendar
# 달력을 볼 수 있게 해주는 모듈
import random
# 난수를 발생시키는 모듈
import webbrowser
# 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
#sys
print(sys.argv) # 실행하는 python 주소
print(sys.path) # sys 실행 주소

#pickle
f = open("test.txt", "wb")
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

# os
#es.environ = (내)현재 시스템의 환경 변수 값을 알고 싶을 때
print(os.environ)   #딕셔너리 객체들
print(os.environ['path']) # 딕셔너리 주소
#print(os.chdir("C:\WINDOWS")     # 현재 디렉터리 위치 변경
print(os.getcwd())  # 현재 자신의 디렉터리 위치
print(os.system('dir')) # 현재 디렉터리에서 시스템 명령어 dir 실행
#실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
f = os.popen('dir')
print(f.read())
# os.mkdir(디렉터리)	디렉터리를 생성한다.
# os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
# os.unlink(파일)	파일을 지운다.
# os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# shutil
shutil.copy("test.txt", "dst.txt") #('이파일', '이이름으로')복사해

# glob(pathname)
print(glob.glob('c:/Users/BIT/PycharmProjects/GUIEx/JumpToPython/*.py'))

# tempfile
filename = tempfile.mktemp() #중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
print(filename)
f = tempfile.TemporaryFile() #임시저장공간으로 사용할 파일객체 기본적 wb모드
f.close() #생성한 임시파일 자동 삭제

# time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))    #날짜 시간으로
print(time.ctime()) # ctime 은 항상 현재 시간만 돌려줌
#time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
for i in range(10):
    print(i)
    time.sleep(0.1)   # 1초간격쉬기 0.5도 가능 여러가지 가능

# calendar
print(calendar.calendar(2020))  #1~12월 다보여줌
print(calendar.prcal(2020))     #위와 똑같은 결과
print(calendar.prmonth(2020, 2)) # 2020년 2월 달력보여줘
print(calendar.weekday(2020, 12, 31)) # 0월 1화 2수 3목 4금 5토 6일
print(calendar.monthrange(2020, 12)) # 결과(요일, 날짜수) = (화요일 1, 31)

# random
print(random.random())  # 난수(규칙이 없는 임의의 수)값
print(random.randint(1, 10))
print(random.randint(1, 55))
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)
if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))
data = [1,2,3,4,5]
random.shuffle(data)
print(data)

# webbrower
#webbrowser.open("http://google.com") #사용중인창
webbrowser.open_new("http://google.com") # 새창