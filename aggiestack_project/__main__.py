"""
aggiestack

Usage:
   aggiestack config --hardware <filename>
   aggiestack config --images <filename>
   aggiestack config --flavors <filename>
   aggiestack show hardware
   aggiestack show images
   aggiestack show flavors
   aggiestack show all
   aggiestack admin show hardware
   aggiestack admin can_host <machinename><flavor>

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
import aggiestack_project.commands
from docopt import docopt

from . import __version__ as VERSION
from _ast import arg
 
def main():
   
    """Main CLI entrypoint."""
#     from commands import Config
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
    options = docopt(__doc__, version=VERSION)
#     print(options)
     
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
#     for (k, v) in options.items():
#         if(v):
    
    
    for (k, v) in options.items():
        if hasattr(aggiestack_project.commands, k) and v:
            module = getattr(aggiestack_project.commands, k)
            aggiestack_project.commands = getmembers(module, isclass)
            command = [command[1] for command in aggiestack_project.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()