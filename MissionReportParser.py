#!/usr/bin/env python

import logging
import os

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='MissionReportParser.log',
      filemode='w')

class MissionReportParser:
	def __init__(self, gamePath):
		logging.info('Game path: {gamePath}'.format(gamePath=gamePath))
		self.dataPath = gamePath + '\\data'
		self.msPath = None
		self.missionReport = None
		self.findMissionReport()
		self.openMissionReport()
		self.parseMissionReport()

	def findMissionReport(self):
		try:
			logging.info('Looking for latest mission report file...')
			for filename in os.listdir(self.dataPath):
				if 'missionReport' in filename:
					# Overwrites variable until latest mission report
					# TODO: clean older reports
					# TODO: use watchdog to get latest mission report         !!!!!
					self.msPath = filename
			if self.msPath:
				logging.info('Mission Report found: ' + self.msPath)
				return
		except Exception as e:
			logging.error('findMissionReport error')
			logging.error('{error}'.format(error=str(e)))

		raise ValueError('Could not find mission report file!')

	def openMissionReport(self):
		try:
			logging.info('Opening mission report file...')
			with open(self.dataPath + '\\' + self.msPath, 'r') as file:
			    self.missionReport = file.read()
			    return
			
		except Exception as e:
			logging.error('openMissionReport error')
			logging.error('{error}'.format(error=str(e)))

		raise ValueError('Could not open mission report file!')

	def parseMissionReport(self):
		try:
			logging.info('Parsing mission report file...')
			print(self.missionReport)
			# TODO: fetch AType:12, TYPE:fake_block, COUNTRY:203 (Japan)
			# TODO: NAME will hold the variable name
			
		except Exception as e:
			logging.error('parseMissionReport error')
			logging.error('{error}'.format(error=str(e)))

		# raise ValueError('Could not open mission report file!')

lp = MissionReportParser('C:\\Program Files (x86)\\Steam\\steamapps\\common\\IL-2 Sturmovik Battle of Stalingrad')