from socket import *
import random
import time

#create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

print("UDP Ping Server with delay and loss is ready to receive")

while True:
    message, address = serverSocket.recvfrom(1024) #create message from socket
    delay = random.uniform(0.01, 0.02) #simulate a 10-20second delay
    time.sleep(delay) #add delay

    #if 10% packe tloss
    if random.random() < 0.1:
        continue #skip sending the reply

    serverSocket.sendto(message, address)#send message back
