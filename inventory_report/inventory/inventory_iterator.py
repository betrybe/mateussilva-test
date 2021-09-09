from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, lista):
        self.lista = lista
        self.posicao = 0

    def __iter__(self):
        return self

    # Retornar próximo valor na lista
    def __next__(self):
        try:
            value = self.lista[self.posicao]
            self.posicao += 1
        except IndexError:
            raise StopIteration()
        return value
