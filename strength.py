from human import Human


class Papa(Human):
    def __init__(self):
        super().__init__(Human.generate_genes("male"))

    pass


papa = Papa()
