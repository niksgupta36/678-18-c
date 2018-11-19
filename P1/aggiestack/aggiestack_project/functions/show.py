from .base import Base
from aggiestack_project.definitions import def_image, def_flavor, def_hardware, def_rack,\
    def_server
from test.dtracedata import instance
from aggiestack_project.definitions.logger import *

class Show(Base):
    

    def run(self):
#         outfile = open("aggiestack-log.txt", "a+")
        #print(self.options)
        if(self.options['images']):
            imageslist = def_image.getImages()
            for image in imageslist:
                print(image)
            rackslist = def_rack.getInstances()
            machineslist = def_hardware.getInstances()
            instanceslist = def_server.getInstances()
            for rack in rackslist:
                for machine in machineslist:
                    if rack['rack_name'] == machine['rack_name']:
                        for instance in instanceslist:
                            if instance['machine_name'] == machine['hardware_name']:
                                print(rack['rack_name'] + " : " + instance['image_name'])
                                

            
        elif(self.options['flavors']):
            def_flavor.getFlavors()
        elif(self.options['hardware']):
            def_rack.getRacks();
            def_hardware.getHardwares()
        elif(self.options['all']):
            print('\nImages : \n')
            def_image.getImages()
            print('\nFlavors : \n')
            def_flavor.getFlavors()
            print('\nHardware: \n')
            def_hardware.getHardwares()    
        else:
            logger.logger('Status : FAILURE')
            logger.logger('\n')
            logger.logger("Invalid parameter")