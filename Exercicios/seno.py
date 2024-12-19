from math import radians, cos, tan, sin

ang = float(input('Digite o angulo que você deseja: '))
conv = radians(ang)
sen = sin(conv)
cos = cos(conv)
tang = tan(conv)

print(f'O angulo de {ang} tem o SENO de {sen:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {ang} tem a TANGENTE de {tang:.2f}')



# Metodo do curso

'''

ang = float(input('Digite o angulo que você deseja: '))
seno = math.radians(math.sin(ang))
cos = math.radians(math.cos(ang))
tang = math.radians(math.tan(ang))

'''