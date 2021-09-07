import sys
import xml.etree.ElementTree as ET

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from .importer import Importer


class XmlImporter(Importer):
    def import_data(caminho_arquivo):
        try:
            with open(caminho_arquivo) as arquivo:
                if caminho_arquivo[-4:] == ".xml":
                    report_data = []
                    tree = ET.parse(arquivo)
                    root = tree.getroot()
                    for child in root:
                        report_item = {}
                        for element in child:
                            report_item[element.tag] = element.text
                        report_data.append(report_item)
                    return report_data
                raise ValueError
        except ValueError:
            raise ValueError("Arquivo inválido")
