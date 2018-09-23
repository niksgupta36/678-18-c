
import aggiestack_project.utility.database_connection
import os.path
#import logger

import aggiestack_project.utility.database_crud as db_crud
#import flavor_utils

def loadHardwareList(hardwareListPath):
    print(hardwareListPath)
   # rackListPath, machineListPath = splitFile(hardwareListPath)
    #db_crud.loadList(rackListPath,["rack_name","space"],'rack_collection')
    db_crud.loadList(hardwareListPath,["hardware_name","ip","RAM","numDisks","numVcpus"],'machine_collection')

def getHardwareList():
    print ("These are the machines configured on the server")
    db_crud.getList('machine_collection')
   


