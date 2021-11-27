#!/usr/bin/python3 
import sys
import re
path = '/home/hadoop/Documents/stop_words_english.txt'
stop_words = []
f = open(path, "r", encoding='utf-8-sig')
for x in f:
    stop_words.append(x.rstrip("\n"))
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        new_word = re.sub(r'[\W_]+', '',word)
        if new_word not in stop_words and new_word!="": 
            print('%s\t%s' % (new_word, 1))
