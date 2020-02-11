import socket
import numpy as np
import cv2

# Socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count) # sock.recv:소켓으로부터 데이터 읽을 때
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # client 소켓 생성, IP4v와 TCP
client_socket.connect((HOST, PORT))  # IP주소와 port번호에 컨넥

while True:
    message = '1'
    client_socket.send(message.encode())   # 메세지인코드데이터 서버에게 전송

    length = recvall(client_socket, 16)   # recvall 함수 실행하여 buf 값 length에 넣기
    stringData = recvall(client_socket, int(length))
    data = np.frombuffer(stringData, dtype='uint8')

    decimg = cv2.imdecode(data, 1) # 데이터 디코딩
    cv2.imshow('Image', decimg)

    key = cv2.waitKey(1)
    if key == 27:
        break

client_socket.close()