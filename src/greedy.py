# Authors: Benjamin Jacobs, Genavieve Holmberg
# CSCI 443 Project 2
#

import os
from random import randint
import operator
import time
from partition import partition
INPUT_FILE = 'C:\\Users\\Genavieve\\Documents\\SCSU\\SCSU Fall 2018\\CSCI 443\\Project 2\\CSCI_443_Min_Bin_GA\\data\\100000numbers.dat'

def find_partition(int_list):
    # returns: An attempt at a partition of `int_list` into two sets of equal sum
    a = 0
    b = 0
    for n in sorted(int_list, reverse=True):
        if a < b:
            a += n
        else:
            b += n
    return (a, b)

def Main_driver():
    start = time.time()
    data_file = open(INPUT_FILE, 'rt')
    read_in_data_file = []
    for value in data_file.read().split():
        read_in_data_file.append(value)
        read_in_data_file = [int(i) for i in read_in_data_file]

    bin1, bin2 = find_partition(read_in_data_file)
    fitness = abs(bin1 - bin2)
    end = time.time()
    alg_time = end - start
    
    print("Greedy Fitness: [" + str(fitness) + "]\n")
    print("The Greedy Algorithm took [" + str(alg_time) + "] seconds.\n")


Main_driver()