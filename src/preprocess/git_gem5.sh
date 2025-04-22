#!/bin/bash
echo "git_gem5.sh, 获取到当前指定任务路径: $1"
echo "git_gem5.sh, 获取到当前指定任务名: $2"
echo "git_gem5.sh, 获取到当前分支: $3"
source ~/.bashrc
work_src="$1/$2"
cd $work_src
git clone https://github.com/OpenXiangShan/GEM5
cd GEM5
git checkout $3