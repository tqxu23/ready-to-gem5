echo "data_processing.sh, 获取到结果路径: $1" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324/test_spec06_01c
echo "data_processing.sh, 获取到当前任务路径: $2" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324
echo "data_processing.sh, 获取到当前任务的json路径: $3" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324
echo "GCBV_REF_SO: $4" # /nfs/home/share/gem5_ci/ref/normal/riscv64-nemu-interpreter-so
echo "GCB_RESTORER: $5" # ""
source ~/.bashrc
export PATH=/nfs/home/yanyue/tools/parallel/parallel-20240722/src:$PATH

export GCBV_REF_SO=$4
export GCB_RESTORER=$5
res_path=$1
work_path=$2
json_path=$3

source ~/.bashrc
conda activate clockanalysis
# cd /nfs/home/xutongqiao/feature/gem5_data_proc
cd $6
export PYTHONPATH=`pwd`
# 指定待测项目
example_stats_dir=$res_path/res
python ./batch.py -s $example_stats_dir -t --topdown-raw -o ${res_path}/out.csv > ${res_path}/out-1.log
python3 simpoint_cpt/compute_weighted.py \
-r ${res_path}/out.csv \
-j ${json_path} \
--score ${res_path}/out-score.csv > ${res_path}/out-2.log

# cd /nfs/home/xutongqiao/feature/gem5_data_proc
# export PYTHONPATH=`pwd`
# example_stats_dir=${work_src}/GEM5/util/xs_scripts/test_${name}_spec17/spec17_v3_1c
# python ./batch.py -s $example_stats_dir -t --topdown-raw -o ${work_src}/out17.csv > ${work_src}/out17-1.log
# python3 simpoint_cpt/compute_weighted.py \
# -r ${work_src}/out17.csv \
# -j /nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/cluster-0-0.json \
# --score ${work_src}/out17-score.csv --spec-version 17 > ${work_src}/out17-2.log