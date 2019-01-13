from .base import Base
import aggiestack_project.definitions.def_hardware as def_hardware
from aggiestack_project.definitions import def_image, def_flavor
import aggiestack_project.definitions.logger as logger

class Config(Base):
   
    
    def run(self):
        try:
            if(self.options['--images']):
               
                image_file=(self.options['<filename>'])
                def_image.insertImages(image_file)
            elif(self.options['--flavors']):
                flavor_file=(self.options['<filename>'])
                def_flavor.insertFlavors(flavor_file)
            elif(self.options['--hardware']):
                hardware_file=(self.options['<filename>'])
                def_hardware.insertHardware(hardware_file)
        except Exception as e:
            print(e)
            logger(e) 
            logger('\n')    
            logger('Status : FAILED')   
        
