default:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	time ./build/RISCV/gem5.opt \
	--debug-flags=CommitTrace --debug-start=200000000 \
	./configs/example/kmh.py \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--generic-rv-cpt=/nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/hmmer_nph3/2887/_2887_0.236683_.zstd
# 	--warmup-insts-no-switch=1000 --maxinsts=20000 \

# 3108210 / 5 * 333 = 208,000,000

coremark:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	./build/RISCV/gem5.opt \
	./configs/example/kmh.py \
	--no-pf \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--raw-cpt --generic-rv-cpt=/nfs/home/xuyan/project_dev/test_bin/nexus-am/apps/mem_test/mem_test_bw/build/mem_test_bw-riscv64-xs.bin

maprobe:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	time ./build/RISCV/gem5.opt \
	./configs/example/kmh.py \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--raw-cpt --generic-rv-cpt=/nfs/home/xuyan/project_dev/GEM5-internal/maprobe-riscv64-xs.bin


# /nfs/home/xuyan/project_dev/test_bin/nexus-am-xs/apps/fitest/build/build-fitest----riscv64-xs.bin

amtest:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	time ./build/RISCV/gem5.opt \
	./configs/example/kmh.py \
	--no-pf \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--raw-cpt --generic-rv-cpt=/nfs/home/xuyan/project_dev/test_bin/nexus-am-xs/apps/fitest/build/build-fitest----riscv64-xs.bin


ddrbw:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	time ./build/RISCV/gem5.opt \
	./configs/example/kmh.py \
	--no-pf --no-l3cache --enable-arch-db --arch-db-file=test.db \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--raw-cpt --generic-rv-cpt=/nfs/home/xuyan/project_dev/test_bin/nexus-am/apps/mem_test/mem_test_bw/build/mem_test_bw-riscv64-xs.bin


latency:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	time ./build/RISCV/gem5.opt \
	./configs/example/kmh.py \
	--no-pf --no-l3cache \
	--mem-type=SimpleMemory \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--raw-cpt --generic-rv-cpt=/nfs/home/xuyan/project_dev/test_bin/nexus-am/apps/mem_test/mem_test_latency/build/build-mem_test_latency-10-riscv64-xs.bin


valgrind:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCB_RESTORER="/nfs/home/xuyan/runtime/gcpt/normal-gcpt.bin" && \
	valgrind -s --track-origins=yes --log-file=valgrind-out.txt --error-limit=no \
    --suppressions=util/valgrind-suppressions \
	./build/RISCV/gem5.debug \
	./configs/example/kmh.py \
	--no-pf --no-l3cache \
	--warmup-insts-no-switch=40000 --maxinsts=80000 \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--generic-rv-cpt=/nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/zstd-checkpoint-0-0-0/calculix/13476/_13476_0.160780_.zstd 


# /nfs/home/xuyan/project_dev/test_bin/nexus-am/apps/cachetest/cachetest_o/build/build-cachetest_o-3-10-riscv64-xs.bin
# /nfs/share/zyy/spec06_rv64gcb_O3_20m_gcc12.2.0-intFpcOff-jeMalloc/checkpoint-0-0-0/zeusmp/60111/_60111_0.062686_.gz
#	--debug-flags=Schedule --debug-start=599701265 --debug-end=599901265 \

#   export GCBV_MULTI_CORE_REF_SO="/nfs/home/xuyan/runtime/nemu-gcbv-multi-core-ref.so"
#   export GCB_MULTI_CORE_RESTORER="/nfs/home/xuyan/runtime/gcb-2core-restorer.bin"


dual:
	export GCBV_MULTI_CORE_REF_SO="/nfs/home/xuyan/runtime/nemu-gcbv-multi-core-ref.so" && \
	export GCB_MULTI_CORE_RESTORER="" && \
	/nfs/home/xuyan/project_dev/GEM5-internal/build/RISCV_CHI/gem5.opt \
	/nfs/home/xuyan/project_dev/GEM5-internal/configs/example/xiangshan.py --ruby --num-cpus=2 --mem-type=DDR4_2400_8x8 \
	--generic-rv-cpt=/nfs/home/xuyan/project_dev/GEM5-internal/multi_core_test.gz


vector:
	export GCBV_REF_SO="/nfs/home/xuyan/runtime/riscv64-nemu-gem5-so" && \
	export GCBV_RESTORER="/nfs/home/xuyan/runtime/gcpt/vector-gcpt.bin" && \
	./build/RISCV_CHI/gem5.opt \
	./configs/example/xiangshan.py \
	--enable-riscv-vector \
	--restore-rvv-cpt \
	--dramsim3-ini=ext/dramsim3/xiangshan_configs/xiangshan_DDR4_8Gb_x8_3200_2ch.ini \
	--generic-rv-cpt=/nfs/home/share/zyy/spec06_rv64gcbv_20m_gcc14.1.0_libquantum_hmmer_h264_without_segment/checkpoint-0-0-0/h264ref_foreman.baseline/13696/_13696_0.106234.gz

# select AtFetch/333,AtDecode/333,AtRename/333,AtDispQue/333,AtIssueQue/333,AtIssueArb/333,AtIssueReadReg/333,AtFU/333,AtBypassVal/333,AtWriteVal/333 from LifeTimeCommitTrace;