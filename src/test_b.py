# import yaml
import argparse

class RTG_configurator():
    def __init__(self):
        pass

    def read_yaml_config(self):
        parser = argparse.ArgumentParser(description='示例脚本')
        parser.add_argument('yaml', type=str, help='yaml source')
        args = parser.parse_args()
        print(f"args.yaml:{args.yaml}")