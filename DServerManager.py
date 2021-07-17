#!/usr/bin/env python

import logging
from MissionManager import MissionManager

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='log/MissionManager.log',
      filemode='w')

class DServerManager:
    def __init__(self, gamePath):
        self.gamePath = gamePath
        self.missionManager =  MissionManager(self.gamePath)

# TODO: open window to point to game path; save info on file
# TODO: continously monitor DS status using RCon

dsManager = DServerManager('C:\\Program Files (x86)\\Steam\\steamapps\\common\\IL-2 Sturmovik Battle of Stalingrad')
