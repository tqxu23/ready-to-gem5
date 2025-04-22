import yaml
import argparse
import time
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
        src = self.params["src"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"{spec}_{coverage}c_{type}_{kmh_version}"
        name = f"{task_name}_{spec}_{coverage}c_{type}_{kmh_version}_{current_time}"
        task_path = os.path.join(src, name)
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
        src = self.params["src"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"single_{task_name}_{case_name}_{case_index}_{kmh_version}"
        name = f"single_{task_name}_{case_name}_{case_index}_{kmh_version}_{current_time}"
        task_path = os.path.join(src, name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path

    def generate_param_given(self):
        kmh_version = self.params["kmh_version"]
        task_name = self.params["task_name"]
        src = self.params["src"]

        current_time = time.strftime('%Y%m%d-%H-%M-%S', time.localtime())
        res_name = f"given_{task_name}_{kmh_version}"
        name = f"given_{task_name}_{kmh_version}_{current_time}"
        task_path = os.path.join(src, name)
        res_path = os.path.join(task_path, res_name)

        self.params["task_path"] = task_path
        self.params["res_path"] = res_path
        self.params["res_name"] = res_name
        self.params["name"] = name

        return name, task_path, res_name, res_path
  

    def generate_param(self,task_category):
        if task_category == "spec":
            return self.generate_param_spec()
        elif task_category == "single":
            return self.generate_param_single()
        elif task_category == "given":
            return self.generate_param_given()
        else:
            print("Task category should be spec or single or given")
            exit(-1)


    def get_param(self,param_name):
        if param_name in self.params:
            return self.params[param_name]
        else:
            return {}
        