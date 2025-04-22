# echo "data_processing.sh, 获取到结果路径: $1" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324/test_spec06_01c
# echo "data_processing.sh, 获取到当前任务路径: $2" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324
# echo "data_processing.sh, 获取到当前任务的json路径: $3" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/test20250324
source ~/.bashrc
export PATH=/nfs/home/yanyue/tools/parallel/parallel-20240722/src:$PATH

export GCBV_REF_SO="/nfs/home/share/gem5_ci/ref/normal/riscv64-nemu-interpreter-so"
export GCB_RESTORER=""
res_path=/nfs/home/xutongqiao/feature/feature_auto/modify_test/replace-HYU_spec06_1c_all_v2_20250401-18-51-16/spec06_1c_all_v2
work_path=/nfs/home/xutongqiao/feature/feature_auto/modify_test/replace-HYU_spec06_1c_all_v2_20250401-18-51-16
json_path=/nfs/home/xutongqiao/feature/feature_auto/modify_test/cpt_scripts/spec06/auto_spec06_1c_all.json

source ~/.bashrc
conda activate clockanalysis
cd /nfs/home/xutongqiao/feature/gem5_data_proc
export PYTHONPATH=`pwd`
# 指定待测项目
example_stats_dir=$res_path/res
python ./batch.py -s $example_stats_dir -t --topdown-raw -o ${res_path}/out.csv > ${res_path}/out-1.log
python3 simpoint_cpt/compute_weighted.py \
-r ${res_path}/out.csv \
-j ${json_path} \
--score ${res_path}/out-score.csv > ${res_path}/out-2.log