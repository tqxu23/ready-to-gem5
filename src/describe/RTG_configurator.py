import yaml
import argparse
import time
import glob
from src.preprocess.RTG_modify_manager import RTG_modify_manager
import os

class RTG_configurator():
    def __init__(self):
        pass

    def read_yaml_config(self):
        
        parser = argparse.ArgumentParser(description='Ready To GEM5!')
        parser.add_argument('yaml', type=str, help='yaml source')
        args = parser.parse_args()
        with open(args.yaml, 'r', encoding='utf-8') as file:
            try:
                # 加载 YAML 文件内容
                params = yaml.safe_load(file)
                # 打印解析后的数据
                params["read_time"] = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
                print(params)
                self.params = params
                return params
            except yaml.YAMLError as e:
                print(f"解析 YAML 文件时出错: {e}")
                exit(-1)
    
    def dump_yaml_config(self, task_path):
        with open(os.path.join(task_path, "config.yaml"), "w") as file:
            yaml.dump(self.params, file, default_flow_style=False, allow_unicode=True)
        print("参数已导出到 config.yaml")

    def generate_param_spec(self):
        spec = self.params["spec"]
        coverage = self.params["coverage"]
        type = self.params["type"]
        kmh_version = self.params["kmh_version"]
        task_name = self.params["task_name"]
        outpath = self.params["outpath"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"{spec}_{coverage}c_{type}_{kmh_version}_{current_time}"
        name = f"{task_name}_{spec}_{coverage}c_{type}_{kmh_version}_{current_time}"
        task_path = os.path.join(outpath,name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path

    def generate_param_single(self):
        kmh_version = self.params["kmh_version"]
        case_name = self.params["case_name"]
        case_index = self.params["case_index"]
        task_name = self.params["task_name"]
        outpath = self.params["outpath"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"single_{task_name}_{case_name}_{case_index}_{kmh_version}_{current_time}"
        name = f"single_{task_name}_{case_name}_{case_index}_{kmh_version}_{current_time}"
        task_path = os.path.join(outpath,name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path

    def generate_param_given(self):
        kmh_version = self.params["kmh_version"]
        task_name = self.params["task_name"]
        outpath = self.params["outpath"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"given_{task_name}_{kmh_version}_{current_time}"
        name = f"given_{task_name}_{kmh_version}_{current_time}"
        task_path = os.path.join(outpath,name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path
    
    def generate_param_continue(self):
        kmh_version = self.params["kmh_version"]
        task_name = self.params["task_name"]
        outpath = self.params["outpath"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"given_{task_name}_{kmh_version}_{current_time}"
        name = self.params["name"]
        task_path = os.path.join(outpath,name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path

    def generate_param(self,task_category, is_continue):
        if not is_continue:
            if task_category == "spec":
                return self.generate_param_spec()
            elif task_category == "single":
                return self.generate_param_single()
            elif task_category == "given":
                return self.generate_param_given()
            else:
                print("Task category should be spec or single or given")
                exit(-1)
        else:
            return self.generate_param_continue()
        
    def get_param(self,param_name):
        if param_name in self.params:
            return self.params[param_name]
        else:
            return None
        
    def get_params(self,param_name):
        if param_name in self.params and self.params[param_name] != None:
            return self.params[param_name]
        else:
            return {}
    
    def precheck(self):
        params = self.params

        kmh_version = params["kmh_version"]
        task_category = params["task_category"]
        assert task_category=="spec" or task_category=="single", "task_category必须为spec或single"

        if task_category=="spec":
            assert "spec" in params, "在spec模式下需要给定spec(spec06/spec17)"
            assert "coverage" in params, "在spec模式下需要给定coverage"
            assert "type" in params, "在spec模式下需要给定type"
            spec = params["spec"]
            coverage = params["coverage"]
            type = params["type"]
            assert spec=="spec06" or spec=="spec17", "spec必须为06或17"
            assert float(coverage)<=1 and float(coverage)>0, "coverage的范围是(0,1]"
            assert type=="float" or type=="int" or type=="all", "type需要是float, int, all中的一种"
        elif task_category=="single":
            assert "spec" in params, "在single模式下需要给定spec(spec06/spec17)"
            assert "case_name" in params, "在single模式下需要给定case_name"
            assert "case_index" in params, "在single模式下需要给定case_index"
            ckpt_path = ""
            spec = params["spec"]
            # if spec=="spec06":
            #     ckpt_path = "/nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/"
            # else:
            #     ckpt_path = "/nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/"
            # ckpt_path = f"{ckpt_path}{params['case_name']}/{params['case_index']}/_{params['case_index']}*"
            # assert glob.glob(ckpt_path), f"ckpt设置错误！{ckpt_path}"
        elif task_category=="given":
            assert "source" in params, "在given模式下需要给定source"
            assert glob.glob(params["source"]), f"ckpt设置错误！{params['source']}"
        elif task_category=="continue":
            assert "name" in params, "在continue模式下需要给定name，即任务所在文件夹名"
        assert kmh_version=="v3" or kmh_version=="v2", "kmh_version为v2或v3"
        if "modify_functions" in params and params["modify_functions"]!=None:
            modify_functions = params["modify_functions"]
            if "modify_params" in params and params["modify_params"]!=None:
                modify_params = params["modify_params"]
            else:
                modify_params = {}
            for modify_func in modify_functions:
                modify_manager = RTG_modify_manager()
                assert modify_manager.try_dynamic_import(modify_func, modify_func, modify_params)==0, "modify function出错！"
