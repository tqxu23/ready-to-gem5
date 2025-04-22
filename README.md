# ready-to-gem5

GEM5一键运行脚本

## 文件结构

configs: 可以尝试运行的yaml案例

cpt_scripts: 用于获取spec切片对应的lst和json文件

environment: （暂时）存储路径相关的文件变量，作为一个python类存储

gem5_data_proc: 用于spec跑分的postprocessing过程中计算最终分数

modify_func: 自动化修改架构，用于动态调用的python函数

src: ready-to-gem5的主要实现

start.py: ready-to-gem5的启动函数

## 运行方法

./start.py example.yaml