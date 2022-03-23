import os
import time
import argparse

time.sleep(60)
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data_dir', type=str)
args = parser.parse_args()
list_files(args.data_dir)
