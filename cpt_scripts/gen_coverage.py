# 输入cluster-0-0.json
# 输出不同coverage的cluster-0-0-coverage.json
# python3 gen_coverage.py -j cluster-0-0.json -c 0.8 -o spec06_0.8c_int.json -t int

import json
# import os
# import random
# import sys
# import argparse
def gen_coverage(json_name, output, coverage, type):
    # 指定输出int, float or all的benchmark
    spec06 = {
        'int': ['perlbench', 'bzip2', 'gcc', 'mcf', 'gobmk', 'hmmer', 'sjeng', 'libquantum', 'h264ref', 'omnetpp', 'astar', 'xalancbmk'],
        'float': ['bwaves', 'gamess', 'milc', 'zeusmp', 'gromacs', 'cactusADM', 'leslie3d', 'namd', 'dealII', 'soplex', 'povray', 'calculix', 'GemsFDTD', 'tonto', 'lbm', 'wrf', 'sphinx3'],
    }

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-j', '--json', type=str, required=True)
    # parser.add_argument('-o', '--output', type=str, required=True)
    # parser.add_argument('-c', '--coverage', type=float, required=True)
    # parser.add_argument('-t', '--type', type=str, default='all')
    # args = parser.parse_args()

    # json_name = args.json

    data = {}
    with open(json_name) as f:
        data = json.load(f)


    num = 0
    new_json : dict = {}
    for bmk in data.items():
        bmk_name, bmk_ckpts = bmk
        
        # 根据args.type过滤benchmark
        # 检查benchmark是否属于int或float类型
        # 对于perlbench_checkspam这样的变体,提取基本名称(perlbench)进行判断
        base_name = bmk_name.split('_')[0]
        # if args.type == 'int' and base_name not in spec06['int']:
        #     continue
        # elif args.type == 'float' and base_name not in spec06['float']:
        #     continue
        # elif args.type != 'all' and base_name not in spec06['int'] + spec06['float']:
        #     continue
        if type == 'int' and base_name not in spec06['int']:
            continue
        elif type == 'float' and base_name not in spec06['float']:
            continue
        elif type != 'all' and base_name not in spec06['int'] + spec06['float']:
            continue

        bmk_ckpts['points'] = sorted(bmk_ckpts['points'].items(), key=lambda x: float(x[1]), reverse=True)
        lst = []
        total = 0
        if coverage == 1:
            lst = bmk_ckpts['points']
        while total < coverage:
            point = bmk_ckpts['points'][0]
            total += float(point[1])
            bmk_ckpts['points'].remove(point)
            lst.append(point)
        # if args.coverage == 1:
        #     lst = bmk_ckpts['points']
        # while total < args.coverage:
        #     point = bmk_ckpts['points'][0]
        #     total += float(point[1])
        #     bmk_ckpts['points'].remove(point)
        #     lst.append(point)
        
        new_json[bmk_name] = {
            'insts' : bmk_ckpts['insts'],
            'points' : dict(lst)
        }
    # json.dump(new_json, open(args.output, 'w'), indent=4)
    json.dump(new_json, open(output, 'w'), indent=4)
