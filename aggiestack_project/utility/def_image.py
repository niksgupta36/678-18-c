'''
Created on Sep 23, 2018

@author: sharm
'''
import aggiestack_project.utility.database_connection
import os.path
#import logger

import aggiestack_project.utility.database_crud as db_crud

def loadImageList(imageListPath):
    db_crud.loadList(imageListPath,["image_name","path"],'image_collection')

def getImageList():
    print ("These are the images configured on the server")
    db_crud.getList('image_collection')  

# def getImage(image):
#     return database.getItem('image_name',image,'image_collection')


# def clearImageList():
#     database.clearList('image_collection')

# def isValidImage(image):
#     return database.isAvailable('image_name',image,'image_collection')