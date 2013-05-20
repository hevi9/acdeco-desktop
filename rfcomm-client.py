from bluetooth import *

server_address = "78:DD:08:A8:14:4E"
port = 1

sock = BluetoothSocket( RFCOMM )
sock.connect((server_address, port))

sock.send("hello!!")

sock.close()
