class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo


# Uso
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(f"Saldo final: {cuenta.obtener_saldo()}")
