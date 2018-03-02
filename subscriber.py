from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000
command = ['sub','quit']

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

current_topic = ''
#message = input('Client >: ')
while True:
    print ('Subscriber:> ', end='') 
    sys.stdout.flush()
    txtout = sys.stdin.readline().strip()
    cmd,arg = txtout.split(None,1)
    if cmd in command:
        s.send(txtout.encode('utf-8'))
        if txtout == 'quit':
            break
        else:
            while True:
                modifiedMsg = s.recv(2048)
                print (modifiedMsg.decode('utf-8'))

s.close()
