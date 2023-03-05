#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

numero = int(input("Informe um número: "))

# calcula a sequência de Fibonacci até o número informado
fibonacci = [0, 1]
while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# verifica se o número informado pertence à sequência
if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
