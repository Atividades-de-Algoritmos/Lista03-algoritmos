#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
# data: 26/06/2022
#

print("informe os valores de a, b e c") # Introduzindo o código
print("exemplo: aX^2 + bX + c = 0\n")

# Entrada de dados

a = int(input("informe o valor de a: ")) # Solicitando um valor inteiro para a
b = int(input("informe o valor de b: ")) # Solicitando um valor inteiro para b
c = int(input("informe o valor de c: ")) # Solicitando um valor inteiro para c

# Processamento de dados

delta = b**2 - 4*a*c  #calculo do delta

# se delta for negativo, não existe raiz
# se delta for igual a zero, existe apenas uma raiz ou duas raízes iguais
# se delta for positivo, existe duas raízes

# Saída de dados

if delta < 0: #se delta for negativo
  print(f"\ndelta = {delta}")
  print("não existe raiz!")

elif delta == 0: #se delta for igual a zero
  print(f"\ndelta = {delta}")
  x1 = x2 = (-b + (delta**(1/2))/(2*a)) #calculo da raiz, x1 = x2
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")

else: #se delta for positivo
  print(f"\ndelta = {delta}")
  x1 = (-b + (delta**(1/2))/(2*a)) #calculo da raiz x1
  x2 = (-b - (delta**(1/2))/(2*a)) #calculo da raiz x2
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")

print("fim do programa") # Informando ao usuário que o programa terminou