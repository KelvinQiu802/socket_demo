from socket import *

serverName = '127.0.0.1'
serverPort = 12345

clinetSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('Input lowercase sentence: ')
clinetSocket.sendto(msg.encode(), (serverName, serverPort))
print('Request Sent!')

modefiedMsg, serverAddr = clinetSocket.recvfrom(2048)
print('Reply from Server: {0}'.format(modefiedMsg.decode()))

clinetSocket.close()
