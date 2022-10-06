class MeuErro(Exception):
    
    #para personalizar a mensagem de erro
    def __init__(self, msg):
        self.msg = msg
    
    
    def __str__(self):
        return f'Erro criado por mim: {self.msg}'
    
raise MeuErro('Msg personalizada')
