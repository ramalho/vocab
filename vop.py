
import asyncio
import aiohttp
import string
import json
import os

BASE = ('http://www.portaldalinguaportuguesa.org/'
        'advanced.php?action=browse&l1=%s&l2=%s')

TIMEOUT = 300

@asyncio.coroutine
def baixar(letra1, letra2):
    nome_arq = 'data/%s/%s%s.html' % (letra1, letra1, letra2)
    if os.path.exists(nome_arq):
        print('OK', nome_arq)
        return

    busca = BASE % (letra1, letra2)
    response = yield from aiohttp.request('GET', busca, timeout=TIMEOUT,
                                            conn_timeout=TIMEOUT)
    print(letra1+letra2, response.status)
    if response.status == 200:
        data = yield from response.read()
        os.makedirs('data/' + letra1, exist_ok=True)
        with open(nome_arq, 'wb') as saida:
            saida.write(data)
        print('--->', nome_arq, 'salvo')
    else:
        print('***')



def principal():
    tarefas = []
    for letras in [(l1, l2) for l1 in string.ascii_lowercase
                            for l2 in string.ascii_lowercase
                  ]:
        tarefas.append(baixar(*letras))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tarefas))

if __name__ == '__main__':
    principal()
