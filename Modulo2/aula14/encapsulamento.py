class Conta():
    def __init__(self, saldo):
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        self._saldo = saldo

conta1 = Conta(200)
conta2 = Conta(300)
conta3 = Conta(-100)

print(conta1.get_saldo(), conta2.get_saldo(), conta3.get_saldo())

conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())

print(conta3.get_saldo())
