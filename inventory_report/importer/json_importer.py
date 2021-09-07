import sys
import json

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from .importer import Importer


class JsonImporter(Importer):
    def import_data(self, caminho_arquivo):
        try:
            with open(caminho_arquivo) as arquivo:
                if caminho_arquivo[-5:] == ".json":
                    return json.load(arquivo)
                raise ValueError
        except ValueError as ex:
            print("Arquivo inválido")
