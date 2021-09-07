import sys

# from collections.abc import Iterator
from .inventory_iterator import InventoryIterator
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer):
        self.importer = importer
        self.posicao = 0
        self.data = []

    # Retornar Iterador
    def __iter__(self, lista):
        return InventoryIterator(lista)

    # Adicionar itens a lista
    def add_data(self, item):
        self.data.append(item)

    # Utilizar método import_data da classe de importação dependendo do
    # argumento passado para a Classe InventoryRefactor
    def import_data(self, caminho_arquivo):
        for item in self.importer.import_data(self, caminho_arquivo):
            self.add_data(item)
        return self.data
