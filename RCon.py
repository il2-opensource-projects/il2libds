#!/usr/bin/env python

import socket
import urllib.parse

BUFFER_SIZE = 2048
TIMEOUT = 5.0

class RCon:
	def __init__(self, ip, port):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((ip, port))
		self.s.settimeout(TIMEOUT)
		# TODO: handle error
		print('Connected to DServer!')

	def auth(self, user, password):
		msg = '\x2c\x00auth {user} {password}\x00'.format(user=user, password=password)
		self.s.send(msg.encode())
		data = self.s.recv(BUFFER_SIZE)
		# TODO: handle error
		# TODO: parse return code
		print(data[2:].decode())

	def authenticated(self):
		msg = '\x09\x00mystatus\x00'
		self.s.send(msg.encode())
		data = self.s.recv(BUFFER_SIZE)
		# TODO: handle error
		# TODO: parse return code
		print(data[2:].decode())

	def getConsole(self):
		msg = '\x0b\x00getconsole\x00'
		self.s.send(msg.encode())
		data = self.s.recv(BUFFER_SIZE)
		# TODO: handle error
		# TODO: parse return code
		url = urllib.parse.unquote(data[2:].decode())
		print(url)

	def serverInput(self, MCU):
		msg = '\x14\x00serverinput {MCU}\x00'.format(MCU=MCU)
		self.s.send(msg.encode())
		data = self.s.recv(BUFFER_SIZE)
		# TODO: handle error
		# TODO: parse return code
		print(data[2:].decode())

	def disconnect(self):
		self.s.close()

# rc = RCon('127.0.0.1', 8991)
# rc.authenticated()
# rc.auth('user@hostname.com', 'password')
# rc.authenticated()
# rc.getConsole()
# rc.serverInput('In_Test')
# rc.disconnect()
