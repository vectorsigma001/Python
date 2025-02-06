## All Programs 
```text
1. get hostname and remote host name 
2. convert IPv4 address to different formats 
3. using port number get network service
4. convert network byte order to host byte order and vice versa
5. set and get default socket timeout 
6. Modifying a socket's send/receive buffer
sizes
7. his Python script creates a simple TCP server that listens
 for incoming connections on 127.0.0.1 (localhost). It continuously
 waits for client connections and handles them one by one.
8. Reusing socket addresses
9. print the current time from the internet time server 
using NTP server 
10. Write your own sntp server 
11. Write a simple TCP echo client/server application
12. Write a simple UDP echo client/server application
```

## 1. get hostname and remote host name 
```python
import socket 
host_name = socket.gethostname()
print(host_name)
print(socket.gethostbyname(host_name))
remote_host = 'www.python.org'
print(remote_host)
print(socket.gethostbyname(remote_host))
```

Description
```text
hostname given when you configure your OS
 also where your python intepreter is running 
gethostname() 
gethostbyname() 
remotehost , ip needed 
```

## 2. convert IPv4 address to different formats 
```python
import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)  # Use packed_ip_addr here
        print("%s %s, %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

convert_ip4_address()
```

Description
```text
hexlify: binary to hexadecimal 
inet_aton: converts ip into binary form 
inet_ntoa: converts ip into dotted decimal string
```

## 3. using port number get network service
```python
import socket 
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port %s => service name: %s" %(port, socket.getservbyport(port,protocolname)))
        print("Port: >%s => service name: %s" %(53, socket.getservbyport(53, 'udp')))
    
find_service_name()

# Port 80 => service name: http, 80 port is used by http services
# Port: >53 => service name: domain, 53 port is used by domain services 
# Port 25 => service name: smtp, 25 port is used by smtp services
# Port: >53 => service name: domain, 53 port is used by domain services 
```

Description
```text
which port is taken by what network services 
also what protocol do these port are using
TCP or UDP protocol 
```

## 4. convert network byte order to host byte order and vice versa
```python
import socket 
def convert_integer():
    data = 1234 
    # 32-bit 
    print("Original: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data)))
    # 16-bit 
    print("Original: %s => Short host bute order: %s,Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data)))

convert_integer()
```

Description
```text
convert network byte order to host byte order 
and vice-versa 
ntohl: translates a long integer from network byte
 order to host byte order 
htonl: converts an unsigned long integer from the
 host byte order to network byte order 
ntohs:  used to convert a 16-bit unsigned integer
 from network byte order to host byte order 
htons: converts an unsigned short integer (16-bit)
 from the host byte order to the network byte 
order
```

## 5. set and get default socket timeout 
```python
import socket
def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" %s.gettimeout())# get the default timeout 
    s.settimeout(100) # set the default tim eout
    print("Current socket timeout: %s" %s.gettimeout())

test_socket_timeout()
```

Description
```text
this function creates a new socket
s = socket.socket() 
socket.AF_INET: specifies the address family as IPV4 
socket.SOCK_STREAM: specifies the socket as TCP socket 
```

## 6. Modifying a socket's send/receive buffer sizes
```python
import socket

# Define buffer sizes
SEND_BUF_SIZE = 4096  # Send buffer size in bytes
RECV_BUF_SIZE = 4096  # Receive buffer size in bytes

def modify_buff_size():
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the current send buffer size
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before]: %d bytes" % bufsize)

    # Set new buffer sizes
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    # Get the new send buffer size after modification
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]: %d bytes" % bufsize)

    # Close the socket
    sock.close()

# Run the function when the script is executed
if __name__ == '__main__':
    modify_buff_size()
```

Description
```text
A buffer is a temporary storage area used to hold data while
 it is being transferred between two places. It helps manage
 differences in data processing speeds.
SOL_SOCKET: tells we are configuring general socket settings
SO_SNDBUF: how much buffer to send
SO_SNDBUF: Sets the send buffer size.
SO_RCVBUF: Sets the receive buffer size
SEND_BUF_SIZE: The desired size for the send buffer.
RECV_BUF_SIZE: The desired size for the receive buffer.
```

## 7. this Python script creates a simple TCP server that listens for incoming connections on 127.0.0.1 (localhost). It continuously waits for client connections and handles them one by one.
```python
import socket
import time 

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set blocking mode (1 means blocking mode is enabled)
    s.setblocking(1)

    # Set timeout for socket operations (0.5 seconds)
    s.settimeout(0.5)

    # Bind to an available port on localhost
    s.bind(("127.0.0.1", 0))

    # Get the assigned address and port
    socket_address = s.getsockname()
    print("Trivial Server launched on socket:", socket_address)

    # Start listening for connections (max 1 pending connection)
    s.listen(1)

    while True:
        try:
            conn, addr = s.accept()  # Accept client connection
            print("Connection established with:", addr)
            time.sleep(10)
            conn.close()  # Close the connection
        except socket.timeout:
            print("No connection, waiting...")

if __name__ == '__main__':
    test_socket_modes()
```

## 8. Reusing socket addresses
```python
import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old sock state: %s" % old_state)
    
    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New sock state: %s" % new_state)
    
    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    
    print("Listening on port: %s" % local_port)
    
    while True:
        try:
            connection, addr = srv.accept()
            print("Connected by %s:%s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            break
        except socket.error as msg:
            print("%s" % msg)

if __name__ == '__main__':
    reuse_socket_addr()
```

Description
```text
- SO_REUSEADDR: The SO_REUSEADDR socket option
 allows a socket to forcibly bind to a port in use by another socket- 
- getsocketopt: used to retrieve the current value of a specific socket
 option associated with a given socket
```

## 9. print the current time from the internet time server using NTP server 
```python
import ntplib
from time import ctime 
def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()
```

Description
```text
ntplib interacts Network Time Protocol (NTP) servers to fetch accurate
 time information over the internet.
send a request to an NTP server to get the current time. The parameter
 'pool.ntp.org' refers to a public NTP
 server that you are connecting to.
The ctime() function is used to convert a timestamp (which is the number 
of seconds since the Unix epoch) into a human-readable 
string format.
```

## 10. Write your own sntp server 
```python
import sys
import time
import socket
import struct

NTP_SERVER = "0.uk.pool.ntp.org"  # Fixed typo
TIME1970 = 2208988800

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'  # Send correct binary data
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    
    if data:
        print('Response received from:', address)
    
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

sntp_client()
```

Description
```text
creates a UDP socket (SOCK_DGRAM), which is typically used for lightweight 
communication where reliability is not a concern, 
such as SNTP. AF_INET indicates the use of IPv4.
- create a binary data and send it to the ntp server with 123 port number
- the data is received and stored in the data variable. The address variable
 holds the server's address.
- struct.unpack method to unpack the binary response. The format string !12I means:
!: Network byte order (big-endian).
12I: 12 unsigned integers (4 bytes each). The NTP packet contains 12 32-bit integers,
 and the time is stored in the 10th integer (index 10).
- The NTP time is in seconds since 1900, while Unix time is in seconds since 1970. 
Subtracting TIME1970 converts the NTP time to Unix time.
```

## 11. Write a simple TCP echo client/server application

server.py
```python
import socket
import argparse

host = 'localhost'
data_payload = 2048  # Max data size
backlog = 5  # Max queued connections

def echo_server(port):
    """A simple TCP echo server."""
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enable reuse of the address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the address and port
    server_address = (host, port)
    print("Starting echo server on %s port %s" % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(backlog)

    while True:
        print("Waiting for a client connection...")
        client, address = sock.accept()
        print(f"Connection from {address}")

        data = client.recv(data_payload)
        if data:
            print("Received: %s" % data.decode('utf-8'))
            client.sendall(data)  # Send data back
            print("Sent back to client.")

        # Close client connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP Echo Server')
    parser.add_argument('--port', required=True, type=int, help='Port to listen on')
    args = parser.parse_args()
    echo_server(args.port)
```

client.py
```python
import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    """A simple echo client."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to {} port {}".format(*server_address))

    try:
        sock.connect(server_address)
        message = "Hello, server!"
        print("Sending: {}".format(message))
        sock.sendall(message.encode('utf-8'))

        # Receive response
        data = sock.recv(1024)
        print("Received: {}".format(data.decode('utf-8')))
    
    except socket.error as e:
        print("Socket error: {}".format(str(e)))

    finally:
        print("Closing connection")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, default=9999)  # Default port added
    given_args = parser.parse_args()
    port = given_args.port

    echo_client(port)
```

Description
```text
server.py
- create a tcp socket 
- socket enable reuse of the address/ port 
- bind the socket with 'localhost' '9999'
- means that the socket will listen on the specified address 
and port 
- wait for the incoming connections
- recv(1024) means you can receive 1024 bytes 
```

## 12. Write a simple UDP echo client/server application

udp_client.py
```python
import socket
import argparse

def echo_client(port):
    """A simple UDP echo client."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
    server_address = ('localhost', port)
    
    message = "Hello, this is a test message!"
    
    try:
        print("Sending: {}".format(message))
        sent = sock.sendto(message.encode('utf-8'), server_address)  # Send message
        
        data, server = sock.recvfrom(2048)  # Receive response
        print("Received: {}".format(data.decode()))

    finally:
        print("Closing connection")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Echo Client")
    parser.add_argument("--port", type=int, required=True, help="Port to connect to")
    args = parser.parse_args()
    
    echo_client(args.port)
```

udp_server.py
```python
import socket
import argparse

def echo_server(port):
    """A simple UDP echo server."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
    server_address = ('localhost', port)
    
    print("Starting UDP echo server on {} port {}".format(*server_address))
    sock.bind(server_address)

    while True:
        print("Waiting to receive message from client...")
        data, address = sock.recvfrom(2048)  # Receive data from client
        print("Received {} bytes from {}: {}".format(len(data), address, data.decode()))

        if data:
            sent = sock.sendto(data, address)  # Echo data back to client
            print("Sent {} bytes back to {}".format(sent, address))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP Echo Server")
    parser.add_argument("--port", type=int, required=True, help="Port to listen on")
    args = parser.parse_args()
    
    echo_server(args.port)
```

Description
```text
- create a udp socket 
```

Link to read in more better way 
```text
https://excalidraw.com/#json=WhsHAcS-FlIFGhkX5noNn,02cRQUIEOfIEjrCIU6dIhw
```

