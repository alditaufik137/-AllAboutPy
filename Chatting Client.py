#program client
import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222
handlerSocket.connect((serverIP,serverPort))
print ('connected to server')
while True:
	message = handlerSocket.recv(1024)
	print ('pesan dari server : ',message)
	message = input("masukkan pesan anda : ")
	handlerSocket.send(message.encode('utf-8'))
	pass
pass
