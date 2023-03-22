from socket import *

serverPort = 12345

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('The server is ready on port {0}'.format(serverPort))

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    print('Message from Client: {0}'.format(msg.decode()))
    modefiedMsg = msg.decode().upper()
    serverSocket.sendto(modefiedMsg.encode(), clientAddr)
    print('Modefied Message Sent!')
