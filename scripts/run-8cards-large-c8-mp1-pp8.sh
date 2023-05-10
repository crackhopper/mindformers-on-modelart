bash run_distribute.sh \
    /user/config/nbstart_hccl.json \
    ../configs/gpt2/run_gpt2-large-c8-mp1-pp8.yaml \
    [0,8] \
    train