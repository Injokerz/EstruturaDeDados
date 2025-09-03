class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
    
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i],end = ' ')
        print()
        
    def inserir_fim(self,valor):
        self.vetor[self.quant] = valor
        self.quant += 1 

    def esta_cheia(self):
        return self.quant == self.tam
    
    def esta_vazia(self):
        return self.quant == 0 
    
    def remover_fim(self):
        self.quant -= 1

    # def remover(self, valor):
    #     while i < self.quant and self.vetor[i] != valor:
    #         i += 1
    #     if i < self.quant:
    #         for j in range(i,self.quant -1):
    #             self.vetor[j] = self.vetor[j - 1]
    #         self.quant -= 1


