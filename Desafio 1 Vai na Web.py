# --------------------01--------------------

nota = float(input("Digite a nota do aluno: "))
if nota >= 6:
  print("Aprovado")
else:
  print("Reprovado")

# --------------------02--------------------

idade = int(input("Digite sua idade: "))

if idade >= 16:
  print("Você pode votar!")
else:
  print("Você ainda não tem idade para votar.")

# --------------------03--------------------

nota = float(input("Digite a nota do aluno: "))

if 90 <= nota <= 100:
  print("Parabéns, você tirou A!")
elif 80 <= nota <= 89:
  print("Muito bem, você tirou B.")
elif 70 <= nota <= 79:
  print("Bom trabalho, você tirou C.")
elif 60 <= nota <= 69:
  print("Fique atento, você tirou D.")
else:
  print("Estude um pouco mais, você tirou F.")

# --------------------04--------------------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma dos dois números é:", soma)

# --------------------05--------------------

senha_correta = "Python123"

senha = input("Digite a senha para acessar o cofre: ")

if senha == senha_correta:
  print("Acesso concedido! Bem-vindo ao cofre.")
else:
  print("Acesso negado. Senha incorreta.")

# --------------------06--------------------

numero = 1

while numero <= 10:
  print(numero)
  numero += 1

# --------------------07--------------------

numeros = [8, 3, 10, 1, 5]
numeros.sort()

print(numeros) 

# --------------------08--------------------

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

print("Primeiro nome:", alunos[0])
print("Último nome:", alunos[-1])

# --------------------09--------------------

numero = float(input("Digite um número: "))

dobro = numero * 2

print("O dobro de", numero, "é", dobro)

# --------------------10--------------------

nome = input("Digite um nome: ")

quantidade_letras = len(nome)

print("O nome", nome, "tem", quantidade_letras, "letras")