import socket
import thread
roomKeys=range(30)
userKeys=100
chatters=[]
rooms={}
def send(data,chatters,sender):
    global chatter
    for chatter in chatters:
        if chatter is not sender:
            chatter.send(data)
def roomChat(room):
    global chatters,roomKeys,rooms
    print("starting room")
    while len(rooms[room])>0:
        for chatter in rooms[room]:
            try:
                data=chatter.recv(1024)
                if(data.isdigit())and int(data)==0:#logoff
                        rooms[room].remove(chatter)
                        chatters.remove(chatter)
                        chatter.send("logged off")
                        print("chatter logged off")
                else:
                    send(data,rooms[room],chatter)
            except:
                i=0
    print("room closed")
    roomKeys.append(room)
    rooms.pop(room)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1729))
print("server started")
server_socket.listen(userKeys)
print("listening...")
while 1:
    if(userKeys>0):
        client, address = server_socket.accept()
        print("client accepted")
        userKeys-=1
        chatters.append(client)
        client.send('1')
        code=client.recv(1024)
        if code.isdigit():
            code=int(code)
            if code==0:#new room
                if len(roomKeys)>0:
                    room=roomKeys.pop(0)
                    rooms[room]=[]
                    rooms[room].append(client)
                    client.send(str(room))
                    client.setblocking(False)
                    thread.start_new_thread(roomChat,(room,))
                else:
                    client.send('e')
            elif code==1:#enter room
                room=client.recv(1024)
                room=int(room)
                if room in roomKeys or room>=30 or room<0:
                    client.send('e')
                else:
                        rooms[room].append(client)
                        client.send(str(room))
                        client.setblocking(False)
        del client



