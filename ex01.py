#

#entrada de dados
a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

#calculo do delta
delta = b**2 - 4*a*c

if delta < 0:
  print(f"delta = {delta}")
  print("não existe raiz!")
elif delta == 0:
  print(f"delta = {delta}")
  x1 = x2 = (-b + (delta**(1/2))/(2*a))
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")
else:
  print(f"delta = {delta}")
  x1 = (-b + (delta**(1/2))/(2*a))
  x2 = (-b - (delta**(1/2))/(2*a))
  print(f"a raiz x1 é {x1}")
  print(f"a raiz x2 é {x2}")

#saída de dados
#se sair aqui dar erro quando o delta for zero
#print(f"a raiz x1 é {x1}")
#print(f"a raiz x2 é {x2}")