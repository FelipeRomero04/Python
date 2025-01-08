reta1 = input('Digite os lados do Triangulo: ').strip()
converter = sorted(list(map(int, reta1.split(','))))


if converter[0] == converter[1] == converter[2]:  #O map transforma todos os numero da lista em inteiros sendo possivel selecionar indivualmente [] no if
    print('O triângulo é EQUILÁTERO')
if max(converter) == converter[1] != min(converter) or max(converter) != converter[1] == min(converter):
    print('Isoceles')
if max(converter) != converter[1] != min(converter):
    print('Escaleno')

