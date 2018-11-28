from .base import Base
from aggiestack_project.definitions import def_hardware, def_server, def_flavor
import aggiestack_project.definitions.logger as logger
from aggiestack_project.definitions.logger import loggerlist

class Server(Base):
   

    def run(self):
        
#         outfile = open("aggiestack-log.txt", "a+")
        logger('\n')
        logger('\n')
        if (self.options['create'] ):
            
            result=(def_server.getHardwareName()) 
            image = self.options['<imagename>']
            instance = self.options['<instancename>']
            for data in result:
                if def_hardware.canHost(data,self.options['<flavor>'])=='yes':
                    def_server.insertServer(data, self.options['<flavor>'], image,instance)
                    print("Server created!")
                    logger('Server created!')
                    break;
            
        if (self.options['delete'] ):
            
            
            instance = self.options['<instancename>']
            instancedata= def_server.getInstanceName(instance)
            flavor = ""
            machine = ""
            for data in instancedata:
                flavor = data['flavor_name']
                machine = data['machine_name']
            machineinfo = def_hardware.getHardware(machine)
          
            flavor = (def_flavor.getFlavor(flavor))
            
            
            def_hardware.insertUpdatedHardware(machineinfo['hardware_name'], 
                              int(machineinfo['Current RAM'])+int(flavor['RAM']), 
                              int(machineinfo['Current num_Disks'])+int(flavor['num_Disks']), 
                              int(machineinfo['Current num_Vcpus'])+int(flavor['num_Vcpus']))
            
            
            def_server.deleteInstance(instance)
            
        
        if (self.options['list'] ):
            res = def_server.getInstances()
#             outfile = open("aggiestack-log.txt", "a+")
            logger('\n')
            logger('\n')
            if res == []:
                print('No server to list')
                
                logger('No server to list')
                
            for data in res:
                listservers = []
                listservers.append("instance_name: " + data['instance_name'])
                listservers.append("flavor_name: " + data['flavor_name'])
                listservers.append("image_name: " + data['image_name'])
                loggerlist(listservers)
                print(listservers)
                
            

                
       
   
    


        
