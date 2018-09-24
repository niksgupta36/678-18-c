
import pymongo
import json
import os


def connectMongo():
 

    url = 'mongodb+srv://admin:admin@cluster0-v0u4h.mongodb.net/test?retryWrites=true'
    
    
    client = pymongo.MongoClient(url)
    db = client.test
    outfile = open("aggiestack-log.txt", "a+")
    outfile.write('\n')
    outfile.write('Connection to database is successful!')
    outfile.write('\n')
    outfile.write('\n')
    return db