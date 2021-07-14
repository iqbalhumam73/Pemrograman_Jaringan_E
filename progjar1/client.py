import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #bikin socket/kabel
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.122.37', 10000) #bikin ip sm port
server_address2 = ('192.168.122.36', 10000)
print(f"connecting to {server_address}")
print(f"connecting to {server_address2}")
sock.connect(server_address) #trus diconnect ke server
sock2.connect(server_address2)


try:
    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    print(f"sending {message}")
    sock.sendall(message.encode()) #client ngirim pesan ke server
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16) #nerima data dari server, cuma 16 bytes
        amount_received += len(data)
        print(f"{data}")
    
    message2 = 'INI ADALAH DATA YANG DIKIRIM'
    print(f"sending {message2}")
    sock2.sendall(message2.encode()) #client ngirim pesan ke server
    # Look for the response
    amount_received2 = 0
    amount_expected2 = len(message2)
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(16) #nerima data dari server, cuma 16 bytes
        amount_received2 += len(data2)
        print(f"{data2}")
finally:
    print("closing")
    sock.close()
    sock2.close()
