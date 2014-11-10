__author__ = 'Luke Levis'

import itertools
import sys


# def overlap(a, b):
#     """Return the negative amount of overlap between the end of string a and the beginning
#     of string b. If there is none, 0 is returned.
#     """
#     for index, val in enumerate(a):
#         chop = a[index:]
#         amt = len(chop)
#         if chop == b[:amt]:
#             return -amt
#     return -0
def overlap(text1, text2):
    len1 = len(text1)
    len2 = len(text2)
    if len1 > len2:
        text1 = text1[-len2:]
    elif len1 < len2:
        text2 = text2[:len1]
    if text1 == text2:
        return -min(len1, len2)
    best = 0
    length = 1
    while True:
        pattern = text1[-length:]
        found = text2.find(pattern)
        if found == -1:
            return -best
        length += found
        if text1[-length:] == text2[:length]:
            best = length
            length += 1


def make_pairs(words):
    tup = []
    pair_obj = itertools.permutations(words, 2)
    for i in pair_obj:
        tup.append(i)
    return tup


def most_overlap(param):
    """Returns the pair that overlaps the most; will break ties by picking arbitrarily.
    """
    to_return = (0,())
    for pair in param:
        lap = overlap(pair[0], pair[1])
        if lap < to_return[0]:
            to_return = (lap, pair)
    return to_return


def merge_two(a, b, amount):
    return a + b[amount:]


def remove_subs(words):
    l = words
    return [j for i, j in enumerate(l) if all(j not in k for k in l[i + 1:])]


reads = sys.stdin.read().splitlines()
reads = remove_subs(reads)
while len(reads) > 1:
    pairs = make_pairs(reads)
    min_item = most_overlap(pairs)
    new_substring = merge_two(min_item[1][0], min_item[1][1], -min_item[0])
    reads.append(new_substring)
    reads.remove(min_item[1][0])
    reads.remove(min_item[1][1])
    if len(reads)%5 == 0:
        reads = remove_subs(reads)
answer = "".join(reads)
print answer
