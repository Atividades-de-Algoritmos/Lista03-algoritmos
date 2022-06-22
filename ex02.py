# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se ele é: equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

ladoA = int(input("informe o lado A: "))
ladoB = int(input("informe o lado B: "))
ladoC = int(input("informe o lado C: "))

# O primeiro teste que fazemos é para saber se a soma de quaisquer dois lados é menor que o terceiro lado.
# Se for, esses três valores não formam um triângulo e acabou o programa aí.
if (ladoA + ladoB < ladoC) or (ladoA + ladoB < ladoC) or (ladoA + ladoB < ladoC):
  print("não é um triângulo!")
# Se não for, precisamos testar se é equilátero, isósceles ou escaleno.
elif (ladoA == ladoB) and (ladoA == ladoC):
  print("é um triângulo equilátero!")
# Note que não precisamos comparar os lados b e c, pois se a é igual a b E TAMBÉM (operador lógico and) a é igual a c, então o lado b vai ser automaticamente igual ao lado c.
# Se forem todos iguais, diz que é equilátero e acabou aí.
# Se não for equilátero, cai no próximo elif.
# Lá vamos testar se ele tem dois lados iguais: a==b ou a==c ou b==c (notem o OU, que é o operador lógico or).
# Se alguma dessas comparações retornar verdadeiro, o triângulo é isósceles e acaba aí.
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
  print("é um triângulo isósceles!")
#Porém, se não for isósceles, cai no else final.
#Pois se não é equilátero nem isósceles, e é um triângulo, tem de ser escaleno.
else:
  print("é um triângulo Escaleno!")