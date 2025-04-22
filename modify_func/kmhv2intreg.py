import re
import os

def kmhv2intreg(name_path,params):
    file_path = os.path.join(name_path, "GEM5/src/cpu/o3/BaseO3CPU.py")
    size = int(params["kmhv2intreg"]["size"])
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 numPhysFloatRegs 的值
    content = re.sub(r'numPhysIntRegs = Param.Unsigned\(\d+,', rf'numPhysIntRegs = Param.Unsigned({size},', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"kmhv2intreg已成功修改！")

def kmhv2intreg_precheck(params):
    if not "kmhv2intreg" in params:
        print("kmhv2intreg no in params!")
        return -1
    if not "size" in params["kmhv2intreg"]:
        print("size not in kmhv2intreg!")
        return -1
    return 0