import aggiestack_project.database.database_connection as db_connect
import os
from builtins import str

def getRecords(collection_name, paramsList, display = True):
    outfile = open("aggiestack-log.txt", "a+")
    
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    message = collection.find()
    count=0
    for data in message:
        if display:
            for the_key, the_value in data.items():
                if not isinstance(the_value,(list,)): 

                    for param in paramsList:
                        if param == the_key:
                            count+=1
                            print (the_key, ' : ', the_value )
                            outfile.write(the_key)
                            outfile.write(' : ')
                            temp = str(the_value) 
                            outfile.write(temp)
                            outfile.write('\n')

                    
        print ("\n")
    outfile.write('\n')
    if (count is 0):
        print('0 entries found')
        outfile.write('\n')
        outfile.write('0 entries found')
        outfile.write('\n')

    outfile.write('Status : SUCCESS')
    outfile.write('\n')        

def insertRecords(listPath,paramsList,collection_name,key, offset):
    try:
        outfile = open("aggiestack-log.txt", "a+")
        outfile.write('\n')
        outfile.write('\n')
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        count=0
        if(os.path.isfile(listPath)):
            with open(listPath, "r") as fp:
#                 lines  = fp.readlines()
#                 lines = [x.strip() for x in lines] 
#             #print lines
#                  
#                 machines = lines[int(int(lines[0])+1):]
#                 for line in machines:
                for i, line in enumerate(fp):
                    if i == 0:
                        continue
                    else:
                        count+=1
                        params = line.split()
                        post = {}
                        for i in range (len(paramsList)-offset):
                       
                            post[paramsList[i]] = params[i]
                            if key == 'hardware_name':
                                    post[paramsList[6]] = params[3] # for current RAM= Original RAM when loading
                                    post[paramsList[7]] = params[4] # for current numDisks= Original numDisks when loading
                                    post[paramsList[8]] = params[5] # for current VirtualCpu= Original VirtualCpu when loading

                        if(collection.find({key  : params[0]}).count()):
                            collection.remove({key: params[0]})
                            logStr = 'Deleting previous duplicate entry for ' +key+' : '+  params[0] 
                            print( logStr )   
                            outfile.write(str(logStr))
                            outfile.write('\n')
                         
                        post_id = collection.insert_one(post).inserted_id
                   

                logStr = 'Success!! Added '+str(count)+' new configurations to the collection : ' +  collection_name 
                print( logStr )
                outfile.write(str(logStr))
                outfile.write('\n')
                outfile.write('Status : SUCCESS')

        else:
            print(listPath, ' -File not found (Invalid path)')
            outfile.write(listPath)
            outfile.write(' -File not found (Invalid path)')
            outfile.write('\n')
            outfile.write('Status : FAILURE')
    
    except Exception as e:
        print('Invalid content. One or more parameters not found. Please check the log file')
        print(e)
        outfile.write('One or more parameters not found')
        outfile.write('\n')
        outfile.write(str(e))
        outfile.write('\n')
        outfile.write('Status : FAILURE')

   
def getRecord(key,value,collection_name):
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    if(collection.find({key  : value}).count()):
        message = collection.find({key : value})
        for data in message:
            logStr = " Found value in [" + key + "] field of [" + collection_name + "]"
            return data
    else:
        logStr = " Couldn't find value in [" + key + "] field of [" + collection_name + "]"
        return None

def getServerName(collection_name):
    outfile = open("aggiestack-log.txt", "a+")
    list = []
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    message = collection.find()
    for data in message:
        list.append(data['hardware_name'])
    return list   

def insertServers(data, flavor, image,instance,collection_name):
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    collection.insert_many([{"machine_name":data,
                           "flavor_name": flavor,
                           "image_name":image,
                           "instance_name":instance}])

def insertUpdatedHardware(data, RAM, Disks,Vcpus,collection_name):
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    collection.find_one_and_update({"hardware_name": data}, 
                                  {"$set": { "Current RAM": RAM,
                                             "Current num_Disks": Disks,
                                             "Current num_Vcpus": Vcpus
                                             }
                                 })


def getInstanceName(collection_name,instance):
    outfile = open("aggiestack-log.txt", "a+")
    list = []
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    message = collection.find({"instance_name": instance})
    for data in message:
        
        list.append(data)
    return list   


def deleteInstance(collection_name,instance):
    outfile = open("aggiestack-log.txt", "a+")
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    collection.remove({"instance_name": instance})
      
def getInstances(collection_name):
    outfile = open("aggiestack-log.txt", "a+")
    list = []
    db = db_connect.connectDatabase()
    collection = db[collection_name]
    message = collection.find()
    for data in message:
        
        list.append(data)
    return list