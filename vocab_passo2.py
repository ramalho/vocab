import json
import glob
import unicodedata
import string

def remover_acentos(txt, codif='utf-8'):
    return unicodedata.normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

"""
bio-historiador
oxi-hidrila
pau-de-bicho
"""

TAM_PREFIX = 4

def gerar_prefixos(tamanho=TAM_PREFIX):
    interr = '?' * (tamanho-1)
    for nome_arq in sorted(glob.glob('data/?/%s-.json' % interr)):
        with open(nome_arq) as entrada:
            lista = json.load(entrada)
        ultima = lista[-1]
        prefixo = remover_acentos(ultima[:tamanho])
        indice = string.ascii_lowercase.find(prefixo[-1])
        if indice >= 0:
            finais = string.ascii_lowercase[indice:]
            #print(prefixo[:3], finais)
            for letra in finais:
                yield prefixo[:tamanho-1] + letra

