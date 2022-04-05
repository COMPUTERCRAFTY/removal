import time
import os
import shutil
path="C:\Recycle Bin"
days=30
def removal():
    days=time.time()
    path_exists=os.path.exists(path)
    if path_exists==True:
        files_folders=os.walk(path)
        path_files=os.path.join(path,files_folders)
        ctime=os.stat(path).st_ctime
        if ctime>=days:
            files_folders=os.remove(path)
        else:
            shutil.rmtree()
    else:
        print("Path not found..")   
removal() 


