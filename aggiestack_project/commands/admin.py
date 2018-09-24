'''
Created on Sep 23, 2018

@author: sharm
'''
from json import dumps

from .base import Base
from json import dumps

import aggiestack_project.utility.def_hardware as def_hardware
import os.path
from aggiestack_project.utility import def_image, def_flavor


class Admin(Base):
    """Say hello, world!"""

    def run(self):
        print('admin, world!')
        print(self.options)
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

       
                
        if (self.options['show'] & self.options['hardware'] ):
            def_hardware.getHardwareList()  

        
    
        elif (self.options['can_host']):
            print('can_host called')
            #def_hardware.isHardwareAvailable(self.options['<MACHINE_NAME>'],self.options['<FLAVOR>'])

        
