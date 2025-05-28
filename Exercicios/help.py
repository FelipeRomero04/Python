import time

def modulo_import(modulo):
    import importlib

    modulo = importlib.import_module(modulo)
    return modulo

def document_library(modulo):
    import pydoc
    try:
        print(pydoc.render_doc(modulo_import(modulo)))
    except Exception:
        print('Modulo não encontrado. Tente novamente!')


while True:
    print('~' * 30)
    print('Sitema de ajuda PyHelp')
    print('~' * 30, '\n')

    func = input('Função ou biblioteca > ')
    if func == '':
        print('~' * 20)
        print('Até logo')
        print('~' * 20)
        time.sleep(1)
        break

    print('~' * 30)
    print(f'Acessando o manual de comando \'{func}\'')
    print('~' * 30, '\n')
    time.sleep(3)

    document_library(func)
    time.sleep(2)


       

