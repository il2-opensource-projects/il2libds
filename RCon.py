#!/usr/bin/env python

import socket
import urllib.parse
import logging
import re

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='log/RCon.log',
      filemode='w')

BUFFER_SIZE = 2048
TIMEOUT = 5.0

class RCon:
	def __init__(self, ip, port):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(TIMEOUT)

		try:
			self.s.connect((ip, port))
			logging.info('Connected to {ip}:{port}'.format(ip=ip, port=port))
			return
		except Exception as e:
			logging.error('Error connecting to {ip}:{port}'.format(ip=ip, port=port))
			logging.error('{error}'.format(error=str(e)))

		raise ValueError('Could not connect to DServer host!')

	def parseResponse(self, msg, fieldName):
		self.s.send(msg.encode())
		data = self.s.recv(BUFFER_SIZE)
		data = urllib.parse.unquote(data[2:].decode().replace('\x00',''))
		data = dict(urllib.parse.parse_qsl(data))

		logging.debug(msg)
		logging.debug(data)
		# Check for null fieldName (serverInput)
		if fieldName:
			return data[fieldName]
		return data

	# TODO: is there a way to reduce the repetition of code below?
	def auth(self, user, password):
		msg = '\x2c\x00auth {user} {password}\x00'.format(user=user, password=password)
		try:
			logging.info('Trying to authenticate...')
			return int(self.parseResponse(msg, 'STATUS'))
		except Exception as e:
			logging.error('Error trying to authenticate')
			logging.error('{error}'.format(error=str(e)))
			return -1

	def isAuthenticated(self):
		msg = '\x09\x00mystatus\x00'
		try:
			return int(self.parseResponse(msg, 'authed'))
		except Exception as e:
			logging.error('Error while trying to check authentication')
			logging.error('{error}'.format(error=str(e)))
			return -1

	def getConsole(self):
		msg = '\x0b\x00getconsole\x00'
		try:
			return self.parseResponse(msg, 'console')
		except Exception as e:
			logging.error('getConsole error!')
			logging.error('{error}'.format(error=str(e)))
			return -1

	def serverInput(self, MCU):
		msg = '\x14\x00serverinput {MCU}\x00'.format(MCU=MCU)
		try:
			return self.parseResponse(msg, None)
		except Exception as e:
			logging.error('serverInput error!')
			logging.error('{error}'.format(error=str(e)))
			return -1

	def getPlayerList(self):
		msg = '\x0e\x00getplayerlist\x00'
		try:
			res = self.parseResponse(msg, None)
			# Handle empty player list
			if 'playerList' in res:
				return res['playerList']
			return None
		except Exception as e:
			logging.error('getPlayerList error!')
			logging.error('{error}'.format(error=str(e)))
			return -1

	# TODO: figure out how to send a successful msg using this command
	# def openSDS(self, sds):
	# 	msg = '\x0f\x00opensds {sds}\x00'.format(sds=sds)
	# 	try:
	# 		return self.parseResponse(msg, 'STATUS')
	# 	except Exception as e:
	# 		logging.error('openSDS error!')
	# 		logging.error('{error}'.format(error=str(e)))
	# 		return -1

	# TODO: implement remaining RCon commands

	def disconnect(self):
		self.s.close()

rc = RCon('127.0.0.1', 8991)
print(rc.auth('user@host.com', 'pass'))
# print(rc.isAuthenticated())
# print(rc.getConsole())
# print(rc.serverInput('In_Test'))
# print(rc.openSDS('SDSFile'))
# print(rc.getPlayerList())
rc.disconnect()
