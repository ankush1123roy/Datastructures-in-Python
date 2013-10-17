import sys
import pdb;pdb.set_trace()
f = open(sys.argv[1],"r")
No  = int(sys.argv[2])
I = 0
while I < No:
    print f.readline()
    I +=1
f.close()
