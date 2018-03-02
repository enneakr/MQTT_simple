
from socket import * 
from threading import Thread
import os,sys

SERV_PORT = 50000
publish_list = {}
subsribe_list = {}

def handle_client(s):
  while True:
     txtin = s.recv(1024)
     print ('Client> %s' %(txtin).decode('utf-8'))
     cmd,arg = txtin.decode('utf-8').split(None,1)

     if cmd == 'topic':
        if s not in publish_list:
            publish_list[s] = arg
            print(str(publish_list))
            s.send(("checked").encode('utf-8'))
        else:
            s.send(("Must cancel current topic").encode('utf-8'))

     elif cmd == 'cancel':
        if publish_list[s] == arg:
            del publish_list[s]   
            # print(str(publish_list))
            s.send(("canceled").encode('utf-8'))
        else:
            s.send(("invalided").encode('utf-8')) 
    
     elif cmd == 'publish':
         if s in publish_list:
             current_topic = publish_list[s]
             for x,y in subsribe_list.items():
                 if y == current_topic:
                     x.send((arg).encode('utf-8'))
                     s.send(("published successful").encode('utf-8'))
           
     elif cmd == 'sub':
         subsribe_list[s] = arg
         print(str(subsribe_list))

     elif txtin == b'quit':
        print('Client disconnected ...')
        break
    
  s.close()
  return

def main():
  addr = ('127.0.0.1', SERV_PORT)
  s = socket(AF_INET, SOCK_STREAM)
  s.bind(addr)
  s.listen(5)
  print ('TCP threaded server started ...')

  while True:
    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1]) 
    print ('New client connected from ..' + ip + ':' + port)
  
    try:
      Thread(target=handle_client, args=(sckt,)).start()
    except:
      print("Cannot start thread..")
      import traceback
      traceback.print_exc()

  s.close()

if __name__ == '__main__':
   try:
     main()
   except KeyboardInterrupt:
     print ('Interrupted ..')
     try:
       sys.exit(0)
     except SystemExit:
       os._exit(0)
