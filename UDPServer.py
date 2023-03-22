from socket import *

server_port = 12345

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

print('The server is ready on port {0}'.format(server_port))

while True:
    msg, client_addr = server_socket.recvfrom(2048)
    print('Message from Client: {0}'.format(msg.decode()))
    modefied_msg = msg.decode().upper()
    server_socket.sendto(modefied_msg.encode(), client_addr)
    print('Modefied Message Sent!')
