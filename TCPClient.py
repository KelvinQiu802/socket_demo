from socket import *

serverName = '127.0.0.1'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Connected to Server')

sentence = input('Input lower case sentence: ')

clientSocket.send(sentence.encode())
print('Message Sent!')
modefiedMsg = clientSocket.recv(2048)
print('Reply from Server: {0}'.format(modefiedMsg.decode()))

clientSocket.close()
