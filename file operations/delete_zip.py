from pathlib import Path
  
  
        
import os
directory = os.path.dirname(os.path.realpath(__file__))
     
for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        os.remove(filename)


     
     
    
