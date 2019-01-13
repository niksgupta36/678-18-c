"""
aggiestack

Usage:
   aggiestack config --hardware <filename>
   aggiestack config --images <filename>
   aggiestack config --flavors <filename>
   aggiestack admin show hardware
   aggiestack admin rem <machinename>
   aggiestack admin can_host <machinename> <flavor>
   aggiestack show hardware
   aggiestack show images
   aggiestack show flavors
   aggiestack show all
   aggiestack server create --image <imagename> --flavors <flavor> <instancename>
   aggiestack server delete <instancename>
   aggiestack server list
   aggiestack admin show instances
   aggiestack admin evacuate <rackname>
   aggiestack admin add -mem <RAM> -disk <NUM_DISKS> -vcpus <VCPUs> -ip <IP> -rack <rackname> <machinename> 
 
   
Options:
    <filename>           File name argument.
    <machinename>        Physical server argument.
    <flavor>             Virtual server type.
    --hardware           File describing the hardware hosting the cloud.
    --images             File describing the images hosting the cloud.
    --flavors            File describing the flavor hosting the cloud.
    <imagename>          name of image    
    <instancename>       name of instance 
    <rackname>           name of rack
    <RAM>                Ram of the machine
    <NUM_DISKS>          Disks on the machine
    <VCPUs>              VCPUs on the machine
    <IP>                 IP address of the machine
    
Examples:
  aggiestack admin show hardware
  
"""
import sys
from inspect import getmembers, isclass
import aggiestack_project.functions
from aggiestack_project.functions import server
from docopt import docopt
import aggiestack_project.definitions.logger as logger
from . import __version__ as VERSION
from _ast import arg
 
def main():
   
    try:
        logger('\n')
        args = sys.argv[1:]
        st = ""
        for arg in args:
            st = st +" "+ arg
        logger('####################################################################')
        logger('\n')
        logger('Command: '+'aggiestack '+str(st))
        logger('\n')
        usage = docopt(__doc__, version=VERSION)
         
        
        for (a, b) in usage.items():
            if hasattr(aggiestack_project.functions, a) and b:
                module = getattr(aggiestack_project.functions, a)
                aggiestack_project.functions = getmembers(module, isclass)
                command = [command[1] for command in aggiestack_project.functions if command[0] != 'Base'][0]
                command = command(usage)
                command.run()
                
    except Exception as e:
        print(e)            
    
    