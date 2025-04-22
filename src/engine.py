
from src.describe.RTG_configurator import RTG_configurator
from src.simulate.RTG_runner import RTG_runner
from src.preprocess.RTG_preprocessor import RTG_preprocessor
from src.postprocess.RTG_postprocessor import RTG_postprocessor
from src.utils.RTG_logger import RTG_logger
from src.preprocess.RTG_workload import RTG_workload
from src.utils.RTG_timer import RTG_timer
import os
# 创建ArgumentParser对象
def engine():
    configurator = RTG_configurator()
    preprocessor = RTG_preprocessor()
    postprocessor = RTG_postprocessor()
    timer = RTG_timer()
    workload = RTG_workload()
    params = configurator.read_yaml_config()
    outpath = configurator.get_param("outpath") # src指的是输出的task的父文件夹路径，用来存放结果的
    gem5_commit_id = configurator.get_param("gem5_commit_id") #七位
    task_category = configurator.get_param("task_category")
    is_continue = configurator.get_param("is_continue")
    if is_continue==None:
        is_continue = False
    kmh_version = configurator.get_param("kmh_version")

    configurator.precheck() #yaml没有格式要求，所以可能会出错，为了避免跑了很久之后出错，就先检查一下参数是不是正确

    name, task_path, res_name, res_path = configurator.generate_param(task_category, is_continue)
    if not is_continue:
        preprocessor.init_task(task_path) #创建任务目录,创建了之后才能开始记录
    preprocessor.init_res(res_path) #创建任务目录,创建了之后才能开始记录

    with RTG_logger(os.path.join(res_path, "logout.log")):
        
        wkld_path, spec = workload.get_wkld_path(configurator, task_category)

        configurator.dump_yaml_config(res_path)

        timer.start()
        if not is_continue:
            preprocessor.pull_gem5(name, outpath, gem5_commit_id)
                
            modify_functions = configurator.get_params("modify_functions")
            modify_params = configurator.get_params("modify_params")
            preprocessor.get_modify_manager().dynamic_import_and_call_all(modify_functions, modify_params, task_path)
            preprocessor.init_gem5(task_path)

        runner = RTG_runner(wkld_path=wkld_path, task_path=task_path)
        runner.execute(res_name=res_name, version=kmh_version, spec=spec, category=task_category)

        # spec可以跑分
        if task_category=="spec":
            spec = configurator.get_param("spec")
            coverage = configurator.get_param("coverage")
            spec_type = configurator.get_param("type")
            json_path, __ = workload.get_lst_json_config(spec=spec, coverage=coverage, type=spec_type)
            postprocessor.data_processing_spec(spec, res_path, task_path, json_path)

        timer.end()