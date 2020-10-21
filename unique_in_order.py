"""
Implement the function unique_in_order which takes as argument a sequence and returns
a list of items without any elements with the same value next to each other and
preserving the original order of elements.
"""
from itertools import groupby
def unique_in_order(mySeq):
    result = []
    for i in mySeq:
        if len(result) == 0 or result[-1] != i:
            result.append(i)
    return result
    # result =[x for k, x in enumerate(mySeq) if k==0 or mySeq[k-1] != x]
    # return result
    # return [key for key, _ in groupby(mySeq)]

print(unique_in_order(input()))
# unique_in_order(input())