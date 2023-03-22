from socket import *

server_name = '127.0.0.1'
server_port = 12345

client_socket = socket(AF_INET, SOCK_DGRAM)
msg = input('Input lowercase sentence: ')
client_socket.sendto(msg.encode(), (server_name, server_port))
print('Request Sent!')

modefied_msg, server_addr = client_socket.recvfrom(2048)
print('Reply from Server: {0}'.format(modefied_msg.decode()))

client_socket.close()
