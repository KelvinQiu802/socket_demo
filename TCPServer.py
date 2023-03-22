from socket import *

server_port = 12345

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('The server is ready on port {0}'.format(server_port))

while True:
    # create a new socket for each connection
    connection_socket, client_addr = server_socket.accept()
    print('Listening....')
    msg = connection_socket.recv(2048).decode()
    modefied_msg = msg.upper()
    connection_socket.send(modefied_msg.encode())
    print('Modeifed Message Sent!')
    connection_socket.close()
    print('Connection Closed!')
