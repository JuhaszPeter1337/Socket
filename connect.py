import socket

# socket.AF_INET     : This specifies that the socket will use the IPv4 address family.
# socket.AF_INET6    : This specifies that the socket will use the IPv6 address family.
# socket.SOCK_STREAM : This specifies that the socket will use the TCP protocol.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex(('localhost', 8888))

if result == 0:
   print("Port is open")
else:
   print("Port is not open")