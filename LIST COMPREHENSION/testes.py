"""
    [o que quero retornar - loop - condicional (opcional)]
    [expression for value in iterable if condition]
"""

"""
    [1 - 2 - 3]
    [1 - aqui vamos retornar o resultado do que sair no 2 ou 3 --- podemos usar metodos no valor -- p exemplo se eu estiver iterando nomes posso usar o .upper() para capitalizar o valor]
    [1 - posso usar operadores ternarios tambem -- True if number % 2 == 0 Else False]
    [2 - aqui vamos ter o loop]
    [3 - aqui vamos ter a condicional se aplicavel]

    NUMEROS PARES [numero for numero in range(0, 100) if numero % 2 == 0] --- esta lista vai conter numeros pares de 0 ate o 100
"""


# 1. Crie uma lista com os números de 1 a 10.
lista = [number for number in range(1,11)]
print(lista)



# 2. Crie uma lista com o quadrado de cada número de 1 a 10.
quadrado = [number ** 2 for number in range(1,11)]
print(quadrado)

# 3. Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma nova lista contendo apenas os números pares.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [number for number in lista_de_numeros if number % 2 == 0]
print(numeros_pares)


# 4. Dada a lista palavras = ['olá', 'mundo', 'em', 'python'], crie uma nova lista com o comprimento de cada palavra.
lista_palavras = ['olá', 'mundo', 'em', 'python']
comprimento_de_palavra = [len(palavra) for palavra in lista_palavras]
print(comprimento_de_palavra)


# 5. Dada a lista de strings frutas = ['maça', 'banana', 'morango', 'uva'], crie uma nova lista com as frutas escritas em maiúsculo.
frutas = ['maça', 'banana', 'morango', 'uva']
frutas_em_maiusculo = [fruta.upper() for fruta in frutas]
print(frutas_em_maiusculo)


# 6. Dada a lista de inteiros valores = [1, -2, 3, -4, 5, -6], crie uma nova lista com o valor absoluto de cada número.
valores = [1, -2, 3, -4, 5, -6]
absoluto = [abs(number) for number in valores ]
print(absoluto)

# 7. Dada a lista temperaturas = [10, 20, 25, 30], converta cada valor para a escala Fahrenheit (multiplique por 9/5 e some 32).
temperaturas = [10, 20, 25, 30]
Fahrenheit = [(temperatura * 1.8) + 32 for temperatura in temperaturas]
print(Fahrenheit)


# 8. Crie uma lista de todos os números divisíveis por 3 em um intervalo de 1 a 30.
divisiveis = [number for number in range(1,11) if number % 3 == 0]
print(divisiveis)


# 9. Crie uma lista de booleanos indicando se cada número de 1 a 10 é par.
boolean = [True if number % 2 == 0 else False for number in range (1,11)]
print(boolean)


# 10. Dada uma lista de nomes, crie uma nova lista com uma saudação para cada nome, por exemplo, ['Olá, Alice', 'Olá, Bob'].
nomes = ["samuel", "luis", "pablo", "lucas", "henrique", "sansão"]
saudacao = ["Oi " + name for name in nomes]
print(saudacao)


# Nível Básico
# 1. Crie uma lista com os números de 1 a 10.
# 2. Crie uma lista com o quadrado de cada número de 1 a 10.
# 3. Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma nova lista contendo apenas os números pares.
# 4. Dada a lista palavras = ['olá', 'mundo', 'em', 'python'], crie uma nova lista com o comprimento de cada palavra.
# 5. Dada a lista de strings frutas = ['maça', 'banana', 'morango', 'uva'], crie uma nova lista com as frutas escritas em maiúsculo.
# 6. Dada a lista de inteiros valores = [1, -2, 3, -4, 5, -6], crie uma nova lista com o valor absoluto de cada número.
# 7. Dada a lista temperaturas = [10, 20, 25, 30], converta cada valor para a escala Fahrenheit (multiplique por 9/5 e some 32).
# 8. Crie uma lista de todos os números divisíveis por 3 em um intervalo de 1 a 30.
# 9. Crie uma lista de booleanos indicando se cada número de 1 a 10 é par.
# 10. Dada uma lista de nomes, crie uma nova lista com uma saudação para cada nome, por exemplo, ['Olá, Alice', 'Olá, Bob'].
# Nível Intermediário
# 11. Dada uma lista de palavras, crie uma nova lista que contenha apenas as palavras com mais de 4 caracteres.
# 12. Crie uma lista de todos os anos bissextos entre 2000 e 2024. (Dica: anos bissextos são divisíveis por 4, mas não por 100, a menos que sejam divisíveis por 400).
# 13. Dada a lista numeros = [10, 20, 30, 40, 50], crie uma nova lista que contenha o valor de cada número dividido por 10, mas apenas se o número for maior que 25.
# 14. Dada a lista de strings lista_mista = ['1', '2', 'três', '4', 'cinco'], crie uma lista de inteiros apenas para os elementos que podem ser convertidos.
# 15. Crie uma lista de tuplas, onde cada tupla contém um número de 1 a 5 e o seu quadrado.
# 16. Dada uma lista de listas, como matriz = [[1, 2], [3, 4], [5, 6]], crie uma lista plana com todos os elementos.
# 17. Dada uma lista de nomes, crie uma nova lista onde cada nome seja capitalizado (primeira letra maiúscula) apenas se tiver mais de 5 letras.
# 18. Crie uma lista com todos os números de 1 a 50 que são divisíveis por 2 e 5.
# 19. Dada uma lista de palavras, crie um dicionário onde a chave é a palavra e o valor é o seu comprimento.
# 20. Crie uma lista de todas as combinações de números de 1 a 3 em duas listas aninhadas.
# Nível Avançado
# 21. Dada uma lista de frases, crie uma única lista contendo todas as palavras, sem duplicatas.
# 22. Dada uma matriz (lista de listas), crie uma nova lista com os elementos transpostos. Ex: [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]].
# 23. Crie uma lista de todos os pares de coordenadas (x, y) onde x e y variam de 0 a 2.
# 24. Dada uma lista de dicionários, como estudantes = [{'nome': 'Ana', 'nota': 8}, {'nome': 'Carlos', 'nota': 6}], crie uma lista apenas com os nomes dos estudantes que tiraram nota maior ou igual a 7.
# 25. Dada uma lista de listas, filtre as sublistas que contêm pelo menos um número par.
# 26. Crie uma lista de todas as palavras de uma frase, mas com as vogais substituídas por asteriscos.
# 27. Crie uma lista com a soma de cada par de elementos de duas listas de mesmo tamanho, ex: [1, 2, 3] e [4, 5, 6] -> [5, 7, 9].
# 28. Crie uma lista de todos os números primos até 100 usando list comprehension e uma função auxiliar.
# 29. Crie uma lista de tuplas (caractere, código ASCII) para cada caractere de uma string.
# 30. Dada a lista numeros = [1, 2, 3], crie uma lista de todas as permutações possíveis dos elementos.