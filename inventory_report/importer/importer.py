import abc


class Importer(abc.ABC):
    @abc.abstractclassmethod
    def import_data(self, caminho_arquivo):
        pass
