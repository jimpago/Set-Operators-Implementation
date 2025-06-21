#DIMITRIOS PAGONIS AM:4985
import csv
import sys

def union(file_r,file_s,file_union):
    with open(file_r,'r') as f1,open(file_s,'r') as f2:
        line1 = next(f1,None)
        line2 = next(f2,None)
        
        prev_line1 = None
        prev_line2 = None
        
        fu = open(file_union,'w')
        
        while line1 and line2:
            
            key1_1 = line1.split("\t")[0]
            key1_2 = int(line1.split("\t")[1])
            key2_1 = line2.split("\t")[0]
            key2_2 = int(line2.split("\t")[1])
            
            
            if(key1_1 < key2_1):
                if line1 != prev_line1:
                    fu.write(line1)
                    prev_line1 = line1
                line1 = next(f1,None)
                
            elif(key2_1 < key1_1):
                if line2 != prev_line2:
                    fu.write(line2)
                    prev_line2 = line2
                line2 = next(f2,None)
                
            else:
                if(key1_2<key2_2):
                    if line1 != prev_line1:
                        fu.write(line1)
                        prev_line1 = line1
                    line1 = next(f1,None)
                elif(key2_2<key1_2):
                    if line2 != prev_line2:
                        fu.write(line2)
                        prev_line2 = line2
                    line2 = next(f2,None)
                
                else:
                    if line1 != prev_line1 and line2 != prev_line2:
                        fu.write(line2)
                        prev_line1 = line1 
                        prev_line2 = line2
                    line1=next(f1,None)    
                    line2=next(f2,None)
                    

        if line1:
            print("File S has remaining lines.")
        while line1:
            fu.write(line1)
            line1 = next(f1, None)

        if line2:
            print("File R has remaining lines.")
        while line2:
            fu.write(line2)
            line2 = next(f2, None)
            
if len(sys.argv) != 4:
    print("Use the correct number of arguments!")
    sys.exit(1)


file_r = sys.argv[1]
file_s = sys.argv[2]
file_union = sys.argv[3]

union(file_r, file_s, file_union)                    
