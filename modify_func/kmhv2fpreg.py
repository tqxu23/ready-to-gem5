import re
import os

def kmhv2fpreg(name_path,params):
    file_path = os.path.join(name_path, "GEM5/src/cpu/o3/BaseO3CPU.py")
    size = int(params["kmhv2fpreg"]["size"])
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 numPhysFloatRegs 的值
    content = re.sub(r"numPhysFloatRegs = Param.Unsigned\(\d+,", rf"numPhysFloatRegs = Param.Unsigned({size},", content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"kmhv2fpreg已成功修改！")

def kmhv2fpreg_precheck(params):
    if not "kmhv2fpreg" in params:
        print("kmhv2fpreg no in params!")
        return -1
    if not "size" in params["kmhv2fpreg"]:
        print("size not in kmhv2fpreg!")
        return -1
    return 0