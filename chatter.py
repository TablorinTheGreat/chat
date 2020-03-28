from msvcrt import getch
import sys
import thread
import socket
def chat():
    global logged
    while logged:
        data=raw_input()
        if data=="0":
            my_socket.send(data)
            logged=False
        my_socket.send(name+": "+data)
logged=True
name=raw_input("enter name")
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 1729))
my_socket.recv(1024)
print("connected")
print("press 0 for new chatroom\npress 1 and then the room key to log")
data=raw_input()
my_socket.send(data)
if data=="1":
    my_socket.send(raw_input("enter chat key"))
result=my_socket.recv(1024)
if result=="e":
    print("error please start again")
else:
    print(result)
    print("press 0 to log off")
    thread.start_new_thread( chat,() )
    while logged:
       print(my_socket.recv(1024))
my_socket.close()

