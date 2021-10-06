import glob
import os
import shutil
import sys

def function_q3(inp_file_path, out_folder_path):
    if os.path.isdir(out_folder_path):
        os.rmdir(out_folder_path)
    os.mkdir(out_folder_path)
    files = glob.glob(os.path.join(inp_file_path,'*.txt'))
    #Write code from here
    
            
if __name__=="__main__":
    # inp_file_path = "./testcases/q3/input/"
    # out_folder_path = "./testcases/q3/output/"
    inp_file_path = sys.argv[1]
    out_folder_path = sys.argv[2]
    function_q3(inp_file_path, out_folder_path)





















