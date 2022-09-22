from mascotas import Mascota, Perro
from ninja import Ninja

mascota1= Perro("sami", "gato", "churu")
ninja1= Ninja("cho", mascota1, "salmon", "croquetas")

ninja1.alimentar().caminar().bañar()