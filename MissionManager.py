#!/usr/bin/env python

import logging
from MissionReportParser import MissionReportParser

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='log/MissionManager.log',
      filemode='w')

class MissionManager:

    def __init__(self, gamePath):
        self.gamePath = gamePath
        self.mrParser =  MissionReportParser(self.gamePath, self.flagHandler)
        self.mrParser.run()

    # TODO: import modules according to mission name
    # TODO: erase method below
    def flagHandler(missionReport):
        print("flagHandler: " + missionReport)

    def handleMissionChange(self, missionPath):
        print('handleMissionChange: ' + missionPath)


missionManager = MissionManager('C:\\Program Files (x86)\\Steam\\steamapps\\common\\IL-2 Sturmovik Battle of Stalingrad')
