'''
Created on Sep 22, 2018

@author: sharm
'''
from .base import Base
from json import dumps
from aggiestack_project.utility import def_image, def_flavor, def_hardware, logger

class Show(Base):
    """Say hello, world!"""

    def run(self):
        print('show, world!')
        #print(self.options)
        if(self.options['images']):
            def_image.getImageList()
        elif(self.options['flavors']):
            def_flavor.getFlavorList()
        elif(self.options['hardware']):
            def_hardware.getHardwareList()
        elif(self.options['logs']):
            logger.getLogs()
#         elif(self.options['instances'] and self.options['show']):
#             instance_utils.getInstanceList()
#         elif(self.options['hardware'] and self.options['show']):
#             def_hardware.getInstanceList()
        elif(self.options['all']):
            print('\nImages : \n')
            def_image.getImageList()
            print('\nFlavors : \n')
            def_flavor.getFlavorList()
            print('\nHardware: \n')
            def_hardware.getHardwareList()
            print('\nLogs: \n')
            logger.getLogs()
        else:
            logger.log("Invalid parameter",True)