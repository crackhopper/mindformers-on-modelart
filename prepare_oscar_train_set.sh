CUR_DIR=`pwd`

input_file="$CUR_DIR/data/oscar-en-10k.jsonl"
cleaned_file="$CUR_DIR/data/oscar-train.txt"
output_file="$CUR_DIR/data/oscar-train.mindrecord"
vocab_file="$CUR_DIR/data/gpt2-vocab.json"
merge_file="$CUR_DIR/data/gpt2-merges.txt"

python retrieve_from_jsonl.py \
    --input "$input_file" \
    --output "$cleaned_file" \
    --workers 1 --chunk-size 1

echo "converting to mindrecord..."
rm "$output_file"*

python create_lm_data.py \
    --input_file "$cleaned_file" \
    --output_file "$output_file" \
    --num_splits 1 \
    --max_length 2049 \
    --vocab_file="$vocab_file" \
    --merge_file="$merge_file"

if [[ -f "$cleaned_file" ]]; then
    rm "$cleaned_file"
fi
