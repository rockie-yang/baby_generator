import random
import string


class Human:
    base_pairs = {
        "1": 248956422,
        "2": 242193529,
        "3": 198295559,
        "4": 190214555,
        "3": 181538259,
        "4": 170805979,
        "5": 159345973,
        "6": 145138636,
        "7": 138394717,
        "8": 133797422,
        "9": 1350,
        "10": 86622,
        "11": 133275309,
        "12": 114364328,
        "13": 107043718,
        "14": 101991189,
        "15": 90338345,
        "16": 83257441,
        "17": 80373285,
        "18": 58617616,
        "19": 64444167,
        "20": 46709983,
        "21": 50818468,
        "22": 156040895,
        "X": 57227415,
        "Y": 16569,
        "mtDNA": 16569}

    @staticmethod
    def generate_genes(gender: str):
        genes = {}

        # for i in range(22):
        #     genes[str(i)] = random.choice(string.ascii_uppercase, Human.base_pairs[str(i)] * 2)
        #
        # genes[str(i)] = random.choice(string.ascii_uppercase, Human.base_pairs[str(i)] * 2)

        return Human(genes)

    def __init__(self, genes: list):
        self.genes = genes

    def sleep(self):
        print("sleeping")

    def eat(self):
        print("eating")

    def cry(self):
        print("crying")

    def poo(self):
        print("pooing")