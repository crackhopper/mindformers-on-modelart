# 在modelart上测试mindformers

数据需要下载到data文件夹。包含：
- gpt2-merges.txt
- gpt2-vocab.json
- oscar-en-10k.jsonl

# 数据预处理
执行 `prepare_oscar_train_set.sh`

预处理后，在data文件夹中找到对应的mindrecord文件。即为测试数据。

数据样本为5442。因为预处理的时候，进行了一定的样本合并，保证样本长度达到2048.

# 单卡运行

执行 `./run-gpt2-tiny.sh` 

# 8卡运行
进入scripts文件夹 `cd scripts`
执行 `./runrun-8cards-tiny-c8-mp8-pp1.sh`