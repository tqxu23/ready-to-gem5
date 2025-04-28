#!/bin/bash
echo "init_gem5.sh, 获取到当前任务路径: $1"
echo "GCBV_REF_SO: $2"
echo "GCB_RESTORER: $3"

source ~/.bashrc
conda deactivate
export PATH=/nfs/home/yanyue/tools/parallel/parallel-20240722/src:$PATH
export GCBV_REF_SO=$2
export GCB_RESTORER=$3
work_src=$1
cd $work_src
cd GEM5
git diff > git.diff
bash ./init.sh
scons build/RISCV/gem5.opt --gold-linker -j128 --ignore-style
export gem5_home=`pwd`