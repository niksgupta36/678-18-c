


from .base import Base


import aggiestack_project.utility.def_hardware as def_hardware

from aggiestack_project.utility import def_image, def_flavor

class Config(Base):
   
    
    def run(self):
#         print('config, world!')
        #print(self.options)
        if(self.options['--images']):
           
            image_list_path=(self.options['<filename>'])
            def_image.loadImageList(image_list_path)
        elif(self.options['--flavors']):
            flavor_list_path=(self.options['<filename>'])
            def_flavor.loadFlavorList(flavor_list_path)
        elif(self.options['--hardware']):
            hardware_list_path=(self.options['<filename>'])
            def_hardware.loadHardwareList(hardware_list_path)
        
