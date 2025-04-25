class FilaCircular:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.fila = [None] * tamanho_max
        self.inicio = 0
        self.fim = -1
        self.qtd = 0

    def esta_vazia(self):
        return self.qtd == 0

    def esta_cheia(self):
        return self.qtd == self.tamanho_max

    def inserir(self, valor):
        if self.esta_cheia():
            print("Não dá pra inserir, fila cheia.")
        else:
            self.fim = (self.fim + 1) % self.tamanho_max
            self.fila[self.fim] = valor
            self.qtd += 1

    def remover(self):
        if self.esta_vazia():
            print("Não tem nada pra remover, fila vazia.")
        else:
            valor_removido = self.fila[self.inicio]
            self.fila[self.inicio] = None  # só pra mostrar melhor
            self.inicio = (self.inicio + 1) % self.tamanho_max
            self.qtd -= 1
            return valor_removido

    def imprimir(self):
        if self.esta_vazia():
            print("Fila vazia.")
        else:
            print("Fila:", end=" ")
            i = self.inicio
            for _ in range(self.qtd):
                print(self.fila[i], end=" ")
                i = (i + 1) % self.tamanho_max
            print()
