import sys
import modify_func
import importlib

class RTG_modify_manager():
    def __init__(self):
        sys.path.append('./modify_func')

    def try_dynamic_import(self, module_name, function_name, param):
        try:
            module = importlib.import_module(module_name)
            
            getattr(module, function_name)
            if hasattr(module, function_name+"_precheck"):
                func = getattr(module, function_name+"_precheck")
                return func(param)
            return 0
        except ModuleNotFoundError:
            print(f"模块 '{module_name}' 未找到，请确认文件是否存在。")
            return -1
        except AttributeError:
            print(f"函数 '{function_name}' 未找到，请确认函数是否在模块 '{module_name}' 中。")
            return -1
        except Exception as e:
            print(f"调用函数时出错：{e}")
            return -1

    def dynamic_import_and_call_all(self, modify_functions, modify_params, task_path):
        for modify_func in modify_functions:
            result = self.dynamic_import_and_call(modify_func, modify_func, task_path, modify_params)
            if result is not None:
                print(result)

    def dynamic_import_and_call(self, module_name, function_name, task_path, modify_params):
        """
        动态导入模块并调用函数。

        :param module_name: 模块的名称（字符串，例如 'module1'）
        :param function_name: 函数的名称（字符串，例如 'my_function'）
        :param args: 位置参数
        :param kwargs: 关键字参数
        :return: 函数的返回值
        """
        try:
            # 动态导入模块
            module = importlib.import_module(module_name)
            
            # 获取模块中的函数
            func = getattr(module, function_name)
            
            # 调用函数并返回结果
            return func(task_path, modify_params)
        except ModuleNotFoundError:
            print(f"模块 '{module_name}' 未找到，请确认文件是否存在。")
            exit(-1)
        except AttributeError:
            print(f"函数 '{function_name}' 未找到，请确认函数是否在模块 '{module_name}' 中。")
            exit(-1)
        except Exception as e:
            print(f"调用函数时出错：{e}")
            exit(-1)