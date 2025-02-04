'''cid = str(input('Qual cidade você nasceu? ')).strip()
cid = cid.lower().split()

print('santo' in cid[0])
'''

# Outro método

cid = str(input('Qual cidade você nasceu? ')).strip()

print(cid.lower().startswith('santo')) # Retorna True se começar com 'santo'




