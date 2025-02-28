from os import system

system('cls')


times_brasileirao_2024 = (
   "Palmeiras", "Grêmio", "Atlético Mineiro", "Flamengo", "Botafogo",
    "Bragantino", "Fluminense", "Athletico Paranaense", "Internacional",
    "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", 
    "Bahia", "Santos", "Vitória", "Juventude", "Atlético Goianiense",
    "Criciúma"
)

time = str(input('Escreva o nome do seu time: '))


print(f'Lista de times do Brasileirão: {times_brasileirao_2024}')
print('=-' * 66)
print(f'Os 5 primeiros são: {times_brasileirao_2024[:5]}')
print(f'=-' * 66)
print(f'Os 4 ultimos são: {times_brasileirao_2024[-4:]}')
print('=-' * 66)
print(f'Times em ordem alfabética: {sorted(times_brasileirao_2024)}')

cont = 0

        
       
        








