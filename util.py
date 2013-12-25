import re
import unicodedata

abacaxis = '''abacaxi adj. s.2g. s.m.
abacaxibirra s.f.
abacaxi-branco s.m.; pl. abacaxis-brancos
abacaxicultor (ô) s.m.
abacaxicultura s.f.
abacaxicultural adj.2g.
abacaxi-de-tingir s.m.; pl. abacaxis-de-tingir
abacaxiense adj. s.2g.
abacaxi-silvestre s.m.; pl. abacaxis-silvestres
abacaxizado adj.
abacaxizal s.m.
abacaxizar v.
abacaxizeiro s.m.'''

abaces = '''abacé s.m. “abaçá”; cf. ábace
ábace s.m. “besouro”; cf. abacé
abaceias s.f.pl.'''

RE_CLASSE = re.compile('(.*?)\s+(\w+\..*)')

def extrair_verbete(linha):
    partes = RE_CLASSE.search(linha)
    verbete, resto = partes.groups()
    paren = verbete.find('(')
    if paren >= 0:
        pronun = verbete[paren:].strip()
        verbete = verbete[:paren].strip()
    else:
        pronun = ''
        verbete = verbete.strip()
    return verbete, pronun, resto

def remover_acentos(txt):
    cars = unicodedata.normalize('NFKD', txt)
    octetos = cars.encode('ASCII', 'ignore')
    return octetos.decode('ASCII')

def normalizar(txt):
    return remover_acentos(txt).lower().replace('-', '')

def chave(verbete):
    return (normalizar(verbete), verbete)

def testar_extrair_verbete():
    for linha in abacaxis.split('\n'):
        verbete, pronun, resto = extrair_verbete(linha)
        print(verbete, resto, pronun, sep='\t')

def testar_chave():
    linhas = abaces.split('\n')
    linhas.extend(abacaxis.split('\n'))
    for lin in sorted(linhas, key=chave):
        print(lin)



if __name__=='__main__':
    testar_chave()


