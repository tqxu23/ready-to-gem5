from src.utils.runtime_cmd import run_command_realtime
from environment.Environment import Environment
import os

class RTG_postprocessor():
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(current_file_path)
    
    def data_processing_spec(self, spec, res_path, name_path, json_path):
        if spec == "spec06":
            self.data_processing06(res_path, name_path, json_path)
        elif spec == "spec17":
            self.data_processing17(res_path, name_path, json_path)
        else:
            raise ValueError("Invalid spec value. Expected 'spec06' or 'spec17'.")

    def data_processing06(self, res_path, name_path, json_path):
        run_command_realtime(['bash', os.path.join(self.current_dir, 'data_processing06.sh'), res_path, name_path, json_path, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, os.path.join(self.current_dir, '../../gem5_data_proc')])

    def data_processing17(self, res_path, name_path, json_path):
        run_command_realtime(['bash', os.path.join(self.current_dir, 'data_processing17.sh'), res_path, name_path, json_path, Environment.GCBV_REF_SO, Environment.GCB_RESTORER, os.path.join(self.current_dir, '../../gem5_data_proc')])
