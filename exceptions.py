
class ElectronicsShopError(Exception):
    pass

class InstantiateCSVError(ElectronicsShopError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '"Файл item.csv поврежден"'