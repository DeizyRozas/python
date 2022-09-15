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

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario(self):
        print("Usuario", self.name, ", balance: $", self.balance_cuenta)

    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        print(self.name, "ha transferido", amount, "a usuario", other_user.name, ". Nuevo balance:")
        self.mostrar_balance_usuario()
        other_user.mostrar_balance_usuario()

sammi = Usuario("Samantha Roses", "sammi.la.gata@miau.com")
zelda = Usuario("Zelda Roses", "black.pincess@miau.com")
pepi = Usuario("Pepi rockstar", "pepita.cashupin@guauguau.com")


sammi.hacer_deposito(600)
sammi.hacer_deposito(50)
sammi.hacer_deposito(100)
sammi.mostrar_balance_usuario()
zelda.hacer_deposito(150)
zelda.hacer_deposito(250)
zelda.hacer_retiro(100)
zelda.hacer_retiro(50)
zelda.mostrar_balance_usuario()
pepi.hacer_deposito(1000)
pepi.hacer_retiro(500)
pepi.hacer_retiro(100)
pepi.hacer_retiro(50)
pepi.mostrar_balance_usuario()
sammi.transfer_dinero(pepi, 350)



