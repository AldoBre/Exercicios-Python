#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# ## Exercícios Cap02



# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
a = 1,2,3,4,5,6,7,8,9,10
lista = [a]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
teste = ["leite","5","ola","eu","nos","esse é o 5"]
print(teste)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
a = "eu"
b = " consegui"
c = a + b
print(c + " programar")

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
teste = (1,2,2,3,4,4,4,5)
teste.count(4)

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dici = {}
print(dici)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dici2 = {"key 1":5,"key 2":2,"key 3":6}
print(dici2)
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dici2["key add"] = 28
print(dici2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dici3 = {"key1":10,"key2":20,"key3":[10,20]}
print(dici3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista3 = ["string",("tupla1","tupla2"),{"dici1":10,"dici2":20},10.8]
print(lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>

# Parabéns se você chegou até aqui. Use o voucher PYTHONDSA9642 para comprar qualquer curso ou Formação da DSA com 5% de desconto.
