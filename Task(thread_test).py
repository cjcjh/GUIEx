import _thread, time

# thread에서 실행될 함수
def counter(id):
    for i in range(5):
        print('id %s --> %s' % (id, i))
        time.sleep(0.1)

# thread 5개 실행
for i in range(5):
    _thread.start_new_thread(counter, (i,))

# thread가 다 돌 때까지 대기
time.sleep(1)
print('Exiting')

