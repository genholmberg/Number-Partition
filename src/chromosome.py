from random import randint

class chromosome:
    def __init__(self):
        self.total_1 = 0
        self.total_2 = 0
        self.fitness = 0
        self.DNA     = []

    def init_DNA(self, chro_length):
        for x in range(chro_length):
            self.DNA.append(randint(0, 1))

    def set_DNA(self, DNA_string):
        self.DNA = DNA_string.copy()

    def set_fitness(self):
        self.fitness = abs(self.total_1 - self.total_2)

    def get_DNA(self):
        return self.DNA

    def get_fitness(self):
        return self.fitness

    def totaling_sum_1(self, number):
        self.total_1 += number

    def totaling_sum_2(self, number):
        self.total_2 += number

    def pack_numbers(self, data_array):

        for d in range(len(self.DNA)):
            if (self.DNA[d] == 1):
                self.totaling_sum_1(int(data_array[d]))
            else:
                self.totaling_sum_2(int(data_array[d]))

        self.set_fitness()