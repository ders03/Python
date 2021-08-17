import sys 
import os

try: 
  sys.argv[1] 
except Exception as e: 
  print("Syntax: $filter-clients-nmap.py <file input> <file to write>") 
else:
  file = open(sys.argv[1], "r") 
  os.system("touch " + sys.argv[2]) 
  file2 = open(sys.argv[2], "a")  
  with file as lines: 
    for line in lines: 
      if " for 192." in line: 
        next(lines) 
        next(lines) 
        next(lines) 
        next(lines) 
        next(lines)  
      else: 
        file2.write(line) 
try:
  file.close() 
  file2.close() 
except Exception as f: 
  pass 

