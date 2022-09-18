from cuentaBancaria import CuentaBancaria

class Usuario:

    
    def __init__(self , name, email_address, numero_cuenta):
        self.name = name
        self.email = email_address
        self.total_cuentas=[]
        self.cuenta= CuentaBancaria(numero_cuenta, tasa_int=0.02, balance=0) 
        self.total_cuentas.append(self.cuenta)

    def abrir_nueva_cuenta(self, numero_cuenta):
        nueva_cuenta= CuentaBancaria(numero_cuenta, tasa_int=0.02, balance=0) 
        self.total_cuentas.append(nueva_cuenta)
        return self

    def mostrar_info_cuentas_usuarios(self):
        for cuenta in self.total_cuentas:
            print("la cuenta", cuenta.numero_cuenta, "del cliente", self.name, "tiene un balance de", cuenta.balance )
        return self


    def balance_usuario(self):
        print( self.name, ", balance: $", self.cuenta.balance)
        return self

    def transfer_dinero(self, other_user, amount):
        self.cuenta.retiro(amount)
        other_user.cuenta.deposito(amount)
        print(self.name, "ha transferido $", amount, "a usuario", other_user.name, ". Nuevos balances:")
        self.balance_usuario()
        other_user.balance_usuario()
        return self

sammi = Usuario("Samantha Roses", "sammi.la.gata@miau.com",1)
zelda = Usuario("Zelda Roses", "black.pincess@miau.com",1)
pepi = Usuario("Pepi rockstar", "pepita.cashupin@guauguau.com",1)

sammi.cuenta.deposito(600).deposito(50).deposito(100)
sammi.balance_usuario().abrir_nueva_cuenta(2).mostrar_info_cuentas_usuarios()
zelda.cuenta.deposito(150).deposito(250).retiro(100).retiro(50)
zelda.balance_usuario()
pepi.cuenta.deposito(1000).retiro(500).retiro(100).retiro(50)
pepi.balance_usuario()
sammi.transfer_dinero(pepi, 350)




