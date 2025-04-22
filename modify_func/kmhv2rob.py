import re
import os
# numROBEntries = Param.Unsigned(160, "Number of reorder buffer entries")

def kmhv2rob(name_path,params):
    file_path = os.path.join(name_path, "GEM5/src/cpu/o3/BaseO3CPU.py")
    size = int(params["kmhv2rob"]["size"])
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 numPhysFloatRegs 的值
    content = re.sub(r"numROBEntries = Param.Unsigned\(\d+,", rf"numROBEntries = Param.Unsigned({size},", content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"kmhv2rob已成功修改！")

def kmhv2frob_precheck(params):
    if not "kmhv2rob" in params:
        print("kmhv2rob no in params!")
        return -1
    if not "size" in params["kmhv2rob"]:
        print("size not in kmhv2rob!")
        return -1
    return 0