from environment.Environment import Environment
from src.utils.runtime_cmd import run_command_realtime
from cpt_scripts.gen_coverage import gen_coverage
from cpt_scripts.gen_lst import gen_lst
import os
class RTG_workload():
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(current_file_path)

    # 在spec模式下生成或使用lst_path
    def get_lst_json_config(self, spec="spec06", coverage=1, type="all"):
        lst_src = ""
        if spec == "spec06":
            # lst_src = os.path.join(self.current_dir, "../../cpt_scripts/spec06/")
            lst_src = Environment.spec06_lst_path
        elif spec == "spec17":
            # lst_src = os.path.join(self.current_dir, "../../cpt_scripts/spec17/")
            lst_src = Environment.spec17_lst_path
        else:
            raise ValueError("spec必须为06或17")
        lst_path = os.path.join(lst_src, f"auto_{spec}_{coverage:.1f}c_{type}.lst")
        json_path = os.path.join(lst_src, f"auto_{spec}_{coverage:.1f}c_{type}.json")
        # 生成json文件
        if os.path.exists(json_path):
            print(f"json文件 '{json_path}' 存在。")
        else:
            # run_command_realtime(['conda', 'run', '-n', 'clockanalysis', 
            #                         'python3', os.join(self.current_dir, f'../../cpt_scripts/gen_coverage.py'), '-j', os.join(lst_src, f"cluster-0-0.json"), '-c', f"{coverage:.1f}", 
            #                             '-o', f"{json_path}", '-t', f"{type}"])
            gen_coverage(json_name=os.path.join(lst_src, f"cluster.json"), output=f"{json_path}", coverage=coverage, type=f"{type}")
        if os.path.exists(lst_path):
            print(f"lst文件 '{lst_path}' 存在。")
        else:
            # run_command_realtime(['conda', 'run', '-n', 'clockanalysis', 
            #                             'python3', self.current_dir+'../../cpt_scripts/gen_lst.py', '-l', lst_src+"checkpoint-0-0-0.lst", '-j', json_path, 
            #                             '-o', lst_path ])
            gen_lst(lst=os.path.join(lst_src, "checkpoint.lst"), json_name=json_path, output=lst_path)
        return json_path, lst_path


    def get_wkld_path(self, configurator, task_category):
        # 准备负载的时候三者有所不同,目标是输出lst_path/ckpt_path
        if task_category=="spec":
            spec = configurator.get_param("spec")
            coverage = configurator.get_param("coverage")
            spec_type = configurator.get_param("type")
            __, lst_path = self.get_lst_json_config(spec=spec, coverage=coverage, type=spec_type)
        elif task_category=="single":
            spec = configurator.get_param("spec")
            if spec=="spec06":
                # ckpt_path = "/nfs/home/jiaxiaoyu/checkpoint/spec06_gcc15.x.0_rv64gcbv_base_intFppOff_2025_0307_elf_NEMU_archgroup_2025-03-28-14-26/checkpoint-0-0-0"
                # ckpt_path= "/nfs/share/zyy/spec06_gcc15_rv64gcbv_base_seg0_ff0_zbs1_autovec_NEMU__full/checkpoint-0-0-0/"
                # ckpt_path = "/nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/"
                ckpt_path = Environment.spec06_path
            elif spec=="spec17":
                # ckpt_path = "/nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/"
                ckpt_path = Environment.spec17_path
            else:
                raise ValueError("spec必须为06或17")
            lst_path = f"{ckpt_path}/{configurator.get_param('case_name')}/{configurator.get_param('case_index')}/_{configurator.get_param('case_index')}*"
        elif task_category == "given":
            spec="not spec"
            lst_path = configurator.get_param("source")
        return lst_path, spec