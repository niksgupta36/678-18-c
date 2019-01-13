def changeme(mylist):
    print ("Values inside the function before change: ", mylist)
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
mylist= [10,20,30]
changeme(mylist[:]) # what if we change to mylist[:] ???
print ("Values outside the function: ", mylist)

if __name__ == "__main__":
    import sys
else:
    print("Loading module: " + __name__)