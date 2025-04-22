
from src.utils.runtime_cmd import run_command_realtime
import os
from environment.Environment import Environment

# wkld_path lst文件的路径, 如果是单个文件, 直接传入ckpt路径
# task_path 任务路径(使用的gem5的父文件夹)
# res_name 任务结果的名称
class RTG_runner():

    # 用作完全自定义的模式
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(current_file_path)
        pass

    def __init__(self, wkld_path, task_path):
        current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(current_file_path)
        self.wkld_path = wkld_path
        self.task_path = task_path

    def __check_and_print(self, res_name):
        print("Start Running!")
        print(f"workload文件路径: {self.wkld_path}")
        print(f"当前路径: {self.current_dir}")
        print(f"任务路径: {self.task_path}")
        print(f"任务结果路径: {res_name}")

    def execute_single_v2(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,'single_v2.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER])

    def execute_single_v3(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,self.current_dir,'single_v3.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER])

    def execute_spec06_v2(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,self.current_dir,'spec06_v2.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, Environment.spec06_path])

    def execute_spec06_v3(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,self.current_dir,'spec06_v3.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, Environment.spec06_path])

    def execute_spec17_v2(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,self.current_dir,'spec17_v2.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, Environment.spec17_path])

    def execute_spec17_v3(self, res_name):
        self.__check_and_print(res_name)
        run_command_realtime(['bash', os.path.join(self.current_dir,self.current_dir,'spec17_v3.sh'), self.current_dir, self.task_path, self.wkld_path, res_name, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, Environment.spec17_path])

    def execute(self, res_name, version, spec, category):
        if version == "v2":
            if category == "single":
                self.execute_single_v2(res_name)
            elif category == "spec":
                if spec == "spec06":
                    self.execute_spec06_v2(res_name)
                elif spec == "spec17":
                    self.execute_spec17_v2(res_name)
                else:
                    print("Execute error: spec should be spec06 or spec17")
            else:
                print("Execute error: category should be single or spec")
        elif version == "v3":
            if category == "single":
                self.execute_single_v3(res_name)
            elif category == "spec":
                if spec == "spec06":
                    self.execute_spec06_v3(res_name)
                elif spec == "spec17":
                    self.execute_spec17_v3(res_name)
                else:
                    print("Execute error: spec should be spec06 or spec17")
            else:
                print("Execute error: category should be single or spec")
        else:
            print("Execute error: version should be v2 or v3")
