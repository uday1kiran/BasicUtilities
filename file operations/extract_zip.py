# importing required modules 
from zipfile import ZipFile
from pathlib import Path
  
def unzip_myfile(zipname):
    with ZipFile(zipname, 'r') as zip:
        print('Extracting zip:'+zipname)
        zip.extractall(Path(zipname).stem)
        print('Extracting Done!')

        
        
import os
directory = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        print(filename)
        unzip_myfile(filename)
        



     
     
    
