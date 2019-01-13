from .base import Base
import aggiestack_project.definitions.def_hardware as def_hardware


class Admin(Base):
   

    def run(self):

        #print(self.options)

        outfile = open("aggiestack-log.txt", "a+")
        outfile.write('\n')
        outfile.write('\n')
                
        if (self.options['show'] & self.options['hardware'] ):
            def_hardware.getAdminHardwares()  

        
    
        elif (self.options['can_host']):
#             print('can_host called')
            result=def_hardware.canHost(self.options['<machinename>'],self.options['<flavor>'])
            outfile.write(str(result))
            outfile.write('\n')
            outfile.write('Status : SUCCESS')
            print(result)

        
