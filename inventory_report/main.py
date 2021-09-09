import sys
import getopt
from inventory.inventory_refactor import InventoryRefactor
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport

import json


def main():
    args = sys.argv
    try:
        # Verificar argumentos passados por linha de comando
        if len(args) != 3:
            raise getopt.error("Verifique os argumentos")
        caminho_arquivo, tipo_relatorio = args[1:]
        # Verificar qual classe utilizar para cada tipo de arquivo
        if caminho_arquivo[-4:] == ".csv":
            instance = InventoryRefactor(CsvImporter)
        elif caminho_arquivo[-5:] == ".json":
            instance = InventoryRefactor(JsonImporter)
        elif caminho_arquivo[-4:] == ".xml":
            instance = InventoryRefactor(XmlImporter)

        # Gerar a lista de dicionários
        report_data = instance.import_data(caminho_arquivo)

        # Gerar relatórios
        if tipo_relatorio == "simples":
            relatorio = SimpleReport(report_data).generate()
        elif tipo_relatorio == "completo":
            relatorio = CompleteReport(report_data).generate()
        else:
            raise getopt.error("Verifique os argumentos")
        # Mostrar relatório
        print(relatorio)

    except getopt.error as err:
        print(str(err), file=sys.stderr)


if __name__ == "__main__":
    main()
