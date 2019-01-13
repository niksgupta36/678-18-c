import aggiestack_project.database.database_crud as db_crud
import os.path

from aggiestack_project.definitions import def_flavor
from aggiestack_project.definitions import def_rack
import aggiestack_project.definitions.logger as logger




def insertHardware(hardware):  
    try:
        if(os.path.isfile(hardware)):
            with open(hardware, "r") as fp:
                lines  = fp.readlines()
                lines = [x.strip() for x in lines] 
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
                db_crud.insertRecords(machineListPath,["hardware_name","rack_name","ip","Original RAM","Original num_Disks","Original num_Vcpus", "Current RAM", "Current num_Disks", "Current num_Vcpus", "machine_status"],'machine_collection','hardware_name',4)        
                db_crud.insertRecords(rackListPath,["rack_name","rack_storage","rack_status"],'rack_collection', 'rack_name',1);
        else:
            print('File not found (Invalid path)')
            logger.logger('File not found (Invalid path)')
            logger.logger('Status : FAILURE')
                    
    except Exception as e:
        print(e)
        
def getHardware(hardware_name):
    return db_crud.getRecord('hardware_name',hardware_name,'machine_collection')

def getHardwareName():
    return db_crud.getServerName('machine_collection')

def getHardwares():
    print ("***** Hardware available on the server *****")
    print("Total: "+ str(db_crud.getCount('machine_collection')))
    logger.logger("Total: "+ str(db_crud.getCount('machine_collection')))
    db_crud.getRecords('machine_collection',["hardware_name","rack_name","ip","Original RAM","Original num_Disks", "Original num_Vcpus"])
   
def getAdminHardwares():
    print ("**** Current Hardware available on the server ****")
    db_crud.getRecords('machine_collection',["hardware_name","ip","Original RAM","Original num_Disks","Original num_Vcpus", "Current RAM", "Current num_Disks", "Current num_Vcpus"])   
 
def canHost(machine, flavor):
    machine = getHardware(machine)
    flavor  = def_flavor.getFlavor(flavor)
    if(int(machine['Current RAM'])>=int(flavor['RAM']) and
       int(machine['Current num_Disks'])>=int(flavor['num_Disks']) and
       int(machine['Current num_Vcpus'])>=int(flavor['num_Vcpus']) and 
       machine['machine_status'] == 'healthy'):
        insertUpdatedHardware(machine['hardware_name'], 
                              int(machine['Current RAM'])-int(flavor['RAM']), 
                              int(machine['Current num_Disks'])-int(flavor['num_Disks']), 
                              int(machine['Current num_Vcpus'])-int(flavor['num_Vcpus']))
        return "yes"
    else:
        return "no"

def insertUpdatedHardware(data, RAM, Disks,Vcpus):  
    db_crud.insertUpdatedHardware(data,RAM,Disks,Vcpus,'machine_collection')
    
def getInstances():
    return db_crud.getInstances("machine_collection")

def updateHardwareStatus(machinename, status):
    db_crud.updateHardwareStatus(machinename, status, "machine_collection")
    
def getMachineName(rackname):
    return db_crud.getMachineName("machine_collection", rackname)

def deleteHardware(machine):
    db_crud.deleteHardware("machine_collection", machine)
    
def insertHardwareByCommand(hardware_name, rack_name, ip, Original_RAM, Original_num_Disks, Original_num_Vcpus, machine_status):
    db_crud.insertHardwareByCommand(hardware_name, rack_name, ip, Original_RAM, Original_num_Disks, Original_num_Vcpus, machine_status,'machine_collection')
    