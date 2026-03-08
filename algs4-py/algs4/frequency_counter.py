"""
    Execution:
        python -m algs4.frequency_counter L  input.txt
    Data files:      ../dataset/<arquivo>.txt
        ../dataset/tnyTale.txt
        ../dataset/tale.txt
        ../dataset/leipzig1M.txt

    Read in a list of words from standard input and print out
    the most frequently occurring word that has length greater than
    a given threshold.

    % python -m algs4.frequency_counter 1 ../dataset/tinyTale.txt
    it 10
  
    % python -m algs4.frequency_counter 8 ../dataset/tale.txt
    business 122
  
    % python -m algs4.frequency_counter 10 ../dataset/leipzig1M.txt
    government 24763
"""

import sys
# from algs4.sequential_search_st import SequentialSearchST
#from algs4.binary_search_st import BinarySearchST
from algs4.red_black_bst import RedBlackBST

minlen = int(sys.argv[1])
# st = SequentialSearchST()
#st = BinarySearchST()
st = RedBlackBST()

for line in sys.stdin:
    words = line.split()
    for word in words:
        if len(word) < minlen:
            continue
        if not st.contains(word):
            st.put(word, 1)
        else:
            st.put(word, st.get(word) + 1)

maxstr = ""
st.put(maxstr, 0)
for word in st.Keys():
    if st.get(word) > st.get(maxstr):
        maxstr = word
print(maxstr, " ", st.get(maxstr))
