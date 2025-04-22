import re
import os

def lifetimedb(name_path,params):
    file_path = os.path.join(name_path, "GEM5/configs/example/xiangshan.py")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换 numPhysFloatRegs 的值
    content = re.sub('test_sys.arch_db.dump_lifetime = False', 'test_sys.arch_db.dump_lifetime = True', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"lifetime db on!")

def lifetimedb_precheck(params):
    return 0