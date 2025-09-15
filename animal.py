class Animal:
    def __init__(self, nome, especie, pelagem, classe, tamanho, terreste, aquatico, voador ):
        self.nome = nome
        self.especie = especie
        self.pelagem = pelagem
        self.classe = classe
        self.tamanho = tamanho
        self.terrestre = terreste
        self.aquatico = aquatico
        self.voador = voador
    
    def toString(self):
        print(f'{self.nome},{self.especie},{self.pelagem}, {self.classe}, {self.tamanho}, {self.terrestre}, {self.aquatico}, {self.voador}')
        pass