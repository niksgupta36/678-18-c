'''
Created on Sep 22, 2018

@author: sharm
'''
import aggiestack_project.utility.database_connection
import os.path
#import logger

import aggiestack_project.utility.database_crud as db_crud
#import flavor_utils

def loadHardwareList(hardwareListPath):
    rackListPath, machineListPath = splitFile(hardwareListPath)
    db_crud.loadList(rackListPath,["rack_name","space"],'rack_collection')
    db_crud.loadList(machineListPath,["hardware_name","rack_name","ip","RAM","numDisks","numVcpus"],'machine_collection')

def getHardwareList():
    print ("These are the machines configured on the server")
    db_crud.getList('machine_collection')
    print ("These are the racks configured on the server")
    db_crud.getList('rack_collection')


def splitFile(hardwareListPath):
    if(os.path.isfile(hardwareListPath)):
        with open(hardwareListPath, "r") as fp:
            lines  = fp.readlines()
            lines = [x.strip() for x in lines] 
            #print lines
            racks = lines[0:int(lines[0])+1]
            machines = lines[int(int(lines[0])+1):]
            rackListPath = './racks.txt'
            machineListPath = './machines.txt'
            with open(rackListPath, "w") as rackfile:
                for rack in racks:
                    rackfile.write("%s\n" % rack)
            with open(machineListPath, "w") as machinefile:
                for machine in machines:
                    machinefile.write("%s\n" % machine)
            return rackListPath, machineListPath
            


    

















    
