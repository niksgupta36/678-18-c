from aggiestack_project.database import *;
from aggiestack_project.definitions import *;
from aggiestack_project.functions import *;


def logger(logs):
    outfile = open("aggiestack-log.txt", "a+")
    outfile.write(logs)
    
    