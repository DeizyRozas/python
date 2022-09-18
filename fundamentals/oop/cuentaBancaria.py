

class CuentaBancaria:
# atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, numero_cuenta, tasa_int, balance):
        self.numero_cuenta=numero_cuenta
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    @classmethod
    def todos_los_balances(cls):
        sum=0
        for cuenta in cls.todas_las_cuentas:
            sum+=cuenta.balance
        print("este banco tiene un total de", sum)


    def deposito(self, amount):
        self.balance+=amount
        print( "se han depositado", amount)
        return self

    def retiro(self, amount):
        if self.balance>amount:
            self.balance-=amount
        
        else: 
            print("fondos insuficientes: cobrando tarifa de $5")
            self.balance-=5
        return self

    def mostrar_info_cuenta(self):
        print("Balance: $", self.balance)
        return self

    def generar_interes(self):
        if self.balance>0:
            self.balance*= self.tasa_int
        else: print("sin dinero suficiente")
        return self


# cuenta1=CuentaBancaria(1.75, 2000)
# cuenta2=CuentaBancaria(1.60, 150)

# cuenta1.deposito(500).deposito(300).deposito(100).retiro(700).generar_interes().mostrar_info_cuenta()
# cuenta2.deposito(150).deposito(300).retiro(300).retiro(500).retiro(200).retiro(150).generar_interes().mostrar_info_cuenta()
# print(CuentaBancaria.todos_los_balances())

