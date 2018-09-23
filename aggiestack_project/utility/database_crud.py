'''
Created on Sep 22, 2018

@author: sharm
'''

import aggiestack_project.utility.database_connection as db_connect
from bson.objectid import ObjectId
import pprint as pp

#import logger

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
            for the_key, the_value in data.iteritems():
                if not isinstance(the_value,(list,)):            ## most preferred way to check if it's list
                    print the_key, ' : ', the_value, " | ",
            print 
        datalist.append(data)    
    return datalist


def loadList(listPath,paramsList,collection_name, append=False ):
    db = db_connect.connectMongo()
    collection = db[collection_name]
   




