from socket import *
import random
import time

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

print("UDP Ping Server with delay and loss is ready to receive")

while True:
    # Receive message from client
    message, address = serverSocket.recvfrom(1024)

    # Simulate 10–20 ms delay
    delay = random.uniform(0.01, 0.02)
    time.sleep(delay)

    # Simulate 10% packet loss
    if random.random() < 0.1:
        continue  # Skip sending the reply

    # Send the message back
    serverSocket.sendto(message, address)
