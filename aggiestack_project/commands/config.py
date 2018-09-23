'''
Created on Sep 22, 2018

@author: sharm
'''



from json import dumps

from .base import Base

import aggiestack_project.utility.def_hardware as def_hardware
import os.path

class Config(Base):
    """Say hello, world!"""

    def run(self):
        print('config, world!')
        #print(self.options)
        if(self.options['--images']):
            image_list_path =  self.options['--images']
            #image_utils.loadImageList(image_list_path)
        elif(self.options['--flavors']):
            flavor_list_path =  self.options['--flavors']
            #flavor_utils.loadFlavorList(flavor_list_path)
        elif(self.options['--hardware']):
            hardware_list_path =  self.options['--hardware']
            def_hardware.loadHardwareList(hardware_list_path)
        
