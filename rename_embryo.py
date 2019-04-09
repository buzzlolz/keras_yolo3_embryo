import shutil
import os

def Test():
  
      dir="D:/keras-yolo3/20190409_embryo/"
      
     

      for dirPath, dirNames, fileNames in os.walk(dir):
          print (dirPath+"RRRRR")
          for f in fileNames:
              newname = f.replace(" ","_")
              
              os.rename(os.path.join(dirPath,f),newname)
              
              
      
      
Test()

