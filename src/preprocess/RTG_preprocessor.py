from environment.Environment import Environment
from src.utils.runtime_cmd import run_command_realtime
import os
from .RTG_modify_manager import RTG_modify_manager
class RTG_preprocessor():

    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(current_file_path)
        self.modify_manager = RTG_modify_manager()

    def init_task(self, task_path):
        run_command_realtime(['mkdir', task_path])

    def init_res(self, res_path):
        run_command_realtime(['mkdir', res_path])

    def pull_gem5(self, name, outpath, commit_id):
        run_command_realtime(['bash', os.path.join(self.current_dir, 'git_gem5.sh'), outpath, name, commit_id])

    def init_gem5(self, name_path):
        run_command_realtime(['bash', os.path.join(self.current_dir, 'init_gem5.sh'), name_path, Environment.GCBV_REF_SO, Environment.GCB_RESTORER])

    def get_modify_manager(self):
        return self.modify_manager