import socket # importing the socket module
from _thread import * #importing functions from Low-level threading API module
import threading #This module is the Higher-level threading interface
def threadFunc(conn,address): # Function for a thread when multiple clients connect
    while True:
        data = conn.recv(1024) # receive funtion to receive data from the clients
        if not data:
            print('Disconnected from :', address[0], ':', address[1])
            break
        data = data[::-1] # STRING IS REVERSED
        conn.send(data) #send function is used to send the data to clients
    conn.close()



host = "127.0.0.1" #This is the local host address of my machine
port = 2409 #I can use any port number greater than or equal to 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# socket object is created
s.bind((host, port))#Binding the socket to the above host and port
print("socket is binded to the port ", port)
s.listen(5)#socket is listening fot client requests.
# The number 5 represents the number of client requests it can have in a queue at a time.
#For most of the systems this is the maximum value(5)
print("Socket is listening")

while True:

    conn, address = s.accept()#accept returns a connection socket object used to send and receive data
    # address is the address bound to the socket
    print('Connected to :', address[0], ':', address[1])
    start_new_thread(threadFunc, (conn,address))#This creates a new thread for every client request
s.close() #Closes the socket
