from human import Human
from baby import Baby


class Mama(Human):
    def __init__(self):
        super().__init__(Human.generate_genes("female"))

    def join(self, papa, on="good_genes", how="inner"):
        # genes_pairs = mama.genes.zip
        return Baby(mama.genes)


mama = Mama()

