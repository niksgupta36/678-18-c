import aggiestack_project.database.database_crud as db_crud
from aggiestack_project.definitions import def_flavor



def insertHardware(hardware):  
    db_crud.insertRecords(hardware,["hardware_name","ip","Original RAM","Original num_Disks","Original num_Vcpus", "Current RAM", "Current num_Disks", "Current num_Vcpus"],'machine_collection','hardware_name',3)

def getHardware(hardware_name):
    return db_crud.getRecord('hardware_name',hardware_name,'machine_collection')

def getHardwareName():
    return db_crud.getServerName('machine_collection',["hardware_name"])

def getHardwares():
    print ("***** Hardware available on the server *****")
    db_crud.getRecords('machine_collection',["hardware_name","ip","Original RAM","Original num_Disks", "Original num_Vcpus"])
   
def getAdminHardwares():
    print ("**** Current Hardware available on the server ****")
    db_crud.getRecords('machine_collection',["hardware_name","ip","Original RAM","Original num_Disks","Original num_Vcpus", "Current RAM", "Current num_Disks", "Current num_Vcpus"])   
 
def canHost(machine, flavor):
   
    machine = getHardware(machine)
    flavor  = def_flavor.getFlavor(flavor)
    if(int(machine['Current RAM'])>=int(flavor['RAM']) and
       int(machine['Current num_Disks'])>=int(flavor['num_Disks']) and
       int(machine['Current num_Vcpus'])>=int(flavor['num_Vcpus']) ):
        insertUpdatedHardware(machine['hardware_name'], 
                              int(machine['Current RAM'])-int(flavor['RAM']), 
                              int(machine['Current num_Disks'])-int(flavor['num_Disks']), 
                              int(machine['Current num_Vcpus'])-int(flavor['num_Vcpus']))
        return "yes"
    else:
        return "no"

def insertUpdatedHardware(data, RAM, Disks,Vcpus):  
    db_crud.insertUpdatedHardware(data,RAM,Disks,Vcpus,'machine_collection')
