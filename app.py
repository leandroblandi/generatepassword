# -*- coding: utf-8 -*-
#!/bin/env python

__author__ = "el3be@bgh"

# modulos
import sys, string
import secrets

# variables
abc = string.ascii_letters
num = "1234567890"
sim = "#$%@"
comb = abc + num + sim

# funcion que genera la contraseña
def generar(largo_contraseña):
	contraseña = "".join(secrets.choice(comb) for contraseña in range(largo_contraseña))
	return f"Tu contraseña es: {contraseña}"

# funcion principal
def main():
	largo_contraseña = int(input("Cuantos caracteres: "))
	while largo_contraseña == "" or largo_contraseña == " ":
		 largo_contraseña = int(input("Cuantos caracteres: "))
	else:
		pass
	print(generar(largo_contraseña))
	
# punto de ejecucion
if __name__ == '__main__':
	main()