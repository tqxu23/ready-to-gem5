# 输入json, lst文件
# 输出指定覆盖率的lst
# python3 gen_lst.py -l checkpoint-0-0-0.lst -j spec06_0.8coverage.json -o spec_0.8c.lst

# import argparse

def gen_lst(lst, json_name, output):

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-l', '--lst', type=str, required=True)
    # parser.add_argument('-j', '--json', type=str, required=True)
    # parser.add_argument('-o', '--output', type=str, required=True)
    # args = parser.parse_args()

    def filter_checkpoints(lst_file, json_file, output_file):
        import json
        
        # 读取json文件
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # 获取所有benchmark的关键点
        target_points = {}
        for benchmark in data:
            if 'points' in data[benchmark]:
                # 处理benchmark名称中可能的变体
                base_name = benchmark.split('_')[0]  # 例如从 gobmk_13x13 获取 gobmk
                target_points[benchmark] = data[benchmark]['points'].keys()
                target_points[base_name] = data[benchmark]['points'].keys()  # 同时存储简短版本
        
        # 读取lst文件并写入过滤后的结果
        with open(lst_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                # 跳过空行
                if not line.strip():
                    continue
                
                # 解析每一行
                parts = line.strip().split()
                if not parts:
                    continue
                    
                # 获取checkpoint信息
                checkpoint_name = parts[0]  # 例如 mcf_12253 或 gobmk_13x13_6366
                name_parts = checkpoint_name.split('_')
                
                # 处理不同格式的benchmark名称
                benchmark = name_parts[0]  # 基本名称 (如 mcf, gobmk)
                full_benchmark = '_'.join(name_parts[:-1])  # 完整名称 (如 gobmk_13x13)
                checkpoint_num = name_parts[-1]  # checkpoint编号
                
                # 检查是否匹配（检查both简单名称和完整名称）
                is_target = False
                if benchmark in target_points and checkpoint_num in target_points[benchmark]:
                    is_target = True
                elif full_benchmark in target_points and checkpoint_num in target_points[full_benchmark]:
                    is_target = True
                    
                if is_target:
                    f_out.write(line)



    filter_checkpoints(lst, json_name, output)
    print(f"已将过滤后的结果写入到 {output}")
