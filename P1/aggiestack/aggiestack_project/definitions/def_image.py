import aggiestack_project.database.database_crud as db_crud

def insertImages(images):
    db_crud.insertRecords(images,["image_name","image_size","path"],'image_collection', 'image_name',0)

def getImages():
    print ("**** Images available on the server ****")
    return db_crud.getInstances('image_collection')  

