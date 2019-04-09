
import os
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    for dirPath, dirNames, fileNames in os.walk(dir):
        #print (dirPath)
        for name in fileNames:
            #print (os.path.join(dirPath, name))
            file.write(name)
            file.write("\n")
def Test():
  
      dir="D:/keras-yolo3/result_delete/"
      outfile="result_delete.txt"
      wildcard = ".bmp"
     
      file = open(outfile,"a+")
      if not file:
        print ("cannot open the file %s for writing" % outfile)
      ListFilesToTxt(dir,file,wildcard, 0)
     
      file.close()
Test()

