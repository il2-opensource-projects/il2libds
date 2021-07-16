#!/usr/bin/env python

import logging
import os
import sys
import time
import logging
import re 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='MissionReportParser.log',
      filemode='w')

class MissionReportParser:
	def __init__(self, gamePath, flagHandler):
		logging.info('Game path: {gamePath}'.format(gamePath=gamePath))
		self.dataPath = gamePath + '\\data'
		self.flagHandler = flagHandler
		self.observer = Observer()

	def run(self):
		event_handler = MissionReportHandler(self.flagHandler)
		self.observer.schedule(event_handler, self.dataPath, recursive=False)
		self.observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			self.observer.stop()
		self.observer.join()

	def stop(self):
		self.observer.stop()
		self.observer.join()

class MissionReportHandler(FileSystemEventHandler):
  	def __init__(self, flagHandler):
  		self.flagHandler = flagHandler

  	def on_created(self, event):
  		if event.is_directory:
  			return None
  		elif event.event_type == 'created':
  			msPath = event.src_path
  			if 'missionReport' in msPath and '.txt' in msPath:
  				logging.info('Mission Report created: ' + msPath)
  				# Opens the file and parses the flags, if any
  				try:
  					with open(msPath, 'r') as file:
  						report = file.readlines()
  					for r in report:
  						match = re.findall('fake_block.*COUNTRY:203 NAME:(\\S*)', r)
  						if len(match) > 0:
  							logging.info('Flag found: ' + match[0])
  							# Finally calls flag handler function
  							self.flagHandler(match[0].replace('\\n', ''))
  					# Keeps the folder clean of mission report files
  					os.remove(msPath) 
  				except Exception as e:
  					logging.error('handleNewMissionReport error')
  					logging.error('{error}'.format(error=str(e)))

def test(missionReport):
	print("flagHandler: " + missionReport)

mrParser = MissionReportParser('C:\\Program Files (x86)\\Steam\\steamapps\\common\\IL-2 Sturmovik Battle of Stalingrad', test)
mrParser.run()