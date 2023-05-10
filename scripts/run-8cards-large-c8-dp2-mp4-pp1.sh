bash run_distribute.sh \
    /user/config/nbstart_hccl.json \
    ../configs/gpt2/run_gpt2-large-c8-mp8-pp1.yaml \
    [0,8] \
    train