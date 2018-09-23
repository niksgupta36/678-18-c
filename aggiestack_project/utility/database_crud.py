
import aggiestack_project.utility.database_connection as db_connect
from bson.objectid import ObjectId
import pprint as pp



import os


def search(key,value,list):
    return [element for element in list if element[key] == value]

def searchIndex(key,value,list):
    index = -1
    elementList = [element for element in list if element[key] == value]
    index = list.index(elementList[0])
    return index

def getList(collection_name,display = True):
    db = db_connect.connectMongo()
    collection = db[collection_name]
    message = collection.find()
    datalist = []
    for data in message:
        if display:
            for the_key, the_value in data.items():
                if not isinstance(the_value,(list,)):            ## most preferred way to check if it's list
                    print (the_key, ' : ', the_value, " | ",)
            print (datalist.append(data))    
    return datalist


def loadList(listPath,paramsList,collection_name, append=False ):
    db = db_connect.connectMongo()
    collection = db[collection_name]
    count=0
   # print(collection)
#     if not append:
#         db_connect(collection_name)
    if(os.path.isfile(listPath)):
        with open(listPath, "r") as fp:
            for i, line in enumerate(fp):
                if i == 0:
                    continue
                else:
                    count+=1
                    params = line.split()
                    post = {}
                    for i in range (len(paramsList)):
                       
                        post[paramsList[i]] = params[i]
                        
                        #print(params[i])
                        #args=params[i]
                    #print(params[0])
                    if(collection.find({"hardware_name"  : params[0]}).count()):
                        collection.remove({"hardware_name": params[0]})
                        logStr = 'Deleting previous duplicate entry for machine name: ' +  params[0] 
                        print( logStr )    
                    post_id = collection.insert_one(post).inserted_id
                   
                    #print(post_id)

            logStr = 'Successfully added '+str(count)+' new hardware configurations to the ' +  collection_name + ' collection'
            print( logStr )

    else:
        print('Invalid path, doing nothing', True)
   




