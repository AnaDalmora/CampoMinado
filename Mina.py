import random
class Mina:
    def __init__(self):
        self.tem_mina = self.gerar_mina()
        self.revelada = False
    
    def gerar_mina(self):
        # 15% chance de mina (1), 85% chance sem mina (0)
        return 1 if random.random() < 0.15 else 0