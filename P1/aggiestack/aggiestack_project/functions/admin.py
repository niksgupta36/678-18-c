from .base import Base
import aggiestack_project.definitions.def_hardware as def_hardware
import aggiestack_project.definitions.def_server as def_server
from aggiestack_project.definitions import def_rack
import aggiestack_project.definitions.logger as logger
from aggiestack_project.definitions.logger import loggerlist


class Admin(Base):
   

    def run(self):
        try:
        
            if (self.options['show'] & self.options['hardware'] ):
                def_hardware.getAdminHardwares()  
        
            elif (self.options['can_host']):
                result=def_hardware.canHost(self.options['<machinename>'],self.options['<flavor>'])
                loggerlist((result))
                logger('Status : SUCCESS')
                print(result)
                
            elif (self.options['show'] & self.options['instances']):
                res = def_server.getInstances()
                if len(res)==0:
                    print('No instances to list')
                    logger('No server to list')
                    logger('Status : SUCCESS')
                if len(res)!=0:
                    for data in res:
                        listservers = []
                        listservers.append("machine_name: " + data['machine_name'])
                        listservers.append("instance_name: " + data['instance_name'])
                        print(listservers) 
                        loggerlist(listservers)
                        logger('Status : SUCCESS')          
    
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
                logger('Status : SUCCESS')     
                             
            elif (self.options['rem']):
                machine = self.options['<machinename>']
                instancelist = def_server.getInstances()
                flag = 1
                for instance in instancelist:
                    if instance['machine_name']==machine:
                        print("Machine cannot be removed as an instance is already hosted on it")
                        flag = 0;
                        break;
                if flag == 1:
                    def_hardware.deleteHardware(machine)
                logger('Status : SUCCESS')    
                
            elif (self.options['add']):
                RAM = self.options['<RAM>']
                disks = self.options['<NUM_DISKS>']
                Vcpus = self.options['<VCPUs>']
                ip = self.options['<IP>']
                rackname = self.options['<rackname>']
                
                machinename = self.options['<machinename>']
                def_hardware.insertHardwareByCommand(machinename, rackname, ip, RAM, disks, Vcpus, "healthy")
                logger('Status : SUCCESS')    
                    
        except Exception as e:
            print(e)
            logger(e)
            logger('Status : FAILED')
                    
                 
