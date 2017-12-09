
from pyspark import SparkContext
from pyspark import SparkConf
sc =SparkContext()



#Exercicio 1a

sc = SparkContext.getOrCreate()
ListaPalavras = ['gato', 'elefante', 'rato', 'rato', 'gato']
palavrasRDD = sc.parallelize(ListaPalavras, 4)
print type(palavrasRDD)

# EXERCICIO  1b


def Plural(palavra):
    """Adds an 's' to `palavra`.

    Args:
        palavra (str): A string.

    Returns:
        str: A string with 's' added to it.
    """
    return str.format('{0}s', palavra)

print Plural('gato')

assert Plural('rato')=='ratos', 'resultado incorreto!'
print 'OK'



# EXERCICIO 1c
pluralRDD = palavrasRDD.map(Plural)
print pluralRDD.collect()


assert pluralRDD.collect()==['gatos','elefantes','ratos','ratos','gatos'], 'valores incorretos!'
print 'OK'

# EXERCICIO 1d
pluralLambdaRDD = palavrasRDD.map(lambda palavra: str.format('{0}s', palavra))
print pluralLambdaRDD.collect()

assert pluralLambdaRDD.collect()==['gatos','elefantes','ratos','ratos','gatos'], 'valores incorretos!'
print 'OK'


# EXERCICIO 1e
pluralTamanho = (pluralRDD
                 .map(lambda x: len(x))
                 ).collect()
print pluralTamanho

assert pluralTamanho==[5,9,5,5,5], 'valores incorretos'
print "OK"

# EXERCICIO 1f
palavraPar = palavrasRDD.map(lambda x: (x,1))
print palavraPar.collect()

assert palavraPar.collect() == [('gato',1),('elefante',1),('rato',1),('rato',1),('gato',1)], 'valores incorretos!'
print "OK"

# ===================================================================== PARTE 2

# EXERCICIO 2a
palavrasGrupo = palavraPar.groupByKey()
for chave, valor in palavrasGrupo.collect():
    print '{0}: {1}'.format(chave, list(valor))

	
assert sorted(palavrasGrupo.mapValues(lambda x: list(x)).collect()) == [('elefante', [1]), ('gato',[1, 1]), ('rato',[1, 1])],'Valores incorretos!'
print "OK"

# EXERCICIO 2b
contagemGroup = palavrasGrupo.mapValues(sum)
print contagemGroup.collect()

assert list(sorted(contagemGroup.collect()))==[('elefante',1), ('gato',2), ('rato',2)], 'valores incorretos!'
print "OK"

# EXERCICIO 2c
contagem = palavraPar.reduceByKey(lambda x, y: x+y)
print contagem.collect()

assert sorted(contagem.collect())==[('elefante',1), ('gato',2), ('rato',2)], 'valores incorretos!'
print "OK"


# EXERCICIO 2d
contagemFinal = (palavrasRDD
                 .map(lambda x: (x,1))
                 .reduceByKey(lambda x, y: x+y)
                 )
				 
print contagemFinal.collect()

assert sorted(contagemFinal.collect())==[('elefante',1), ('gato',2), ('rato',2)], 'valores incorretos!'
print "OK"


# ================================================================== PARTE 3

# EXERCICIO 3a
palavrasUnicas = contagemFinal.count()
print palavrasUnicas

assert palavrasUnicas==3, 'valor incorreto!'
print "OK"



# EXERCICIO 3b
# add e equivalente a lambda x,y: x+y
from operator import add
total = (contagemFinal
         .map(lambda (x, y): y)
         .reduce(add)
         )
media = total / float(palavrasUnicas)
print total
print round(media, 2)

assert round(media, 2)==1.67, 'valores incorretos!'
print "OK"


# ===================================================================== PARTE 4

# EXERCICIO 4a
def contaPalavras(chavesRDD):
    """Creates a pair RDD with word counts from an RDD of words.

    Args:
        chavesRDD (RDD of str): An RDD consisting of words.

    Returns:
        RDD of (str, int): An RDD consisting of (word, count) tuples.
    """
    return (chavesRDD
            .map(lambda x: (x, 1))
            .reduceByKey(add)
           )

print contaPalavras(palavrasRDD).collect()

assert sorted(contaPalavras(palavrasRDD).collect())==[('elefante',1), ('gato',2), ('rato',2)], 'valores incorretos!'
print "OK"


# EXERCICIO 4b
import re
def removerPontuacao(texto):
    """Removes punctuation, changes to lower case, and strips leading and trailing spaces.

    Note:
        Only spaces, letters, and numbers should be retained.  Other characters should should be
        eliminated (e.g. it's becomes its).  Leading and trailing spaces should be removed after
        punctuation is removed.

    Args:
        texto (str): A string.

    Returns:
        str: The cleaned up string.
    """
    return re.sub(r'[^A-Za-z0-9 ]', '', texto).strip().lower()
print removerPontuacao('Ola, quem esta ai??!')
print removerPontuacao(' Sem espaco e_sublinhado!')

assert removerPontuacao(' O uso de virgulas, embora permitido, nao deve contar. ')=='o uso de virgulas embora permitido nao deve contar', 'string incorreta!'
print "OK"


# Apenas execute a celula  4C
import os.path
import urllib2

url = 'http://www.gutenberg.org/cache/epub/100/pg100.txt' # url do livro

arquivo = os.path.join('Data','Aula02','shakespeare.txt') # local de destino: 'Data/Aula02/shakespeare.txt'

if os.path.isfile(arquivo):     # verifica se ja fizemos download do arquivo
    print 'Arquivo ja existe!'
else:
    try:        
        response = urllib2.urlopen(url)
        arquivo = (response.read()).split() #ja gera uma lista de palavras
    except IOError:
        print 'Impossivel fazer o download: {0}'.format(url)

# le o arquivo com textFile e aplica a funcao removerPontuacao        
shakesRDD = (sc
             .textFile(arquivo, 8)
             .map(removerPontuacao)
             )

# zipWithIndex gera tuplas (conteudo, indice) onde indice e a posicao do conteudo na lista sequencial
# Ex.: sc.parallelize(['gato','cachorro','boi']).zipWithIndex() ==> [('gato',0), ('cachorro',1), ('boi',2)]
# sep.join() junta as strings de uma lista atraves do separador sep. Ex.: ','.join(['a','b','c']) ==> 'a,b,c'
print '\n'.join(shakesRDD
                .zipWithIndex()
                .map(lambda (linha, num): '{0}: {1}'.format(num,linha))
                .take(15)
               )
			   

# EXERCICIO 4d
shakesPalavrasRDD = shakesRDD.map(lambda linha: linha.split())
total = shakesPalavrasRDD.count()
print shakesPalavrasRDD.take(5)
print total

# EXERCICIO
shakesPalavrasRDD = shakesRDD.flatMap(lambda x: x.split())
total = shakesPalavrasRDD.count()
print shakesPalavrasRDD.top(5)
print total


assert shakesPalavrasRDD.top(5)==[u'zwaggerd', u'zounds', u'zounds', u'zounds', u'zounds'],'lista incorreta de palavras'
print "OK"



# EXERCICIO 4e
shakesLimpoRDD = shakesPalavrasRDD.filter(lambda s: len(s) != 0)
total = shakesLimpoRDD.count()
print total



# EXERCICIO 4f
top15 = contaPalavras(shakesLimpoRDD).takeOrdered(15, key=lambda (x,y): -y)
print '\n'.join(map(lambda (w, c): '{0}: {1}'.format(w, c), top15))
print "OK1"



