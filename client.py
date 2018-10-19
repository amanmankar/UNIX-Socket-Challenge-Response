import sys
import socket
import os
import struct
import hashlib

s = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
server_address = '/run/secret/secret.sock'
s.connect(server_address)
u=b'\x75\x73\x65\x72\x32\x34' #username (user24) converted to hex
ulen=struct.pack('>I',6)
con=ulen+u
s.send(con)
nonce=s.recv(512)

pad="1234855270845859652397297455100036310340236178342887620229"

n=""
while n[:6]!="000000":
    v=u+nonce+pad
    n=hashlib.sha256(v).hexdigest()
    pad=str(int(pad)+1)

print "Digest with starting 3 bytes zeros: "+n
s.send(v)
secret=s.recv(512)
print "The Secret is:"+secret
