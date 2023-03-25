import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serveraddress = (serverIP,serverPORT)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = 'Hi My Name is Yashvardhan Sharma, 2022B1PS1145P'

bytestosend = str.encode(message)

UDPClientSocket.sendto(bytestosend,serveraddress)