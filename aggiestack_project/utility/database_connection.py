'''
Created on Sep 22, 2018

@author: sharm
'''
import pymongo
import json
import os

# HOST = "34.233.78.56"
# DB = "aggiestack_725002873"
# #collection = "aggiestack_725002873"


def connectMongo():
#     data = {}
#     print (os.getcwd())
#     if(os.path.isfile('./connect_db.json')):
#         data = json.load(open('./connect_db.json'))

#     if ('HOST' in data) and ('DB' in data):
#         HOST = data['HOST']
#         DB = data['DB']
#     else:
#         data['HOST'] = raw_input('Enter the host URL: ')
#         data['DB']   = raw_input('Enter the database to connect: ')
#         HOST = data['HOST']
#         DB = data['DB']
#         with open('./connect_db.json', 'w') as connect_db:
#             json.dump(data, connect_db)
        
            

    url = 'mongodb://admin:admin@cluster0-shard-00-00-v0u4h.mongodb.net:27017,cluster0-shard-00-01-v0u4h.mongodb.net:27017,cluster0-shard-00-02-v0u4h.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
    
    
    client = pymongo.MongoClient(url)
    db = client.test
    #collection = db[chatroom]
    return db