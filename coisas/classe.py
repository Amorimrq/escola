class casa:
    def __init__(self, tamanho, numero, cor):
        self.tamanho = tamanho
        self.numero = numero
        self.cor = cor

    def mostrar (self):
        print(self.tamanho, self.numero, self.cor)   



pedro = casa(tamanho='80', numero='629', cor='verde')
pedro.mostrar()