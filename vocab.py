
import asyncio
import aiohttp
import string
import json
import os
import glob

BASE = ('http://www.academia.org.br/sistema_busca_palavras_portuguesas'
        '/volta_voca_org.asp?palavra=')

TIMEOUT = 300

@asyncio.coroutine
def baixar(prefixo):
    letra = prefixo[0]
    caminho = 'data/%s/%s' % (letra, prefixo)
    if glob.glob(caminho+'*'):
        print('OK', caminho)
        return
    busca = prefixo + '*'
    response = yield from aiohttp.request('GET', BASE+busca, timeout=TIMEOUT,
                                            conn_timeout=TIMEOUT)
    print(prefixo, response.status, end=' ')
    if response.status == 200:
        data = yield from response.read()
        html = data.decode('cp1252')
        lista, continua = extrair(html)
        if lista:
            sufixo = '-' if continua else ''
            os.makedirs('data/' + letra, exist_ok=True)
            nome_arq = 'data/%s/%s%s.json' % (letra, prefixo, sufixo)
            with open(nome_arq, 'wt', encoding='utf-8') as saida:
                json.dump(lista, saida)
            print('--->', nome_arq, 'salvo')
        else:
            print('nada')
    else:
        print()

def extrair(html) -> (list, bool):
    """extrair lista de vocábulos do html, e indicador de continuação"""
    if 'Nenhuma palavra encontrada' in html:
        return ([], False)
    continua = 'Sua pesquisa retornou mais de 200 linhas' in html

    texto = html.split('<p>')
    lista = []
    for lin in texto:
        lin = lin.replace('</p>', '')
        lin = lin.strip()
        if not lin:
            continue
        if lin.startswith('<'):
            if not continua:  # tag inesperado
                raise SystemExit()
        else:
            lista.append(lin)
    return (lista, continua)


def principal():
    #from vocab_passo2 import gerar_prefixos
    from vocab_passo4 import gerar_prefixos
    tarefas = []
    """
    for prefixo in [c1+c2+c3 for c1 in string.ascii_lowercase
                             for c2 in string.ascii_lowercase
                             for c3 in string.ascii_lowercase
                   ]:
    """
    #for prefixo in string.ascii_lowercase: #gerar_prefixos(1):
    for prefixo in gerar_prefixos(8):
        tarefas.append(baixar(prefixo))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tarefas))

if __name__ == '__main__':
    principal()
