#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ToDo: Modify this code in order to can pass parameters when executing it.
import random as rnd
import socket

SERVER_IP = 192.168.1.100
SERVER_PORT = 41852

s = socket.socket()
s.connect((SERVER_IP, SERVER_PORT))

p = 2**11213 -1
g = 591684**635
secret = rnd.randint(2, p)
print secret
# Alice Sends Bob A = g^a mod p
A = (g**secret) % p
print "\n  Sending:" , A 

#mensaje = raw.input(A)
#s.send(mensaje)
s.send(A)

print "Paste here your's friend number", B 

# We create a ServerSocket and let it listening
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", SERVER_PORT))
s.listen(1)
sc, addr = s.accept()

B = int(sc.recv(1024))
key = (B ** secret) % p

print "Your private key is:", key 

## Now must start the chat, using the key to encrypt
