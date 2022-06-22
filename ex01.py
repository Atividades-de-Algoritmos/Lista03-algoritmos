##entrada de dados
print("informe os valores de a, b e c")
print("exemplo: aX^2 + bX + c = 0")

a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

#calculo do delta
delta = b**2 - 4*a*c  #calculo do delta

# se delta for negativo, não existe raiz
# se delta for igual a zero, existe apenas uma raiz ou duas raizes iguais
# se delta for positivo, existe duas raizes

if delta < 0: #se delta for negativo
  print(f"delta = {delta}")
  print("não existe raiz!")
elif delta == 0: #se delta for igual a zero
  print(f"delta = {delta}")
  x1 = x2 = (-b + (delta**(1/2))/(2*a)) #calculo da raiz, x1 = x2
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")
else: #se delta for positivo
  print(f"delta = {delta}")
  x1 = (-b + (delta**(1/2))/(2*a)) #calculo da raiz x1
  x2 = (-b - (delta**(1/2))/(2*a)) #calculo da raiz x2
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")

