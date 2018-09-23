'''
Created on Sep 22, 2018

@author: sharm
'''

from json import dumps

from .base import Base
from json import dumps

import aggiestack_project.utility.def_hardware as def_hardware
import os.path
from aggiestack_project.utility import def_image, def_flavor

class Config(Base):
    """Say hello, world!"""

    def run(self):
        print('config, world!')
        #print(self.options)
        if(self.options['--images']):
            #image_list_path =  self.options['--images']
            image_list_path=(self.options['<filename>'])
            def_image.loadImageList(image_list_path)
        elif(self.options['--flavors']):
            #flavor_list_path =  self.options['--flavors']
            flavor_list_path=(self.options['<filename>'])
            def_flavor.loadFlavorList(flavor_list_path)
        elif(self.options['--hardware']):
            print("hardware***")
            #hardware_list_path =  self.options['--hardware']
           # print(self.args)
            #print(self.kwargs)
            hardware_list_path=(self.options['<filename>'])
            def_hardware.loadHardwareList(hardware_list_path)
        
