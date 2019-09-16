class Conta:

    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura

    def deposita(self, valor):
        self.saldo += valor

    #def saca(self, valor):
    #    self.saldo -= valor

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == false):
            return False
        else:
            destino.deposita(valor)
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}\nnome: {} \nsobrenome: {} \nCPF: {} \n".format(self.numero, self.saldo, self.titular.nome,  self.titular.sobrenome, self.titular.cpf))
        print("data de abertura: {}/{}/{} \n".format(self.dia, self.mes, self.ano))
        
    
class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

#

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
