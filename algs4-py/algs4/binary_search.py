"""
*  Execution:    python -m algs4.binary_search whitelist.txt  input.txt
*  Data files:   ../dataset/tinyW.txt
*                ../dataset/tinyT.txt
*                ../dataset/largeW.txt
*                ../dataset/largeT.txt
*
* % python -m algs4.binary_search ../dataset/tinyW.txt ../dataset/tinyT.txt
*  50
*  99
*  13
*
* % python -m algs4.binary_search ../dataset/largeW.txt ../dataset/largeT.txt | more
*  499569
*  984875
*  295754
*  207807
*  140925
*  161828
*  [367, 966 total values]
*
"""


class BinarySearch:
    def index_of(self, arr, key):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            # key is in arr[lo..hi] or not present.
            mid = lo + int((hi - lo) / 2)
            if (key < arr[mid]):
                hi = mid - 1
            elif (key > arr[mid]):
                lo = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    import sys
    # read the integers from a file
    with open(sys.argv[1]) as f:
        whitelist = [int(i) for i in f]
    whitelist = sorted(whitelist)

    # read integer key from standard input; print if not in whitelist
    bs = BinarySearch()
    for line in sys.stdin:
        key = int(line)
        if bs.index_of(whitelist, key) == -1:
            print(key)
