echo "spec06_v2.sh, 获取到当前路径: $1"
echo "spec06_v2.sh, 获取到当前任务路径: $2"
echo "spec06_v2.sh, 获取到lst路径: $3"
echo "spec06_v2.sh, 获取任务结果名称: $4"
echo "GCBV_REF_SO: $5"
echo "GCB_RESTORER: $6"
echo "ckpt_path: $7"
source ~/.bashrc
conda deactivate
export PATH=/nfs/home/yanyue/tools/parallel/parallel-20240722/src:$PATH

export GCBV_REF_SO=$5
export GCB_RESTORER=$6
src=$1
work_src=$2
lst_src=$3
res_name=$4
cd $work_src
cd GEM5
export gem5_home=`pwd`
cd $work_src
# mkdir $res_name
cd $res_name
# bash ../parallel_sim.sh `realpath ../kmh_v2.sh ` /nfs/home/xutongqiao/cpt_scripts/spec06/spec06_1c_tqxu.lst  /nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/  spec06_v2_1c_rob > out06-v2_rob.log

cp ${src}/kmh_v2.sh ${work_src}/GEM5/util/xs_scripts/kmh_v2.sh

# bash ${work_src}/GEM5/util/xs_scripts/parallel_sim.sh `realpath ${work_src}/GEM5/util/xs_scripts/kmh_v2.sh ` ${lst_src} /nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/  res > outsim.log
bash ${work_src}/GEM5/util/xs_scripts/parallel_sim.sh `realpath ${work_src}/GEM5/util/xs_scripts/kmh_v2.sh ` ${lst_src} $7 res > outsim.log
# cd ..
# mkdir test_${name}_spec17
# cd test_${name}_spec17
# bash ../parallel_sim.sh `realpath ../kmh_v3_ideal.sh ` /nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/checkpoint.lst /nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/  spec17_v3_1c > out17.log


# source ~/.bashrc
# conda activate clockanalysis
# cd /nfs/home/xutongqiao/feature/gem5_data_proc
# export PYTHONPATH=`pwd`
# # 指定待测项目
# example_stats_dir=${work_src}/GEM5/util/xs_scripts/test_${name}_spec06/spec06_v3_05c_float
# python ./batch.py -s $example_stats_dir -t --topdown-raw -o ${work_src}/out06.csv > ${work_src}/out06-1.log
# python3 simpoint_cpt/compute_weighted.py \
# -r ${work_src}/out06.csv \
# -j /nfs/home/xutongqiao/cpt_scripts/spec06/spec06_0.5c_float_tqxu.json \
# --score ${work_src}/out06-score.csv > ${work_src}/out06-2.log

# cd /nfs/home/xutongqiao/feature/gem5_data_proc
# export PYTHONPATH=`pwd`
# example_stats_dir=${work_src}/GEM5/util/xs_scripts/test_${name}_spec17/spec17_v3_1c
# python ./batch.py -s $example_stats_dir -t --topdown-raw -o ${work_src}/out17.csv > ${work_src}/out17-1.log
# python3 simpoint_cpt/compute_weighted.py \
# -r ${work_src}/out17.csv \
# -j /nfs/home/yanyue/spec17_cpts/checkpoint-0-0-0/cluster-0-0.json \
# --score ${work_src}/out17-score.csv --spec-version 17 > ${work_src}/out17-2.log