import socket
import cv2
import numpy
from queue import Queue
from _thread import *

enclosure_queue = Queue()  # 웹캠 돌리기위해 큐설정

# 쓰레드 함수
def threaded(client_socket, addr, queue):
    print('Connected by :', addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024) # 클라이언트가 보낸 메시지를 수신하기 위해 대기
            if not data:    # 빈 문자열을 수신하면 루프를 중지
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            stringData = queue.get()    # 큐데이터 얻기(서버가 넣어준거)
            print(str(len(stringData)).ljust(16).encode())
            client_socket.send(str(len(stringData)).ljust(16).encode())
            # client가 인식할 때 string형태로 ljust(왼쪽정렬) 변환한 문자열(크기) 전송
            client_socket.send(stringData)  # stringdata 클라이언트소켓에게 이미지 전송
        except ConnectionResetError as e:   # 연결오류시
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    client_socket.close()

def webcam(queue):
    capture = cv2.VideoCapture(0)   # 1개만 부착되어 있으면 0, 2개 이상이면 첫웹캠0다음1, cv2영상캡쳐하는 객체생성
    while True:
        ret, frame = capture.read()      # retval, image  /  ret : frame capture 결과, frame : capture한 frame
        if ret == False:   # 캡쳐가 잘 안되었으면 다시 continue(while처음으로)
            continue

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]  # image jpg 90% 품질설정, 0~100가능
        print(encode_param)
        result, imgencode = cv2.imencode('.jpg', frame, encode_param) # imencode(ext(확장자), img, parameters)
        data = numpy.array(imgencode) # numpy.array 배열 이미지인코딩하여 데이터
        stringData = data.tostring() # 촬영한 한 프레임 데이타이미지 string형태로 변환

        queue.put(stringData)  # queue에 한 프레임데이터 넣기
        cv2.imshow('image', frame) # 영상 보여주기
        key = cv2.waitKey(1)  # 종료 키
        if key == 27:
            break

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # IP4v 에 TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# SOL_SOCKET : 소켓레벨설정 -> reuseaddr허용
# SO_REUSEADDR : 이미 사용된 주소를 재사용하도록 함
server_socket.bind((HOST, PORT))  # bind : 서버소켓 IP주소, port번호 할당
server_socket.listen(5)    # 5, 0 : 적당한 값

print('server start')

start_new_thread(webcam, (enclosure_queue,))
# _thread.start_new_thread(function, args[, kwargs]) 새 스레드 시작하고 식별자 반환

while True:
    print('wait')
    client_socket, addr = server_socket.accept()   # 서버가 accept하는 과정
    start_new_thread(threaded, (client_socket, addr, enclosure_queue,))  # 클라이언트에게 스레드 실행

server_socket.close()