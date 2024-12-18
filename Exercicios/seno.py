import math

ang = float(input('Digite o angulo que você deseja: '))
conv = math.radians(ang)
sen = math.sin(conv)
cos = math.cos(conv)
tang = math.tan(conv)

print(f'O angulo de {ang} tem o SENO de {sen:.2f}')
print(f'O angulo de {ang} tem o COSSENo de {cos:.2f}')