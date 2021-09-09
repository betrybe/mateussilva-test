import sys
import csv

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "inventory_report")))

from .importer import Importer


class CsvImporter(Importer):
    def import_data(caminho_arquivo):
        try:
            with open(caminho_arquivo) as arquivo:
                if caminho_arquivo[-4:] == ".csv":
                    report_data = []
                    report_item = {}
                    leitor = csv.reader(arquivo, delimiter=",")
                    for linha in leitor:
                        if linha[0] == "id":
                            info = linha
                        else:
                            report_item = dict(zip(info, linha))
                            report_data.append(report_item)
                    return report_data
                raise ValueError
        except ValueError:
            raise ValueError("Arquivo inválido")
