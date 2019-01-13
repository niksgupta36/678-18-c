"""
aggiestack

Usage:
   aggiestack config --hardware <filename>
   aggiestack config --images <filename>
   aggiestack config --flavors <filename>
   aggiestack admin show hardware
   aggiestack admin can_host <machinename> <flavor>
   aggiestack show hardware
   aggiestack show images
   aggiestack show flavors
   aggiestack show all
   

Options:
    <filename>          File name argument.
    <machinename>       Physical server argument.
    <flavor>             Virtual server type.
    --hardware           File describing the hardware hosting the cloud.
    --images             File describing the images hosting the cloud.
    --flavors            File describing the flavor hosting the cloud.

Examples:
  aggiestack admin show hardware

Help:
  For help using this tool, please open an issue on the Github repository:

"""
import sys
from inspect import getmembers, isclass
import aggiestack_project.functions
from docopt import docopt

from . import __version__ as VERSION
from _ast import arg
 
def main():
   
    #print("hello")
    outfile = open("aggiestack-log.txt", "a+")
    outfile.write('\n')
    args = sys.argv[1:]
    st = ""
    for arg in args:
#         print('passed argument :: {}'.format(arg))
        st = st +" "+ arg
    outfile.write('Command: '+'aggiestack '+str(st))
    outfile.write('\n')
    outfile.write('####################################################################')
    usage = docopt(__doc__, version=VERSION)
    #print(options)
     
    
    for (a, b) in usage.items():
        if hasattr(aggiestack_project.functions, a) and b:
            module = getattr(aggiestack_project.functions, a)
            aggiestack_project.functions = getmembers(module, isclass)
            command = [command[1] for command in aggiestack_project.functions if command[0] != 'Base'][0]
            command = command(usage)
            command.run()
