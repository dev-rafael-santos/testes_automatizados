class Banco:
    def __init__(self):
        self.contas = {}
    def incluir_conta(self,conta):
        self.contas[conta.numero] = conta
    def obter_saldo_da_conta(self, numero):
        return self.contas[numero].saldo