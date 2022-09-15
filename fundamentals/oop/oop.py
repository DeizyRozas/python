class Usuario:
# los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
# ahora nuestro metodo tiene 2 parmetros!
    def __init__(self , name, email_address):
# los asignamos en consecuencia
        self.name = name
        self.email = email_address
# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print("Usuario", self.name, ", balance: $", self.balance_cuenta)
        return self

    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        print(self.name, "ha transferido $", amount, "a usuario", other_user.name, ". Nuevo balance:")
        self.mostrar_balance_usuario()
        other_user.mostrar_balance_usuario()
        return self

sammi = Usuario("Samantha Roses", "sammi.la.gata@miau.com")
zelda = Usuario("Zelda Roses", "black.pincess@miau.com")
pepi = Usuario("Pepi rockstar", "pepita.cashupin@guauguau.com")


sammi.hacer_deposito(600).hacer_deposito(50).hacer_deposito(100).mostrar_balance_usuario()
zelda.hacer_deposito(150).hacer_deposito(250).hacer_retiro(100).hacer_retiro(50).mostrar_balance_usuario()
pepi.hacer_deposito(1000).hacer_retiro(500).hacer_retiro(100).hacer_retiro(50).mostrar_balance_usuario()
sammi.transfer_dinero(pepi, 350)



