import sys
import csv
import json
import xml.etree.ElementTree as ET

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    # def __init__(self):
    #     self.caminho_arquivo = caminho_arquivo
    #     self.tipo_relatorio = tipo_relatorio

    def make_from_csv(arquivo):
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

    def make_from_json(arquivo):
        return json.load(arquivo)

    def make_from_xml(arquivo):
        report_data = []
        tree = ET.parse(arquivo)
        root = tree.getroot()
        for child in root:
            report_item = {}
            for element in child:
                report_item[element.tag] = element.text
            report_data.append(report_item)
        return report_data

    def import_data(caminho_arquivo, tipo_relatorio):
        report_data = []
        with open(caminho_arquivo) as arquivo:
            if caminho_arquivo[-4:] == ".csv":
                report_data = Inventory.make_from_csv(arquivo)
            elif caminho_arquivo[-5:] == ".json":
                report_data = Inventory.make_from_json(arquivo)
            elif caminho_arquivo[-4:] == ".xml":
                report_data = Inventory.make_from_xml(arquivo)
        if tipo_relatorio == "simples":
            relatorio = SimpleReport.generate(report_data)
        elif tipo_relatorio == "completo":
            relatorio = CompleteReport.generate(report_data)
        return relatorio
