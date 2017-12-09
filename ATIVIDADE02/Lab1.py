# -*- coding: utf-8 -*-

import numpy as np

class FuncionalW(object):
    def __init__(self, data):
        self.data = data
    def map(self, function):
        """Call `map` on the items in `data` using the provided `function`"""
        return FuncionalW(map(function, self.data))
    def reduce(self, function):
        """Call `reduce` on the items in `data` using the provided `function`"""
        return reduce(function, self.data)
    def filter(self, function):
        """Call `filter` on the items in `data` using the provided `function`"""
        return FuncionalW(filter(function, self.data))
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
    def __getattr__(self, name):  return getattr(self.data, name)
    def __getitem__(self, k):  return self.data.__getitem__(k)
    def __repr__(self):  return 'FuncionalW({0})'.format(repr(self.data))
    def __str__(self):  return 'FuncionalW({0})'.format(str(self.data))


# EXERCICIO 2a
# Crie uma array numpy com os valores 1, 2, 3
arraySimples = np.array([1,2,3])

# Faça o produto escalar multiplicando a array por 5
vezesCinco = arraySimples * 5
print arraySimples
print vezesCinco

# TESTE do exercício (2a)
assert np.all(vezesCinco == [5, 10, 15]), 'valor incorreto para vezesCinco'
print "Correto!"



# EXERCICIO 2b
# A função np.arange(inicio,fim,passo)  cria uma lista iniciando em inicio, terminando antes do fim seguindo passo
u = np.arange(0, 5, .5)   # np.array([0,0.5,1.0,...,4.5])
v = np.arange(5, 10, .5)

elementoAelemento = u * v
prodInterno = np.dot(u, v)
print 'u: {0}'.format(u)
print 'v: {0}'.format(v)
print '\nelementoAelemento\n{0}'.format(elementoAelemento)
print '\nprodInterno\n{0}'.format(prodInterno)

# TESTE do exercício 2b
assert np.all(elementoAelemento == [ 0., 2.75, 6., 9.75, 14., 18.75, 24., 29.75, 36., 42.75]), "Valores incorretos para elementoAelemento"
print "Primeiro teste OK"
assert prodInterno==183.75, "Valor incorreto para prodInterno"
print "Segundo teste OK"



# EXERCICIO 2c
from numpy.linalg import inv  # agora podemos utilizar o comando inv() sem preceder com np.linalg

# Criar uma matriz com listas de listas
A = np.matrix([[1,2,3,4],[5,6,7,8]])
print 'A:\n{0}'.format(A)

# Imprima a matriz transposta
print '\nA transposta:\n{0}'.format(A.T)

# Multiplique A por sua Transposta
AAt = A * A.T
print '\nAAt:\n{0}'.format(AAt)

# Inverta AAt com o comando inv()
AAtInv = inv(AAt)
print '\nAAtInv:\n{0}'.format(AAtInv)

# Mostre que a matriz vezes sua inversa é a identidade
# .round(n) arredonda os valores para n casas decimais
print '\nAAtInv * AAt:\n{0}'.format((AAt * inv(AAt)).round(4))

# TESTE do exercício (2c)
assert np.all(AAt == np.matrix([[30, 70], [70, 174]])), "Valores incorretos para AAt"
print "Primeiro teste OK"
assert np.allclose(AAtInv, np.matrix([[0.54375, -0.21875], [-0.21875, 0.09375]])), "Valor incorreto para AAtInv"
print "Segundo teste OK"

# EXERCICIO 2d
atributos = np.array([1, 2, 3, 4])
print 'atributos:\n{0}'.format(atributos)

# Crie uma array com os 3 últimos elementos de atributos
ultTres = atributos[-3:]

print '\nÚltimos três:\n{0}'.format(ultTres)

# TEST do exercício (2d)
assert np.all(ultTres == [2, 3, 4]), "Valores incorretos para ultTres"
print "Teste OK"

# ---------------------------------------- PARTE 3

# EXERCICIO 3a
# Lembre-se que: "lambda x, y: x + y" cria uma função que adiciona dois valores
mult10 = lambda x: x*10
print mult10(5)

# Note that the function still shows its name as <lambda>
print '\n', mult10

assert mult10(10)==100, "Função incorreta"
print "Teste OK"


# EXERCICIO 3C

# Escreva uma função Soma(x) que retorna uma função que recebe um valor y e soma ao x.
def Soma(x):
	def fsoma(y):
		return x + y
	return fsoma

Soma2 = lambda a,b: Soma(a)(b)
Soma3 = lambda a,b,c: Soma(Soma(a)(b))(c)

print Soma2(1,3), Soma3(1,2,3)

assert Soma3(1,2,3)==6, "Erro na função"
print "Ok soma"


# EXERCICIO 3d

dataset = FuncionalW(range(10))

# Multiplique cada elemento por 5
mapResult = dataset.map(lambda x: x*5)

# Filtre eliminando os elementos ímpares
# No Python "x % 2" é o resultado do resto da divisão de x por 2
filterResult = dataset.filter(lambda x: x%2 == 0)

# Some os elementos
reduceResult = dataset.reduce(lambda x, y: x+y)

print 'mapResult: {0}'.format(mapResult)
print '\nfilterResult: {0}'.format(filterResult)
print '\nreduceResult: {0}'.format(reduceResult)

assert mapResult == FuncionalW([0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),"Valor incorreto para mapResult"
print "Teste 1 OK"

assert filterResult == FuncionalW([0, 2, 4, 6, 8]), "Valor incorreto para filterResult"
print "Teste 2 OK"

assert reduceResult == 45, "Valor incorreto para reduceResult"
print "Teste 3 OK"

# EXERCICIO



# split() divide a string em palavras
Texto = FuncionalW("Esse texto tem varias palavras cada linha tem palavras escritas Esse texto esta escrito".split())

# Vamos fazer uma contagem da palavra 'palavras' no texto

# Crie uma função lambda que recebe duas entradas e retorna se são iguais ou não
Igual = lambda x, y : x == y

# Crie uma função lambda que utiliza a função Igual para detectar se a entrada é igual a palavra 'palavras'
DetectaPalavra = lambda x: Igual(x, 'palavras')

# 1) Filtre as palavras iguais a 'palavras'
# 2) Mapeie todos os elementos para o valor 1
# 3) Reduza para a somatória
contagem = (Texto
            .filter(DetectaPalavra)
            .map(lambda x: 1)
            .reduce(lambda x, y: x+y)
            )

print "Existem {} ocorrências de 'palavras'".format(contagem)
