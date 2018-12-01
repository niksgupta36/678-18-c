import aggiestack_project.database.database_connection as db_connect
import os
from builtins import str
import aggiestack_project.definitions.logger as logger
from aggiestack_project.functions import *

def getRecords(collection_name, paramsList, display = True):    
    try:
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
                                logger.logger(str(the_key)+ ' : '+ str(the_value))
    
                logger.logger('\n')    
            print ("\n")
        logger.logger('\n')
        if (count is 0):
            print('0 entries found')
            logger.logger('0 entries found')
    
        logger.logger('Status : SUCCESS')
    except Exception as e:
        print(e)
        logger.logger(e)    
        logger.logger('Status : FAILED')

def insertRecords(listPath,paramsList,collection_name,key, offset):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        count=0
        if(os.path.isfile(listPath)):
            with open(listPath, "r") as fp:
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
                                    post[paramsList[9]] = 'healthy' # for default machine status as healthy

                            if key == 'rack_name':
                                    post[paramsList[2]] = "healthy" # for default rack status as healthy
                                    
                        if(collection.find({key  : params[0]}).count()):
                            collection.remove({key: params[0]})
                            logStr = 'Deleting previous duplicate entry for ' +key+' : '+  params[0] 
                            print( logStr )   
                            logger.logger(str(logStr))
                         
                        post_id = collection.insert_one(post).inserted_id
                   

                logStr = 'Success!! Added '+str(count)+' new configurations to the collection : ' +  collection_name 
                print( logStr )
                logger.logger(str(logStr))
                logger.logger('Status : SUCCESS')

        else:
            print(listPath, ' -File not found (Invalid path)')
            logger.logger(listPath)
            logger.logger(' -File not found (Invalid path)')
            logger.logger('Status : FAILURE')
    
    except Exception as e:
        print('Invalid content. One or more parameters not found. Please check the log file')
        print(e)
        logger.logger('One or more parameters not found')
        logger.logger(str(e))
        logger.logger('Status : FAILURE')

   
def getRecord(key,value,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        if(collection.find({key  : value}).count()):
            message = collection.find({key : value})
            for data in message:
                return data
        else:
            return None
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE')    
        
def getServerName(collection_name):
    try:
        list = []
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        message = collection.find()
        for data in message:
            list.append(data['hardware_name'])
        return list   
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def insertServers(data, flavor, image,instance,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Data inserted into database')
        print('Data inserted into database')
        collection.insert_many([{"machine_name":data,
                               "flavor_name": flavor,
                               "image_name":image,
                               "instance_name":instance}])
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 
        
def insertUpdatedHardware(data, RAM, Disks,Vcpus,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Updated data inserted into database')
        print('Updated data inserted into database')
        collection.find_one_and_update({"hardware_name": data}, 
                                      {"$set": { "Current RAM": RAM,
                                                 "Current num_Disks": Disks,
                                                 "Current num_Vcpus": Vcpus
                                                 }
                                     })
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def updateHardwareStatus(machinename, status,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Updated hardware status inserted into database')
        print('Updated hardware status inserted into database')
        collection.find_one_and_update({"hardware_name": machinename}, 
                                      {"$set": { "machine_status": status
                                                 }
                                     })
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 
        
def updateHealthyMachine(instancename,machinename,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Updated data inserted into database')
        print('Updated data inserted into database')
        collection.find_one_and_update({"instance_name": instancename}, 
                                      {"$set": { "machine_name": machinename
                                                 }
                                     })
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 
            
def updateRackStatus(rackname, status,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Updated rack data inserted into database')
        print('Updated rack data inserted into database')
        collection.find_one_and_update({"rack_name": rackname}, 
                                      {"$set": { "rack_status": status
                                                 }
                                     })
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 
            
def getInstanceName(collection_name,instance):
    try:
        list = []
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        message = collection.find({"instance_name": instance})
        for data in message:
            list.append(data)
        return list   
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def deleteInstance(collection_name,instance):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Instance deleted : '+ instance)
        print('Instance deleted : '+ instance)
        collection.remove({"instance_name": instance})
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE')     
      
def getInstances(collection_name):
    try:
        list = []
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        message = collection.find()
        for data in message:
            list.append(data)
        return list
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def getCount(collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        return collection.count()
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def getMachineName(collection_name,rackname):
    try:
        list = []
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        message = collection.find({"rack_name": rackname})
        for data in message:
            list.append(data)
        return list
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 
        
def getFlavorName(collection_name,machinename):
    try:
        list = []
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        message = collection.find({"machine_name": machinename})
        for data in message:
            list.append(data)
        return list
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE') 

def deleteHardware(collection_name,machine):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        collection1 = db["instance_collection"]
        logger.logger('Machine deleted : '+ machine)
        print('Machine deleted : '+ machine)
        collection.remove({"hardware_name": machine})
        collection1.remove({"machine_name": machine})
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE')     
    
    
def insertHardwareByCommand(hardware_name, rack_name, ip, Original_RAM, Original_num_Disks, Original_num_Vcpus, machine_status,collection_name):
    try:
        db = db_connect.connectDatabase()
        collection = db[collection_name]
        logger.logger('Machine data inserted into database')
        print('Machine data inserted into database')
        collection.insert_many([{"hardware_name":hardware_name,
                               "Current RAM": Original_RAM,
                               "Current num_Disks":Original_num_Disks,
                               "Current num_Vcpus":Original_num_Vcpus,
                               "machine_status": machine_status,
                               "rack_name":rack_name,
                               "ip":ip,
                               "Original RAM": Original_RAM,
                               "Original num_Disks":Original_num_Disks,
                               "Original num_Vcpus":Original_num_Vcpus}])
    except Exception as e:
        print(e)
        logger.logger(e)
        logger.logger('Status : FAILURE')     
