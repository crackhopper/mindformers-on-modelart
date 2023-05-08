import argparse
import json
import multiprocessing
import time
import sys

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group(title='input data')
    group.add_argument('--input', type=str, required=True,
                       help='Path to input JSON')
    group.add_argument('--json-key', default='text',
                       help='key to extract from json')

    group = parser.add_argument_group(title='output data')
    group.add_argument('--output', type=str, required=True,
                       help='Path to output file')

    group = parser.add_argument_group(title='runtime')
    group.add_argument('--workers', type=int, required=True,
                       help='Number of worker processes to launch')
    group.add_argument('--chunk-size', type=int, required=True,
                       help='Chunk size assigned to each worker process')
    group.add_argument('--log-interval', type=int, default=100,
                       help='Interval between progress updates')
    args = parser.parse_args()

    return args

class Retriever(object):
    def __init__(self, args):
        self.args = args
    def retrieve(self, json_line):
        data = json.loads(json_line)
        text = data[self.args.json_key]
        return text

SEQ_LEN=2048
def main():
    args = get_args()

    print("Opening", args.input)

    r = Retriever(args)
    pool = multiprocessing.Pool(args.workers)

    fin = open(args.input, 'r', encoding='utf-8')
    textlines = pool.imap(r.retrieve, fin, args.chunk_size)

    fout = open(args.output, 'w')
    
    proc_start = time.time()

    lineout=[]
    for i, tline in enumerate(textlines, start=1):
        if len(tline) == 0:
            continue
        lineout += tline.encode('gbk',errors='ignore').decode('gbk').replace('\n','.').split()
        Nout = len(lineout)
        if Nout<SEQ_LEN :
            continue
        else:
            #print(f"lineout num: {Nout}..")
            res = " ".join(lineout)
            fout.write(res)
            fout.write("\n")
            lineout=[]

        if i % args.log_interval == 0:
            current = time.time()
            elapsed = current - proc_start
            print(f"Processed {i} lines",
                  f"({i/elapsed} docs/s).",
                  file=sys.stderr)
            
    print("Done! Now finalizing.")
    fin.close()
    fout.close()
if __name__ == '__main__':
    main()