import aggiestack_project.database.database_crud as db_crud



def getRacks():
    print ("***** Racks available on the server *****")
    print(db_crud.getCount('rack_collection'))
    db_crud.getRecords('rack_collection',["rack_name","rack_storage"])
            
def getInstances():
    return db_crud.getInstances("rack_collection")