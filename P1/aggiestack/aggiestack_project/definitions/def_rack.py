import aggiestack_project.database.database_crud as db_crud



def getRacks():
    print ("***** Racks available on the server *****")
    db_crud.getRecords('rack_collection',["rack_name","rack_storage"])
            