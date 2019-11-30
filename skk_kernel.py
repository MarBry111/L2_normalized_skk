#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from itertools import combinations 

def subseq_kernel(str1, str2, q, lamb ):
    """
    Computes String Subsequence Kernel

    :param str1:    first word, string
    :param str2:    second word, string
    :param q:       length of subsequence 
    :param lamb:    decay parameter, float

    :return ssk:  String Subsequence Kernel
    """
    str1 = list(str1)
    str2 = list(str2)
    #length of both strings
    l1, l2 = len(str1), len(str2)
    #making lists of indexes of each letter
    letters1, letters2 = list(range(l1)), list(range(l2))
    #generating combinations of q-elements indexes of letters
    comb1 = combinations(letters1, q) 
    comb2 = combinations(letters2, q) 
    
    set_u = dict()
    #genereting q-element sequences of letters
    for c1 in comb1:
        tmp_s = ''
        #making sure that the indexes are sorted
        c1 = sorted(list(c1))
        for ci in c1:
            tmp_s = tmp_s + str1[ci]
        if tmp_s in set_u:
            set_u[tmp_s].append([1,c1])
        else:
            set_u[tmp_s] = [[1,c1]]
    
    for c2 in comb2:
        tmp_s = ''
        c2 = sorted(list(c2))
        for ci in c2:
            tmp_s = tmp_s + str2[ci]
        if tmp_s in set_u:
            set_u[tmp_s].append([2,c2])
        else:
            set_u[tmp_s] = [[2,c2]]
    
    ssk = 0 
    for u, k in zip(set_u.values(), set_u.keys()):
        u1, u2 = [],[]
        v1, v2 = 0, 0
        
        for ui in u:
            if ui[0] == 1:
                v1 = v1 + lamb**(ui[1][-1] - ui[1][0] + 1)
            elif ui[0] == 2:
                v2 = v2 + lamb**(ui[1][-1] - ui[1][0] + 1)
        
        if v1 != 0 and v2 != 0:
            ssk = ssk + v1*v2

    return ssk

def subseq_kernel_normalized(str1, str2, q, lamb ):
    """
    Computes normalized String Subsequence Kernel

    :param str1:    first word, string
    :param str2:    second word, string
    :param q:       length of subsequence 
    :param lamb:    decay parameter, float

    :return ssk_n:  normalized String Subsequence Kernel
    """
    ssk_n = subseq_kernel( str1, str2, q, lamb )/ \
            np.sqrt(subseq_kernel( str1, str1, q, lamb )* \
            subseq_kernel( str2, str2, q, lamb ))
    return ssk_n