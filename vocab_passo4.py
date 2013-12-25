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
    prefixo = 'pau-d'
    for letra in string.ascii_lowercase:
        yield normalizar(prefixo + letra)


if __name__=='__main__':
    for i in gerar_prefixos():
        print('\t', i)


