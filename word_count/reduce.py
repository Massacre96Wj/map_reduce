#基础版
import operator
import sys
current_word = None
curent_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
            continue
    if current_word == word:
        curent_count += count
    else:
        if current_word:
            print ('%s\t%s' % (current_word,curent_count))
        current_word=word
        curent_count=count

if current_word==word:
    print ('%s\t%s' % (current_word,curent_count))


# 进阶版
from operator import itemgetter
from itertools import groupby
import sys

def read_mapper_output(file, separator = '\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator = '\t'):
    data = read_mapper_output(sys.stdin, separator = separator)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print ("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            pass

if __name__ == "__main__":
    main()