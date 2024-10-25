#Questão 1
a = '5'
b = 2
c = a * b
print(c)

#Este código não gera um TypeError. O resultado é a repetição da string. O código irá gerar a saída:
#O código gera a saída '55', alternativa c

#Questão 2

for i in range(1, 5):
    if i % 2 == 0:
        print(i, end=' ')

#Esse código imprime apenas os números pares entre 1 e 4, ou seja, 2 e 4.
#B. Saída 2 4

#Questão 3

def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)

print(func(3))

#Função recursiva que calcula o fatorial. Para func(3), o cálculo seria:
#3 * func(2) = 3 * 2 * func(1) = 3 * 2 * 1 * func(0) = 3 * 2 * 1 * 1 = 6
#B. Saída 6

#Questão 4

lista = [1, [2, 3], 4]
print(lista[1][1])

#O código tem o elemento de índice 1 na sublista [2, 3], que é o número 3.
#C. Saída 3

#Questão 6

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz)-i]
    return soma

#Esse código está incorreto porque o índice len(matriz)-i acessa o indíce inválido causando um INDEX ERROR.
#Alternativa A 

#Questão 7

#Código A
lista = [x for x in range(5)]
print(lista)

#Código B
lista = list(range(5))
print(lista)

#Código C
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista)

#O Código A utiliza uma compreensão de lista para gerar a lista [0, 1, 2, 3, 4]
#O Código B transforma o range diretamente em uma lista [0, 1, 2, 3, 4]
#O Código C usa um loop while para preencher a lista com de 0 a 4, resultando em [0, 1, 2, 3, 4]

#Letra D. Todos os códigos A, B e C
#A questão foi respondida com a letra b (Apenas Código B e Código C), mas a resposta correta deveria incluir o Código A também.
#Os três códigos fazem exatamente a mesma coisa, apenas usando diferentes abordagens de iteração ou de criação de listas.

#Questão 8
#IMC = peso / altura²
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc}')

if imc < 17:
    print('Muito abaixo do peso')
elif imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso Normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')

#Dependendo dos valores de peso e altura fornecidos como entrada, o IMC será calculado e exibido.
#O código original foi realizado via if e then de jeito errado.

#Questão 9

# Código da questão
alpha = float(input('Informe alpha: '))
x = float(input('Informe x: '))

if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

#Alpha   x     Saída Esp.                     Justificativa
#0.05   -2     -0.1                           α×x=0.05×−2
#0.05    2      2                             x≥0, imprime x
#0.2     -1    "Valor inválido para alpha"   α>0.1, mensagem de erro
#0.1     -3     -0.3                          α.x=0.1×−3
#0.1     4      4                             x≥0, imprime x