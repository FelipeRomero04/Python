import math

ang = float(input('Digite o angulo que você deseja: '))
conv = math.radians(ang)
sen = math.sin(conv)
cos = math.cos(conv)
tang = math.tan(conv)

print(f'O angulo de {ang} tem o SENO de {sen:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {ang} tem a TANGENTE de {tang:.2f}')