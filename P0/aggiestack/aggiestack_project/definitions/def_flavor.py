import aggiestack_project.database.database_crud as db_crud

def insertFlavors(flavorListPath):
    db_crud.insertRecords(flavorListPath,["flavor_name","RAM","num_Disks","num_Vcpus"],'flavor_collection','flavor_name',0)

def getFlavors():
    print ("**** Flavors available on the server ****")
    db_crud.getRecords('flavor_collection',["flavor_name","RAM","num_Disks","num_Vcpus"])  
def getFlavor(flavor):
    return db_crud.getRecord('flavor_name',flavor,'flavor_collection')
