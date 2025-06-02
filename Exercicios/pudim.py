import requests

def status_url(url):
    try:
        conteudo = requests.get(url)
        if conteudo.status_code == 200:
            return 'Consegui acessar o site pudim com sucesso!'
    except Exception:
        return 'O site Pudim não esta acessivel no momento'

print(status_url('https://www.pudim.com.br/'))
