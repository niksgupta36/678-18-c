
import pymongo
import json
import os


def connectMongo():
 

    url = 'mongodb+srv://admin:admin@cluster0-v0u4h.mongodb.net/test?retryWrites=true'
    
    
    client = pymongo.MongoClient(url)
    db = client.test
    outfile = open("aggiestack-log.txt", "a+")
    outfile.write('\n')
    outfile.write(str(db))
    
    return db