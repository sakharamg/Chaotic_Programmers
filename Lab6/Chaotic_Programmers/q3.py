import os as os
import shutil as shu
import glob
import sys

def function_q3(inp_file_path, out_folder_path):

  """
  	
  	Parameters:	inp_file_path [Type:string]
  				Relative path to the directory containing files
  			out_folder_path [Type:string]
  				Relative path to the directory which will contain all the pairs of files whose contents are reverse of each other
  	Objective:	The function files pairs of files in inp_file_path that are reverse of each other and saves in the out_folder_path directory
  	
  """
  
  if os.path.isdir(out_folder_path):
    os.rmdir(out_folder_path)
  os.mkdir(out_folder_path)
  files = glob.glob(os.path.join(inp_file_path,'*.txt'))
  #Write code from here
  os.chdir(inp_file_path)
  fileslist = os.listdir(".")
  filescontent = {}
  for file in fileslist:
    f = open(file,"r")
    content = f.read().splitlines()
    f.close()
    filescontent[file] = content

#print(filescontent)    
#content has been read, now check for each key, other values
  reverselist = set()   
  for filename in filescontent:
    content = filescontent[filename]
    for key,val in filescontent.items():
        if key == filename:
            continue
        if content == val[::-1]:
            reverselist.add(filename)
            reverselist.add(key)

  #print(reverselist)
  for i in reverselist:
    shu.move('./'+i+'','../output')    
            
if __name__=="__main__":
    # inp_file_path = "./testcases/q3/input/"
    # out_folder_path = "./testcases/q3/output/"
    inp_file_path = sys.argv[1]
    out_folder_path = sys.argv[2]
    function_q3(inp_file_path, out_folder_path)
