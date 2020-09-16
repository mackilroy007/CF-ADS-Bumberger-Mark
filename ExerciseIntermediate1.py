value = int(input("Please enter an integer representing an elapsed time in seconds:\n"))

WW = 0
DD = 0
HH = 0
MM = 0
SS = 0

if (value >= 60*60*24*7) :
    WW = int(value/(60*60*24*7))
    value = value % (60*60*24*7)
    
if (value >= 60*60*24) :
    DD = int(value/(60*60*24))
    value = value % (60*60*24)    

if (value >= 60*60) :
    HH = int(value/(60*60))
    value = value % (60*60)    

if (value >= 60) :
    MM = int(value/(60))
    value = value % (60)

SS = value    

print("This number equals:\n%d week(s) %d day(s) %d hour(s) %d minute(s) and %d second(s)" %(WW,DD,HH,MM,SS))