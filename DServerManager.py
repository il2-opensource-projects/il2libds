#!/usr/bin/env python

import logging
import multiprocessing as mp
import subprocess

from MissionManager import MissionManager

logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(levelname)s: %(message)s',
      filename='log/DServerManager.log',
      filemode='w')

class DServerManager:
    def __init__(self, gamePath):
        self.gamePath = gamePath
        self.dsPath = self.gamePath + '\\bin\\game\\DServer.exe'
        self.run()
        self.missionManager =  MissionManager(self.gamePath)
        self.dspid = 0

    def startDS(self):
        process = subprocess.call([self.dsPath])

    def run(self):
        p = mp.Process(target=self.startDS)
        p.start()
        dspid = p.pid

# TODO: open window to point to game path; save info on file
# TODO: continously monitor DS status using RCon
if __name__ == '__main__':
    gamePath = 'E:\\SteamLibrary\\steamapps\\common\\IL-2 Sturmovik Battle of Stalingrad'
    dsManager = DServerManager(gamePath)
