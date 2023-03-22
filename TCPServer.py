from socket import *

serverPort = 12345

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready on port {0}'.format(serverPort))

while True:
    # create a new socket for each connection
    connectionSocket, clientAddr = serverSocket.accept()
    print('Listening....')
    msg = connectionSocket.recv(2048).decode()
    modefiedMsg = msg.upper()
    connectionSocket.send(modefiedMsg.encode())
    print('Modeifed Message Sent!')
    connectionSocket.close()
    print('Connection Closed!')
