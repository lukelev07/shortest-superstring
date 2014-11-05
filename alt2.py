__author__ = 'lukelev07'

import itertools
from heapq import heappush, heappop
import sys


def overlap(a, b):
    """Return the negative amount of overlap between the end of string a and the beginning
    of string b. If there is none, 0 is returned.
    """
    for index, val in enumerate(a):
        chop = a[index:]
        amt = len(chop)
        if chop == b[:amt]:
            return -amt
    return 0


def make_pairs(words):
    """Generates pairs of strings for the given word list.
    """
    tupes = []
    # make iterator
    pair_obj = itertools.combinations(words, 2)
    for i in pair_obj:
        tupes.append(i)

    return tupes


def most_overlap(param):
    """Returns the pair that overlaps the most; will break ties by picking arbitrarily.
    Implemented via min heap with inverted priorities.
    """
    heap = []
    for pair in param:
        heappush(heap, (overlap(pair[0], pair[1]), pair))
    return heappop(heap)


def merge_two(a, b, amount):
    """Merges the two strings leaving out the extra from the overlap.
    """
    return a + b[amount:]


reads = sys.stdin.read().splitlines()
# your main algorithm should go below
while len(reads) > 1:
    # keep original list

    # make pairs
    pairs = make_pairs(reads)
    # pick pair with most overlap
    min_item = most_overlap(pairs)
    # merge that pair (negate amount first)
    new_substring = merge_two(min_item[1][0], min_item[1][1], -min_item[0])
    reads.append(new_substring)
    # remove originals from list; replace with merged string
    #print min_item[1][0]
   # if min_item[1][0]
    reads.remove(min_item[1][0])
    reads.remove(min_item[1][1])
    # repeat until list size == 1

# return string that results
answer = "".join(reads)
print answer

# TO TRY:
# remove substrings first 

