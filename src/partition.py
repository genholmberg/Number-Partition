from chromosome import chromosome

class partition:
    def __init__(self):
        self.total_1 = 0
        self.total_2 = 0
        self.chromosome = chromosome()

    def totaling_sum_1(self, number):
        self.total_1 += number

    def totaling_sum_2(self, number):
        self.total_2 += number
