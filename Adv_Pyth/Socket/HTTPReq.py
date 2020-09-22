import socket 
#Creating a Stream Based Socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to a Web Server on port 80
my_socket.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_socket.send(command)


while True:
    #receiving 512 chars at a time
    data = my_socket.recv(512)
    #checking if the length of the data is less than 1 aka equal to 0.If there is no data that means no more connection and the stream is closed 
    if(len(data) < 1):
        break
    print(data.decode())
my_socket.close()
