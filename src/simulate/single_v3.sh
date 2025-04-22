echo "single_v3.sh, 获取到当前路径: $1" # /nfs/home/xutongqiao/feature/feature_auto/modify_test
echo "single_v3.sh, 获取到当前任务路径: $2" # /nfs/home/xutongqiao/feature/feature_auto/modify_test/weekly_spec17_1c_all_v3_20250407-09-44-56
echo "single_v3.sh, 获取到ckpt路径: $3" # /nfs/home/xutongqiao/vector/xs-env/nexus-am/apps/riscv-vectorized-benchmark-suite/_axpy/build/_axpy-riscv64-xs.bin
echo "single_v3.sh, 获取任务结果名称: $4" # vector_axpy
echo "GCBV_REF_SO: $5"
echo "GCB_RESTORER: $6"
source ~/.bashrc
conda deactivate
export PATH=/nfs/home/yanyue/tools/parallel/parallel-20240722/src:$PATH

# export GCBV_REF_SO="/nfs/home/share/gem5_ci/ref/normal/riscv64-nemu-interpreter-so"
export GCBV_REF_SO=$5
export GCB_RESTORER=$6
# export GCBV_REF_SO="/nfs/home/xutongqiao/vector/xs-env/NEMU/build/riscv64-nemu-interpreter"
# export GCB_RESTORER="/nfs/home/share/gem5_ci/tools/gcbv-restorer.bin"
src=$1
work_src=$2
ckpt_src=$3
res_name=$4
cd $work_src
cd GEM5
export gem5_home=`pwd`
cd $work_src
# mkdir $res_name
cd $res_name
# bash ../parallel_sim.sh `realpath ../kmh_v2.sh ` /nfs/home/xutongqiao/cpt_scripts/spec06/spec06_1c_tqxu.lst  /nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/  spec06_v2_1c_rob > out06-v2_rob.log

# cp ${src}/kmh_v2.sh ${work_src}/GEM5/util/xs_scripts/kmh_v2.sh

# 注意：此处已经支持向量
# ${work_src}/GEM5/build/RISCV/gem5.opt \
# --redirect-stdout --redirect-stderr \
# ${work_src}/GEM5/configs/example/xiangshan.py --ideal-kmhv3 \
# --arch-db-fromstart=True \
# --generic-rv-cpt=`realpath $3` \
# --enable-arch-db \
# --enable-riscv-vector \
# --arch-db-file=m5out/test.db > outsim.log

${work_src}/GEM5/build/RISCV/gem5.opt \
${work_src}/GEM5/configs/example/xiangshan.py --ideal-kmhv3 \
--generic-rv-cpt=`realpath $3` --enable-riscv-vector > outsim.log