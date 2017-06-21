import random
import string


class Chromosome:

    def __init__(self, Size):
        """
        For chromosome initialization with Size.
        :param Size: int
        :return: None
        """
        self._size = Size
        self._genes = ''
        self._fitness = None

    def mutate(self):
        """
        Mutation of the chromosome - changes one bit of gene.
        :return: None
        """
        i = random.randint(0, self._size - 1)
        gene = self._genes[i]
        new_gene = gene
        while new_gene == gene:
            new_gene = random.choice([random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase)])
        self._genes = self._genes[:i] + new_gene + self._genes[(i+1):]

    def set_genes(self, genes):
        """
        Receives the parameter genes and sets the attribute to the value.
        :param genes: str
        :return: None
        """
        self._genes = genes

    def get_genes(self):
        """
        Decorator for the _genes attribute.
        :return: str
        """
        return self._genes

    def get_fitness(self, target = None):
        """
        Decorator for the _fitness attribute. If target is None just returns the value of _fitness.
        Calculate fitness to the given word otherwise, set the attribute and return it.
        :param target: str, optional
        :return: int
        """
        if not target:
            return self._fitness
        self._update_fitness(target)
        return self.get_fitness()

    def _update_fitness(self, target):
        """
        Calculate distance between two strings of the same lengths and set self._fitness to be equal to that value.
        :param target: str
        :return: None
        """
        fitness = 0
        if self._size != len(target):
            raise ValueError("target is of invalid size")
        for i in range(self._size):
            fitness += abs( ord(self._genes[i]) - ord(target[i]) )
        self._fitness = fitness

    def generate_alfa(self):
        """
        Generate the random sequence of letters of self._size length and set _genes to this sequence.
        :return: None
        """
        self._genes = ''.join(random.choice([random.choice(string.ascii_uppercase),
                                      random.choice(string.ascii_lowercase)]) for i in range(self._size))

    def generate_numeric(self):
        """
        Generate the random sequence of digits of self._size length and set _genes to this sequence.
        :return: None
        """
        self._genes = ''.join(random.choice(string.digits) for i in range(self._size))

    def generate_alfanumeric(self):
        """
        Generate the random sequence of letters and/or digits of self._size length and set _genes to this sequence.
        :return: None
        """
        self._genes = ''.join(random.choice([random.choice(string.ascii_uppercase),
                                     random.choice(string.ascii_lowercase),
                                     random.choice(string.digits)]) for i in range(self._size))

    def __str__(self):
        """
        For string representation of Chromosome.
        :return: str
        """
        return self._genes
