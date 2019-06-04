# Authors: Benjamin Jacobs, Genavieve Holmberg
# CSCI 443 Project 2
#

import argparse
import operator
import os
import sys
import time

from argparse import ArgumentParser
from chromosome import chromosome
from partition import partition
from random import randint


CHROMOSOME_LENGTH = 0
CURRENT_GENERATE  = 0
ELITISM           = float(0.0)
INPUT_FILE        = ''
MUTATION_RATE     = float(0.0)

CUR_POP           = []
NEXT_POP          = []

parser = ArgumentParser()
sys.stdout = open('..\\results\\log_info.txt', 'wt')

parser.add_argument("-f", "--file", required=True, help="Must have a data file for input")
parser.add_argument("-m", "--mutation", required=False, type=float, default=.10)
parser.add_argument("-e", "--elitism", required=False, type=float, default=.10)
parser.add_argument("-p", "--pop_size", required=False, type=int, default=100)

args = parser.parse_args()

ELITISM = args.elitism
INPUT_FILE = args.file
MUTATION_RATE = args.mutation
POP_SIZE = args.pop_size

def mutation(mutate_me = []):
      arr_len = len(mutate_me)

      number_of_mutations = POP_SIZE * MUTATION_RATE
      number_of_mutations = int(round(number_of_mutations))

      for x in range(0, number_of_mutations):
            # the minus one is to account for the index of the array starting at 0
            random_point = randint(0, (arr_len - 1))
            if (mutate_me[random_point] == 1):
                  mutate_me[random_point] = 0
            else:
                  mutate_me[random_point] = 1

      return mutate_me


def crossover(parent_A = [], parent_B = []):

      # TO DO: change the break point to be the same pre-generation
      break_point = randint(1, (CHROMOSOME_LENGTH - 1))
      offspring_A = (parent_A[:break_point]) + (parent_B[break_point:])
      offspring_B = (parent_A[break_point:]) + (parent_B[:break_point])

      if (MUTATION_RATE > 0):
            offspring_A = mutation(offspring_A)
            offspring_B = mutation(offspring_B)

      return offspring_A, offspring_B

def Main_driver():

      # vars
      global CHROMOSOME_LENGTH
      global CUR_POP
      global NEXT_POP

      data_file = open(INPUT_FILE, 'rt')
      read_in_data_file = []
      for value in data_file.read().split():
            CHROMOSOME_LENGTH += 1
            read_in_data_file.append(value)

      # generate the population at random
      for x in range(POP_SIZE):
            temp = chromosome()
            CUR_POP.append(temp)
            CUR_POP[x].init_DNA(CHROMOSOME_LENGTH)

            CUR_POP[x].pack_numbers(read_in_data_file)
            CUR_POP[x].set_fitness()

      start_time = time.time()
      while(True and (CUR_POP[0].fitness != 0) ):

            global CURRENT_GENERATE
            CURRENT_GENERATE += 1

            CUR_POP.sort(key = operator.attrgetter('fitness'))

            for r in range((len(CUR_POP) // 2)):

                  # ensures that parents are only used once in crossover
                  parent_A_position = r * 2
                  parent_B_position = r * 2 + 1

                  child_b = chromosome()
                  child_a = chromosome()
                  offspring_a = []
                  offspring_b = []

                  if ( (parent_A_position < len(CUR_POP)) and (parent_B_position <= len(CUR_POP)) ):
                        offspring_a, offspring_b = crossover(CUR_POP[parent_A_position].DNA,
                                                                  CUR_POP[parent_B_position].DNA)

                  child_a.set_DNA(offspring_a)
                  child_b.set_DNA(offspring_b)
                  child_a.pack_numbers(read_in_data_file)
                  child_b.pack_numbers(read_in_data_file)

                  NEXT_POP.append(child_a)
                  NEXT_POP.append(child_b)

            NEXT_POP.sort(key = operator.attrgetter('fitness'))

            if (ELITISM > 0):
                  number_of_elites = POP_SIZE * ELITISM
                  number_of_elites = int(round(number_of_elites))

                  for x in range(1, number_of_elites + 1):
                        remove_offspring = -1 * x
                        NEXT_POP.pop(remove_offspring)
                        NEXT_POP.append(CUR_POP[x - 1])

            print('-' * 30)
            print("Current Pop Size [" + str(len(CUR_POP)) + "]")
            print("Current Generation: [" + str(CURRENT_GENERATE) + "]")
            print("Mean Fitness: [" + str(sum(curr.fitness for curr in CUR_POP) / len(CUR_POP) ) + "]")
            print("Best Fitness: [" + str(CUR_POP[0].fitness) + "]")
            print("Worst Fitness: [" + str(CUR_POP[-1].fitness) + "]")

            CUR_POP.clear()
            CUR_POP = NEXT_POP.copy()
            NEXT_POP.clear()

      print('-' * 30)
      print("Current Pop Size [" + str(len(CUR_POP)) + "]")
      print("Current Generation: [" + str(CURRENT_GENERATE + 1) + "]")
      print("Mean Fitness: [" + str(sum(curr.fitness for curr in CUR_POP) / len(CUR_POP) ) + "]")
      print("Best Fitness: [" + str(CUR_POP[0].fitness) + "]")
      print("Worst Fitness: [" + str(CUR_POP[-1].fitness) + "]")
      print("--- %s seconds ---" % (time.time() - start_time))

      

Main_driver()
