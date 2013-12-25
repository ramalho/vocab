import sys
import json
import os
import unicodedata

"""
data2/a/agua-.json
    água-vai interj.
data2/b/bio-.json
    bio-historiador s.m.
data2/c/capim-.json
    capim-foice s.m.; pl. capins-foice e capins-foices
data2/c/cipo-.json
    cipó-titora s.m.; pl. cipós-titora e cipós-titoras
data2/e/erva-.json
    erva-doce-bastarda s.f.; pl. ervas-doces-bastardas
data2/o/oxi-.json
    oxi-hidrila (cs) s.f.
data2/p/papa-.json
    papa-roxo s.m.; pl. papa-roxos
data2/p/pau-.json
    pau-de-bicho s.m.; pl. paus-de-bicho
"""

def remover_acentos(txt):
    cars = unicodedata.normalize('NFKD', txt)
    octetos = cars.encode('ASCII', 'ignore')
    return octetos.decode('ASCII')


def normalizar(txt):
    return remover_acentos(txt).lower()


def main(raiz):
    for path, subdirs, arqs in os.walk(raiz):
        for arq in arqs:
            if arq.endswith('-.json'):
                prefixo = arq.split('-')[0]
                path_arq = os.path.join(path, arq)
                with open(path_arq) as arq_json:
                    listar = False
                    lista = json.load(arq_json)
                    ult_lin  = lista[-1]
                    ult_lin_norm = normalizar(ult_lin)
                    if all([    lista,
                                '-' in ult_lin,
                                ult_lin_norm.startswith(prefixo+'-')
                            ]):
                        print(path_arq)
                        print('\t'+lista[-1])




if __name__=='__main__':
    main(sys.argv[1])
