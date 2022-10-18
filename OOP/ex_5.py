from abc import abstractclassmethod, ABC

class Pizza(ABC):
    pedacos = 8
    
    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos
    
    #metaclasse
    #usa-se para não precisar ter que tratar todos os static methods
    #abstractmethod são uncallabels
    @staticmethod
    @abstractclassmethod
    def ingredientes():
        return 'Ingredientes'

class Mussarela(Pizza):
    
    #polimorfismo
    @staticmethod
    def ingredientes():
        return ['queijo', 'molho de tomate', 'oregano', 'azeitona']
    