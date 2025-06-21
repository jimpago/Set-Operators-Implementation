#DIMITRIOS PAGONIS AM:4985
import csv 
import sys
def difference(file_r,file_s,file_dif):
     with open(file_r,'r') as f1,open(file_s,'r') as f2:
        line1 = next(f1,None)
        line2 = next(f2,None)
        
        prev_line1 = None
        
        fd = open(file_dif,'w')
        
        while line1 and line2:
            
            if(line1 < line2):
                if line1 != prev_line1:
                    fd.write(line1)
                    prev_line1 = line1
                line1  = next(f1,None)
            elif(line1 == line2):
                prev_line1 = line1
                line1 = next(f1,None)
                line2 = next(f2,None)
            else:
              
                line2 = next(f2,None)

if len(sys.argv) != 4:
    print("Use the correct number of arguments!")
    sys.exit(1)


file_r = sys.argv[1]
file_s = sys.argv[2]
file_dif = sys.argv[3]

difference(file_r, file_s, file_dif)
            
            
            
            
            
        
        
        