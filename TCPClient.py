from socket import *

server_name = '127.0.0.1'
server_port = 12345

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
print('Connected to Server')

sentence = input('Input lower case sentence: ')

client_socket.send(sentence.encode())
print('Message Sent!')
modefied_msg = client_socket.recv(2048)
print('Reply from Server: {0}'.format(modefied_msg.decode()))

client_socket.close()
