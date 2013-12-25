import sys
import json
import os
import util

vistas = set()

def main(raiz):
    for path, subdirs, arqs in os.walk(raiz):
        print(path)
        for arq in arqs:
            if arq.endswith('.json'):
                path_arq = os.path.join(path, arq)
                with open(path_arq) as arq_json:
                    lista = json.load(arq_json)
                    if lista:
                        for pal in lista:
                            vistas.add(pal)

    for pal in sorted(vistas, key=util.chave):
        print(pal)


if __name__=='__main__':
    main(sys.argv[1])
