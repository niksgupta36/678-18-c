from .base import Base
from aggiestack_project.definitions import def_image, def_flavor, def_hardware, def_rack,\
    def_server
from test.dtracedata import instance
from aggiestack_project.definitions.logger import *

class Show(Base):
    

    def run(self):
        if(self.options['images']):
            images = (def_image.getImages())
            for image in images:
                print("image_name : " + image['image_name'])
                logger("image_name : " + image['image_name'])
                print("image_size : " + image['image_size'])
                logger("image_size : " + image['image_size'])
                print("path : " + image['path'])
                logger("path : " + image['path'])
                print("\n")
                logger("\n")
                logger('Status : SUCCESS')
                                

            
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