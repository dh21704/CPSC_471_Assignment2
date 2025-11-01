from socket import *
import time

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # 1 second timeout

serverName = 'localhost'
serverPort = 12000

for i in range(10):
    message = f"Ping {i+1} {time.time()}"
    start = time.time()
    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        end = time.time()
        rtt = (end - start) * 1000  # Convert to ms
        print(f"Reply from {serverName}: {modifiedMessage.decode()} RTT = {rtt:.2f} ms")
    except timeout:
        print("Request timed out")

clientSocket.close()
