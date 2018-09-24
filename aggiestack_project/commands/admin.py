

from .base import Base
import aggiestack_project.utility.def_hardware as def_hardware


class Admin(Base):
   

    def run(self):
#       print('admin, world!')
        #print(self.options)

        outfile = open("aggiestack-log.txt", "a+")
        outfile.write('\n')
        outfile.write('\n')
                
        if (self.options['show'] & self.options['hardware'] ):
            def_hardware.getAdminHardwareList()  

        
    
        elif (self.options['can_host']):
#             print('can_host called')
            result=def_hardware.isHardwareAvailable(self.options['<machinename>'],self.options['<flavor>'])
            outfile.write(str(result))
            outfile.write('\n')
            outfile.write('Status : SUCCESS')
            print(result)

        
