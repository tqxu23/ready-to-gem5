import re
import os
import shutil

def replacefile(name_path,params):
    src = params["replacefile"]["src"]
    dest_path = params["replacefile"]["dest_path"]
    dest = os.path.join(name_path, dest_path)

    shutil.copy(src, dest)
    
    print(f"已成功替换文件！")

def replacefile_precheck(params):
    if not "replacefile" in params:
        print("replacefile no in params!")
        return -1
    if not "src" in params["replacefile"]:
        print("src not in replacefile!")
        return -1
    if not "dest_path" in params["replacefile"]:
        print("dest_path not in replacefile!")
        return -1
    return 0