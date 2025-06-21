#DIMITRIOS PAGONIS AM:4985
import csv
import sys
def intersection(file_r,file_s,file_inter):
    with open(file_r,'r') as f1,open(file_s,'r') as f2:
        line1 = next(f1,None)
        line2 = next(f2,None)
        
        fi = open(file_inter,'w')
        
        while line1 and line2:
            
            if(line1 == line2):
                fi.write(line1)
                line1 = next(f1,None)
                line2 = next(f2,None)
            elif(line1 < line2):
                line1 = next(f1,None)
            else:
                line2 = next(f2,None)
                

if len(sys.argv) != 4:
    print("Use the correct number of arguments!")
    sys.exit(1)


file_r = sys.argv[1]
file_s = sys.argv[2]
file_inter = sys.argv[3]

intersection(file_r, file_s, file_inter)
