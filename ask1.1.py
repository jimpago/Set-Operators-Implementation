#DIMITRIOS PAGONIS AM:4985
import csv 
import sys


def merge_join(file_r,file_s,file_join):
    with open(file_r,'r') as f1,open(file_s,'r') as f2:
        
        #koitaw 2 grammes ti fora sti mnimi
        line1 = next(f1,None)
        line2 = next(f2,None)
        
        prev_line1 = None
        prev_line2 = None
        fj = open(file_join,"w")
        
        buf = []    # array gia na apothikeuw grammes pou tha xriastw
        buf_pos = 0 # thesi ekastote grammis pou thelo na xrisimopoihsw
        buf_max = 0 # megethos ekastote megistou buffer
        
        flag = 1 # arxikopoihsh sto 1 -- >  default 
        
        key1 = line1.split("\t")[0]
        key2 = line2.split("\t")[0]
            
        
        while line1 and line2:
           
            
            if(key1>key2 ):
                
                buf = []
                prev_line2 =line2
                line2 = next(f2,None)
                key2 = line2.split("\t")[0] if line2 else None
                
                flag = 1
            elif(key1 == key2):
                
                prev_line1 = line1
                if(key1 not in buf):
                    buf = []
                
                if(prev_line2 != line2):
                    fj.write(line1.strip() +"\t"+ "\t".join(line2.split("\t")[1:]).strip() + "\n")
                    buf.extend(line2.strip().split("\t"))
                    flag = 0 
                
                prev_line2 =line2 
                line2 = next(f2,None)
                key2 = line2.split("\t")[0] if line2 else None
                
                
                
                
            else:
                
                if(flag == 0): # to proigoumeno stoixeio itan idio
                    
                    line1 = next(f1,None)
                    key1 = line1.split("\t")[0] if line1 else None
                    
                    if(key1 not in buf): # otan exw 1-1 kai meta (epomeno R) < (epomeno S) vlepe aq
                        buf = []
                    
                
                if(key1 in buf and line1 != prev_line1):
                    
                    
                    while buf_pos<len(buf):
                        fj.write(line1.strip() +"\t"+ buf[buf_pos+1]+"\n")
                        buf_pos+=2
                    
                    buf_pos = 0 # to epomeno stoixeio tha ksanadiavasei ti lista apo tin arxi
                    
                    #elegxos gia buf max
                    if(buf_max<(len(buf)/2)):
                        buf_max = (len(buf)/2)
                        
                    prev_line1 = line1
                    line1 = next(f1,None)
                    key1 = line1.split("\t")[0] if line1 else None
                    
                    
                else:
                    if(flag == 0):
                        continue
                    else:
                        
                        line1 = next(f1,None) if line1 else None
                        key1 = line1.split("\t")[0]
                        if key1 in buf: # exw dio seri idies grammes sto R kai meta exw ksana idio stoixeio vlepe bt
                            continue
                        else:
                            buf = [] #adeiazw buffer
                
                flag = 1 #epanafora flag
                    
        print("Max Buffer:",int(buf_max))            
            
            
if len(sys.argv) != 4:
    print("Use the correct number of arguments!")
    sys.exit(1)


file_r = sys.argv[1]
file_s = sys.argv[2]
file_join = sys.argv[3]

merge_join(file_r,file_s,file_join)

        
    
    
    
    
    
    


    


        
            
