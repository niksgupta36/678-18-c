
from json import dumps

from .base import Base
from json import dumps

import aggiestack_project.utility.def_hardware as def_hardware
import os.path
from aggiestack_project.utility import def_image, def_flavor


class Admin(Base):
    """Say hello, world!"""

    def run(self):
#         print('admin, world!')
        #print(self.options)
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

        outfile = open("aggiestack-log.txt", "a+")
        outfile.write('\n')
        outfile.write('\n')
                
        if (self.options['show'] & self.options['hardware'] ):
            def_hardware.getAdminHardwareList()  

        
    
        elif (self.options['can_host']):
#             print('can_host called')
            result=def_hardware.isHardwareAvailable(self.options['<machinename>'],self.options['<flavor>'])
            outfile.write(str(result))
            print(result)

        
