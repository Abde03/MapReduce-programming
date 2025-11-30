#!/usr/bin/env python
import sys

current_word = None
current_count = 0

# read from standard input
for line in sys.stdin:
    line = line.strip()  # remove leading/trailing whitespace
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # ignore lines with bad format
        continue

    # accumulate counts
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # output the previous word's count
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# output the last word
if current_word:
    print(f"{current_word}\t{current_count}")
