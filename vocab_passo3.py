import json
import glob
import unicodedata
import string


def remover_acentos(txt):
    cars = unicodedata.normalize('NFKD', txt)
    octetos = cars.encode('ASCII', 'ignore')
    return octetos.decode('ASCII')


def normalizar(txt):
    return remover_acentos(txt).lower()


def gerar_prefixos(tamanho=0):
    with open('emendas-hifenadas.txt') as arq:
        palavras = [lin for lin in arq.readlines() if lin[0] == '\t']
        for pal in palavras:
            pal = pal.strip()
            prefixo, resto = pal.split('-', 1)
            print(prefixo, '--', resto)
            indice = string.ascii_lowercase.find(resto[0])
            if indice >= 0:
                finais = string.ascii_lowercase[indice:]
                #print(prefixo[:3], finais)
                for letra in finais:
                    yield normalizar(prefixo + '-' + letra)


if __name__=='__main__':
    for i in gerar_prefixos():
        print('\t', i)


