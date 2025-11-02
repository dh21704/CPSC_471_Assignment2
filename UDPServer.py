import random
import time
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Server is ready to receive")

while True:
    # Receive message and client address
    message, clientAddress = serverSocket.recvfrom(1024)

    # Simulate random packet loss (10%)
    if random.random() < 0.1:
        print("Packet lost")
        continue

    # Simulate delay between 10ms and 20ms
    delay = random.uniform(0.01, 0.02)
    time.sleep(delay)

    # Send the same message back (pong)
    serverSocket.sendto(message, clientAddress)
    print(f"Replied to {clientAddress} with {message.decode()} after {delay*1000:.2f} ms")
