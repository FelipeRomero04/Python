from time import sleep

print('-=-' * 30)
print('Analisador de Triângulos')
print('-=-' * 30)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
lista = sorted([reta1, reta2, reta3]) #para pegar o meio termo de uma lista de 3 variaveis, use sorted() para deixar em ordem crescente e depois selecione o elemento do meio. [1]

print('PROCESSANDO...')
sleep(3)

if max(lista) < min(lista) + lista[1]: 
 #pegando o max da lista significa que mesmo se o maior numero for menor q a soma dos dois menores, poderão formar um trinagulo. eliminando outras situaçoes

    print('os segmento acima PODEM FORMAR um triângulo')
else:
    print('Os segmento acima NÂO PODEM FORMAR um triãngulo')


#OUTRO METODO


'''reta1 = float(input('primeiro reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    #TODAS AS RETAS DEVEM SER MENOR QUE A SOMA DAS OUTRAS
    print('Podem formar um triangulo')
else:
    print('Não podem formar um triângulo')'''




