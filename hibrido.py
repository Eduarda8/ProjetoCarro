from carro import carro

class hibrido(carro):

    def __init__(self,cor, modelo, ano):
        super(hibrido, self).__init__(cor, modelo, ano)

    def carregandoBateria(self):
        print("Carregando")
