from socket import *
import random
import time

# create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

print("UDP Ping Server with delay is ready to receive")

while True:
    
    message, address = serverSocket.recvfrom(1024) #receieve client messages and address
    delay = random.uniform(0.01, 0.02) #simulate 10-20ms network delay
    time.sleep(delay) #time delay

    serverSocket.sendto(message, address) #send back same message
