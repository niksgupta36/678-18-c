'''
Created on Sep 23, 2018

@author: sharm
'''
import aggiestack_project.utility.database_connection
import os.path
#import logger

import aggiestack_project.utility.database_crud as db_crud

def loadImageList(imageListPath):
    db_crud.loadList(imageListPath,["image_name","path"],'image_collection', 'image_name',0)

def getImageList():

#     print ("These are the images configured on the server")
    db_crud.getList('image_collection',["image_name","path"])  

