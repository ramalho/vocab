import json
import glob

for nome_arq in sorted(glob.glob('data/?/???-.json')):
    with open(nome_arq) as entrada:
        lista = json.load(entrada)
    print(nome_arq.split('.')[0], lista[-1])

