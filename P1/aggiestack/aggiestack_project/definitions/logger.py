from aggiestack_project.database import *;
from aggiestack_project.definitions import *;
from aggiestack_project.functions import *;



def logger(logs):
    try:
        outfile = open("aggiestack-log.txt", "a+")
        outfile.write("\n")
        outfile.write(logs)
    except Exception as e:
        print(e) 
        
            
def loggerlist(logs):
    try:
        outfile = open("aggiestack-log.txt", "a+")
        outfile.write("\n")
        for item in logs:
            outfile.write(item)
            outfile.write("\n")
    except Exception as e:
        print(e) 
        