import socket #Importing the socket module

host = '127.0.0.1'
port = 2409

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

message = input("Enter a String: ") #Input through the keyboard
while message != 'exit':# When typed exit, disconnets frorm the server
	s.send(message.encode())    #converting unicode string to bytes object data.
	data = s.recv(1024).decode() #converting the bytes object data back to unicode string
	print('Reversed string from server:' + data)
	message = input("Enter a String: ")
s.close()
