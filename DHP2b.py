from socket import *
import random
import time

#create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

print("UDP Ping Server with delay is ready to receive")

while True:
   
    message, address = serverSocket.recvfrom(1024) #receive message and adderss from stocket
    delay = random.uniform(0.01, 0.02) #simualte delay
    time.sleep(delay) #add delay

    serverSocket.sendto(message, address)#send back delay
