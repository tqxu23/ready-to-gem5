import re
import os

def kmhv3fpreg(name_path,params):
    file_path = os.path.join(name_path, "GEM5/configs/example/xiangshan.py")
    size = int(params["kmhv3fpreg"]["size"])
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 numPhysFloatRegs 的值
    content = re.sub(r'(cpu\.numPhysFloatRegs\s*=\s*)\d+', rf'\g<1>{size}', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"寄存器值已成功修改！")

def kmhv3fpreg_precheck(params):
    if not "kmhv3fpreg" in params:
        print("kmhv3fpreg no in params!")
        return -1
    if not "size" in params["kmhv3fpreg"]:
        print("size not in kmhv3fpreg!")
        return -1
    return 0