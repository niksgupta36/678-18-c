import aggiestack_project.database.database_crud as db_crud

def getHardwareName():
    return db_crud.getServerName('machine_collection',["hardware_name"])

def insertServer(data, flavor, image,instance):    
    db_crud.insertServers(data, flavor, image,instance, "instance_collection")

def getInstanceName(instance):
    return db_crud.getInstanceName('instance_collection',instance)

def deleteInstance(instance):
    db_crud.deleteInstance('instance_collection',instance)
    
def getInstances():
    return db_crud.getInstances('instance_collection')