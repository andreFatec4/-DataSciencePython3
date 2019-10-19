#Exercícios: 
import random
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
import math

def quantidade_de_usuarios_na_rede ():
    return 5

def gera_usuarios (qtde_usuarios_na_rede):
    usuarios = []
    u = 0
    for _ in range (qtde_usuarios_na_rede):
        usuarios.append (u)
        u += 1
    return (usuarios)

def test_gera_usuarios ():
    print(gera_usuarios(quantidade_de_usuarios_na_rede()))


def gera_sexo (qtde_usuarios_na_rede):
    sexo = []
    for _ in range (qtde_usuarios_na_rede):
        i = 0
        u1 = 0
        while (i < qtde_usuarios_na_rede):
            u1 = random.randint(0, 25) 
            i += 1
        sexo.append (u1 % 2)
    return (sexo)   

def test_gera_sexo ():
    print(gera_sexo(quantidade_de_usuarios_na_rede()))


def gera_lista_tuplas (l1, l2):
    lt = []
    i = 0
    while (i < len(l1)):
        a = (l1[i]), l2[i]
        lt.append (a)
        i += 1
    return lt

def test_gera_lista_tuplas_sexo ():
    #l1 = gera_usuarios (quantidade_de_usuarios_na_rede ())
    #l2 = gera_sexo (quantidade_de_usuarios_na_rede ())
    #print(l1)
    #print (l2)
    print (gera_lista_tuplas (gera_usuarios(quantidade_de_usuarios_na_rede ()), gera_sexo (quantidade_de_usuarios_na_rede ())))


def contem (amizade, amizades):
    for e1, e2 in amizades:
        if (amizade[0] == e1 and amizade[1] == e2) or (amizade[0] == e2 and amizade[1] == e1):
            return True
    return False

def gera_amizades (numero_conexoes_desejado, qtde_usuarios_na_rede):
    conexoes = []
    for _  in range (numero_conexoes_desejado):
        u1 = None
        u2 = None
        while u1 == u2 or contem((u1, u2), conexoes):
            u1 = random.randint(0, qtde_usuarios_na_rede - 1) # gera valores de a a b,
            u2 = random.randint(0, qtde_usuarios_na_rede - 1) # gera valores de a a b,
        else: conexoes.append ((u1, u2))
    return [x for x in set(conexoes)]    

def test_gera_amizades ():
    print(gera_amizades(20, quantidade_de_usuarios_na_rede()))


def amizades_por_usuario(usuario, amizades, lt):
    lamizades = []
    fem = 0
    mas = 0
    sujeito = 0
    for e in amizades:
        sujeito = usuario
        if (e[0] == usuario):
            lamizades.append(e)
            for n in lt:
                if (e[1] == n[0] and n[1] == 0):
                    fem += 1
                if (e[1] == n[0] and n[1] == 1):
                    mas += 1
        if (e[1] == usuario):
            lamizades.append(e)
            for n in lt:
                if (e[0] == n[0] and n[1] == 0):
                    fem += 1
                if (e[0] == n[0] and n[1] == 1):
                    mas += 1
    #print (lt)
    #print (lamizades)
    return (sujeito,fem, mas)

def test_amizades_por_usuario():
    usuarios = gera_usuarios(quantidade_de_usuarios_na_rede ())
    sexo = gera_sexo (quantidade_de_usuarios_na_rede ())
    ls = []
    lt = gera_lista_tuplas (usuarios, sexo)
    #print (lt)
    amizades = gera_amizades(20, quantidade_de_usuarios_na_rede())
    for u in usuarios:
        ls.append(amizades_por_usuario(u, amizades, lt))
    print (ls)
    return ls

# 1 Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas 
# de cada sexo têm.
def gera_histograma_contagem_amigos_por_sexo(list):
    usuario = [x[0] for x in list]
    barWidth = 0.3
    indice = np.arange(len(list))
    fig, ax = plt.subplots()
    mulheres = plt.bar(indice, [x[1] for x in list], color='red', width=barWidth, label= 'mulheres')
    homens = plt.bar(indice+barWidth, [x[2] for x in list], color='blue', width=barWidth, label= 'homens')
    plt.axis ([-0.5, quantidade_de_usuarios_na_rede() + 0.5, -0, (quantidade_de_usuarios_na_rede() * 0.75)]) 
    plt.title ("Histograma da Contagem de Amigos divididos por sexo")
    plt.xlabel ("usuário")
    plt.xticks ([i for i in range(quantidade_de_usuarios_na_rede())])
    plt.ylabel ("número de amigos")
    plt.yticks ([i for i in range(quantidade_de_usuarios_na_rede())])
    plt.legend()
    plt.tight_layout() 
    plt.show()

def test_gera_histograma_contagem_amigos_por_sexo():
    gera_histograma_contagem_amigos_por_sexo (test_amizades_por_usuario())

# 2 Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas
# de cada idade têm.
def gera_idade (qtde_usuarios_na_rede):
    idade = []
    for _ in range (qtde_usuarios_na_rede):
        i = 0
        u1 = 0
        while (i < qtde_usuarios_na_rede):
            u1 = random.randint(10, 75) 
            i += 1
        idade.append (u1)
    return (idade)   

def test_gera_idade ():
    print(gera_idade(quantidade_de_usuarios_na_rede()))

def test_gera_lista_tuplas_idade ():
    l1 = gera_usuarios (quantidade_de_usuarios_na_rede ())
    l2 = gera_idade (quantidade_de_usuarios_na_rede ())
    print (gera_lista_tuplas (l1, l2))


def quantidade_de_amigos(amizades):
    a = Counter (i for i, _ in amizades)
    b = Counter (i for _, i in amizades)
    tudo = a + b
    #print (a)
    #print (b)
    #print (tudo)
    res = tudo.items()
    #print (res)
    return res

def test_quantidade_de_amigos ():
    amizades = gera_amizades (10, quantidade_de_usuarios_na_rede())
    quantidade_de_amigos(amizades)


def gera_histograma_contagem_amigos_por_idade(lt, la):
    idade = [x[1] for x in lt]
    amigos = []
    i = 0
    while (i < len(la)):
        for x in la:
            if (x[0] == i):
                amigos.append(x[1])
                i += 1        
    #print (amigos)
    barWidth = 0.8
    plt.bar(idade, amigos)
    plt.axis ([5, 76 + 0.5, 0, (quantidade_de_usuarios_na_rede() * 0.75)]) 
    plt.title ("Histograma do Número de Amigos por Idade do usuario")
    plt.xlabel ("usuário")
    plt.ylabel ("número de amigos")
    plt.yticks ([i for i in range(quantidade_de_usuarios_na_rede())])
    plt.legend()
    plt.tight_layout() 
    plt.show()

def test_gera_histograma_contagem_amigos_por_idade():
    lt = gera_lista_tuplas (gera_usuarios (quantidade_de_usuarios_na_rede ()), gera_idade (quantidade_de_usuarios_na_rede ()))
    la = quantidade_de_amigos (gera_amizades (6, quantidade_de_usuarios_na_rede()))
    print (lt)
    print (la) 
    gera_histograma_contagem_amigos_por_idade (lt, la)


# 3 Escreva uma função que calcula a variância e o desvio padrão da idade das pessoas do 
# sexo masculino que tenham pelo menos 22 anos.
def media_idade (n_usuarios, lista_idades):
    media = sum(lista_idades) / n_usuarios
    return media

def test_media_idade ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    lista_idades = gera_idade(quantidade_de_usuarios_na_rede())
    print (media_idade (qtde_usuarios, lista_idades))


def variancia_menores_de_23 (lista_idades, media_idade):
    x = []
    var = 0
    for a in lista_idades:
        if a <= 22: 
            n = a - media_idade
            x.append(n**2)
    print (x)
    var =  sum(x) / quantidade_de_usuarios_na_rede()
    return var

def test_variancia_menores_de_23():
    lista_idades = gera_idade(quantidade_de_usuarios_na_rede())
    print (lista_idades)
    media  = media_idade(quantidade_de_usuarios_na_rede(), lista_idades)
    print (media)
    print ("variância: ", variancia_menores_de_23(lista_idades, media))


def desvio_padrao_menores_de_23 (variancia):
    return math.sqrt(variancia)

def test_desvio_padrao_menores_de_23 ():
    lista_idades = gera_idade(quantidade_de_usuarios_na_rede())
    print (lista_idades)
    media  = media_idade(quantidade_de_usuarios_na_rede(), lista_idades)
    print (media)
    variancia = variancia_menores_de_23(lista_idades, media)
    print (variancia)
    print ("desvio-padrão: ", desvio_padrao_menores_de_23(variancia))

def main ():
    pass
    #test_gera_usuarios ()
    #test_gera_sexo ()
    #test_gera_lista_tuplas_sexo ()
    #test_gera_amizades ()
    #test_amizades_por_usuario()
    #test_gera_histograma_contagem_amigos_por_sexo()
    #test_gera_idade ()
    #test_gera_lista_tuplas_idade ()
    #test_quantidade_de_amigos ()
    #test_gera_histograma_contagem_amigos_por_idade()
    #test_media_idade ()
    #test_variancia_menores_de_23()
    test_desvio_padrao_menores_de_23 ()
main ()
