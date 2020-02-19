# 보통 1개의 프로세스는 한 가지 일만 하지만
# 스레드를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.
""" # test1
import time

def long_task(): # 5초의 시간이 거리는 함수
    for i in range(5):
        time.sleep(1)
        print("working:%s" %i)

print("Start")
for i in range(5):
    long_task()
print("End")
"""
"""
# test2    --> threads가 뭔지 잘 몰라서 start 와 end 인식이 안되었을때
import time
import threading    # 스레드 생성하기 위해 threading 모듈 필요
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" %i)
print("Start")
threads = []
for i in range(5):
    t = threading.Thread(target=long_task) # 스레드 생성
    threads.append(t)

for t in threads:
    t.start()

print("End")
"""

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()    # join으로 스레드가 종료될 때까지 기다린다.

print("End")