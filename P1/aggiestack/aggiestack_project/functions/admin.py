from .base import Base
import aggiestack_project.definitions.def_hardware as def_hardware
import aggiestack_project.definitions.def_server as def_server
from aggiestack_project.definitions import def_rack
import aggiestack_project.definitions.logger as logger


class Admin(Base):
   

    def run(self):

#         outfile = open("aggiestack-log.txt", "a+")
        logger('\n')
        logger('\n')
        
        if (self.options['show'] & self.options['hardware'] ):
            def_hardware.getAdminHardwares()  
    
        elif (self.options['can_host']):
            result=def_hardware.canHost(self.options['<machinename>'],self.options['<flavor>'])
            logger.logger(str(result))
            logger.logger('\n')
            logger.logger('Status : SUCCESS')
            print(result)
            
        elif (self.options['show'] & self.options['instances']):
            res = def_server.getInstances()
            if res == []:
                print('No instances to list')
#             outfile = open("aggiestack-log.txt", "a+")
            logger('\n')
            logger('\n')
            logger('No server to list')
            for data in res:
                listservers = []
                listservers.append("machine_name: " + data['machine_name'])
                listservers.append("instance_name: " + data['instance_name'])
                print(listservers)           

        elif (self.options['evacuate']):
            rackname = self.options['<rackname>']
            def_rack.updateRackStatus(rackname, 'sick')
            
            sickinstancelist = []
            sickmachinelist = def_hardware.getMachineName(rackname)
            
            for machine in sickmachinelist:
                def_hardware.updateHardwareStatus(machine['hardware_name'], 'sick')
                list = def_server.getFlavorName(machine['hardware_name'])
                if len(list)!=0:
                    sickinstancelist += list  
                    
                    
            machinenames = def_hardware.getHardwareName()
            
            for instance in sickinstancelist:
                for machine in machinenames:
                    if def_hardware.canHost(machine,instance['flavor_name'])=='yes':
                        def_server.updateHealthyMachine(instance['instance_name'], machine)
                        break;
                         
        elif (self.options['remove']):
            machine = self.options['<machinename>']
            def_hardware.deleteHardware(machine)
            
        elif (self.options['add']):
            RAM = self.options['<RAM>']
            disks = self.options['<NUM_DISKS>']
            Vcpus = self.options['<VCPUs>']
            ip = self.options['<IP>']
            rackname = self.options['<rackname>']
            
            machinename = self.options['<machinename>']
            def_hardware.insertHardwareByCommand(machinename, rackname, ip, RAM, disks, Vcpus, "healthy")
                
            
             
