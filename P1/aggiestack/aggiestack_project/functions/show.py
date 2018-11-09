from .base import Base
from aggiestack_project.definitions import def_image, def_flavor, def_hardware

class Show(Base):
    

    def run(self):
        outfile = open("aggiestack-log.txt", "a+")
        #print(self.options)
        if(self.options['images']):
            def_image.getImages()
        elif(self.options['flavors']):
            def_flavor.getFlavors()
        elif(self.options['hardware']):
            def_hardware.getHardwares()
        elif(self.options['all']):
            print('\nImages : \n')
            def_image.getImages()
            print('\nFlavors : \n')
            def_flavor.getFlavors()
            print('\nHardware: \n')
            def_hardware.getHardwares()    
        else:
            outfile.write('Status : FAILURE')
            outfile.write('\n')
            outfile.write("Invalid parameter")