#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
#
# data: 27/06/2022
#

# 2 - Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se ele é: equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

ladoA = int(input("informe o lado A: ")) # Solicitando um valor inteiro para o LadoA
ladoB = int(input("informe o lado B: ")) # Solicitando um valor inteiro para o LadoB
ladoC = int(input("informe o lado C: ")) # Solicitando um valor inteiro para o LadoC

# O primeiro teste que fazemos é para saber se a soma de quaisquer dois lados é menor que o terceiro lado.
# Se for, esses três valores não formam um triângulo e acabou o programa aí.

if (ladoA + ladoB < ladoC) or (ladoA + ladoB < ladoC) or (ladoA + ladoB < ladoC):
  print("\nNão é um triângulo!")

# Se não for, precisamos testar se é equilátero, isósceles ou escaleno.

elif (ladoA == ladoB) and (ladoA == ladoC):
  print("É um triângulo equilátero!")

# Note que não precisamos comparar os lados A e C, pois se ladoA é igual a ladoB e ladoA é igual a ladoC, então o ladoB vai ser automaticamente igual ao ladoC.
# Se forem todos iguais, diz que é equilátero e acabou aí.
# Se não for equilátero, cai no próximo elif.
# Lá vamos testar se ele tem dois lados iguais: a == b ou a == c ou b == c (notem o OU, que é o operador lógico or).
# Se alguma dessas comparações retornar verdadeiro, o triângulo é isósceles e acaba aí.

elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
  print("É um triângulo isósceles!")

# Porém, se não for isósceles, cai no else final.
# Pois se não é equilátero nem isósceles, e é um triângulo, tem de ser escaleno.

else:
  print("é um triângulo Escaleno!")

print("fim do programa") # Informando ao usuário que o programa terminou
