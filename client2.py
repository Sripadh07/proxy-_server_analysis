import socket
host = 'localhost'
port = 8080
client_s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_s1.connect((host, port))
http_request = "GET http://example.com HTTP/1.1\r\nHost: example.com\r\n\r\n"
client_s1.send(http_request.encode())

response = client_s1.recv(1024)
while response:
    print("Received: " + response.decode())
    response = client_s1.recv(1024)
client_s1.close()