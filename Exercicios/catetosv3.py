reta = str(input('Digite os segmentos do triângulo: '))
lista = sorted(list(map(float, reta.split(','))))

if max(lista) < min(lista) + lista[1]:
    tria = 'ISOCÉLES'
    if max(lista) != lista[1] != min(lista):
        tria = 'ESCALENO'
    elif max(lista) == lista[1] == min(lista):
        tria = 'EQUILÁTERO'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tria}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

#A VAR TRIA DEVE SER CRIADA PRIMEIRA TBM, JA QUE FOR CRIADA DENTRO DO IF E DPS DO PRINT, O {} NAO IRA RECONHECER A VAR

#O print teve que ficar por ultimo dentro do primero IF, para primeiro confirmar as condições e alocar a variavel da condição verdadeira



#METODO ACIMA 100% OTIMIZADO CRIADO PELA MINHA CABEÇA, O DEBAIXO TBM MAS EU TAVA BURRO




'''reta = str(input('Digite as reta de um triângulo: ')).strip() 
lista = sorted(list(map(float, reta.split(','))))
#NAO SE PODE USAR STRIP(SERVE PRA N CAUSAR PROBLEMAS NO ESPAÇAMENTO USANDO ',') EM UM INT OU FLOAT, LOGO FAÇA UMA VAR CONVERTENDO PRA INT E LISTA SORTED

if max(lista) == lista[1] + min(lista) or max(lista) > min(lista) + lista[1]:
    print('Estes segmentos não podem formar um triãngulo!')

elif max(lista) != lista[1] != min(lista):
    print(f'Os segmentos acima formam um triangulo ESCALENO')

elif max(lista) != lista[1] or max(lista) != min(lista) :
    print(f'Os segmentos acima podem formar um triângulo ISÓCELES.')

elif max(lista) == lista[1] == min(lista):
    print(f'Os segmentos acima podem formar um triângulo EQUILÁTERO.')'''