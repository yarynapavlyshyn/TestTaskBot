from ChromosomeClass import Chromosome
from multiprocessing import Queue, Process, cpu_count
import time


class Population:

    def __init__(self, chr_size, N):
        """
        For population initialization with size of chromosomes in it and their number.
        :param chr_size: int
        :param N: int
        :return: None
        """
        self._population = []
        self._chromosomes_size = chr_size
        self._size = N

    def generate_random_population(self):
        """
        Generate self._size random sequences of length self._chromosomes_size (chromosomes)
        and set the self._population to be the sequence.
        :return:
        """
        self._population = []
        for i in range(self._size):
            chromosome = Chromosome(self._chromosomes_size)
            chromosome.generate_alfa()
            self._population.append(chromosome)

    def get_chromosome(self, i):
        """
        Get chromosome of population n i-th position in self._population.
        :param i: int
        :return: Chromosome
        """
        return self._population[i]

    def crossover(self, i1, i2, point):
        """
        Crrossover two chromosemes in the given positions where a cross point is given.
        And refresh the _population list with two new chromosomes.
        :param i1: int
        :param i2: int
        :param point: int
        :return: None
        """
        chromosome1 = self.get_chromosome(i1)
        genes1 = chromosome1.get_genes()

        chromosome2 = self.get_chromosome(i2)
        genes2 = chromosome2.get_genes()

        chromosome1.set_genes( genes1[:point] + genes2[point:] )
        chromosome2.set_genes( genes2[:point] + genes1[point:] )

    def crossover(self, i1, i2, point1, point2):
        """
        Crrossover two chromosemes in the given positions where two cross points are given.
        And refresh the _population list with two new chromosomes.
        :param i1: int
        :param i2: int
        :param point: int
        :return: None
        """
        chromosome1 = self.get_chromosome(i1)
        genes1 = chromosome1.get_genes()

        chromosome2 = self.get_chromosome(i2)
        genes2 = chromosome2.get_genes()

        chromosome1.set_genes( genes1[:point1] + genes2[point1:point2] + genes1[point2:])
        chromosome2.set_genes( genes2[:point1] + genes1[point1:point2] + genes2[point2:])

    def mutation(self, i):
        """
        Mutation of a chromosome in the given position in self._population. Update the _population list.
        :param i: int
        :return: None
        """
        chromosome = self.get_chromosome(i)
        chromosome.mutate()

    def _put_result_in_queue(self, q, part, target):
        """
        Helper function to calculate fitness of population using multiprocessing.
        Put rthe result of calculating fitness of part of population in the queue.
        :param q: Queue
        :param part: tuple(int, int)
        :param target: str
        :return: None
        """
        q.put(self.fitness_of_part(target, part[0], part[1]))

    def _divide_in_parts(self):
        """
        Helper function to calculate fitness of population using multiprocessing.
        Divide all tasks in parts in dependency of the number of CPUs.
        :return: list(tuple(int, int)), int
        """
        number_of_processes = cpu_count()
        step = self._size // number_of_processes + 1
        parts = [(step *i, step*(i+1)) for i in range(number_of_processes-1)]
        parts.append((step*(number_of_processes-1), self._size))
        return parts, number_of_processes

    def quick_total_fitness(self, target):
        """
        Calculate fitness of population using multiple processes and return it.
        :param target: str
        :return: int
        """
        start_time = time.time()
        parts, Np = self._divide_in_parts()
        q = Queue()
        processes = []
        for i in range(Np):
            p = Process(self._put_result_in_queue(q, parts[i], target))
            processes.append(p)
            p.start()

        results = []
        for i in range(Np):
            results.append(q.get(True))

        final_sum = sum(results)
        for p in processes:
            p.join()

        end_time = time.time()
        work_time =  end_time - start_time
        print("Quick total fitness: ", work_time)
        print("result: ", final_sum)
        return final_sum

    def total_fitness(self, target):
        """
        Calculate fitness of population and return it.
        :param target: str
        :return: int
        """
        start_time = time.time()
        total = 0
        for chromosome in self._population:
            total += chromosome.get_fitness(target)

        end_time = time.time()
        work_time =  end_time - start_time
        print("Total fitness: ", work_time)
        print("result: ", total)

        return total

    def fitness_of_part(self, target, start_i, end_i):
        """
        Calculate fitness of a part of population from start_i-th to end_i-th chromosome and return it.
        :param target: str
        :return: int
        """
        total = 0
        for i in range(start_i, end_i):
            total += self._population[i].get_fitness(target)
        return total

    def __str__(self):
        """
        For string representation of Population.
        :return: str
        """
        result = ''
        for chromosome in self._population:
            result += chromosome.get_genes() + '\n'
        return result

p = Population(12, 10000)
p.generate_random_population()
p.total_fitness("hello world!")
p.quick_total_fitness("hello world!")
