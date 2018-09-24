


import aggiestack_project.utility.database_crud as db_crud
from aggiestack_project.utility import def_flavor


def loadHardwareList(hardwareListPath):
#     print(hardwareListPath)
  
    db_crud.loadList(hardwareListPath,["hardware_name","ip","Original RAM","Original numDisks","Original numVcpus", "Current RAM", "Current numDisks", "Current numVcpus"],'machine_collection','hardware_name',3)

def getHardware(machine_name):
    return db_crud.getItem('hardware_name',machine_name,'machine_collection')

def getHardwareList():
    print ("***** Hardware configured on the server *****")
    db_crud.getList('machine_collection',["hardware_name","ip","Original RAM","Original numDisks", "Original numVcpus"])
   
def getAdminHardwareList():
    print ("**** Current Hardware configured on the server ****")
    db_crud.getList('machine_collection',["hardware_name","ip","Original RAM","Original numDisks","Original numVcpus", "Current RAM", "Current numDisks", "Current numVcpus"])   
 
def isHardwareAvailable(machine_name, flavor_name):
   
    machine = getHardware(machine_name)
    flavor  = def_flavor.getFlavor(flavor_name)
    if(int(machine['Current RAM'])>=int(flavor['RAM']) and
       int(machine['Current numDisks'])>=int(flavor['numDisks']) and
       int(machine['Current numVcpus'])>=int(flavor['numVcpus']) ):
        #logger.log('Can host instance')
       
        return "yes"
    else:
        #logger.log('Cannot host instance')
        return "no"
