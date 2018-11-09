from .base import Base
import aggiestack_project.definitions.def_hardware as def_hardware
import aggiestack_project.definitions.def_server as def_server


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
            

        elif (self.options['show'] & self.options['instances']):
#             print('can_host called')
            res = def_server.getInstances()
#             for data in res:
            
            
            for data in res:
                listservers = []
                listservers.append("machine_name: " + data['machine_name'])
                listservers.append("instance_name: " + data['instance_name'])
                print(listservers)           

        
