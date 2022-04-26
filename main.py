import os

name = str(input("Digite o nome: "))
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))

os.system('clear')

soma = n1+n2+n3+n4
media = soma/4

if (media >= 6):
  print("Nome:",name)
  print('Media:',media)
  print("Aprovado")
if (media >= 3 and media < 6):
  print("Nome:",name)
  print('Media:',media)
  print("Recuperação")
if (media < 3):
  print("Nome:",name)
  print('Media:',media)
  print("Reprovado")