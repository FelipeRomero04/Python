import time

def voto(birth):
    current_year = time.localtime().tm_year
    old = current_year - birth

    if old < 16:
        return 'NEGATE'
    elif 16 <= old <= 18 or old > 70:
        return 'OPTIONAL'
    else:
        return 'MENDATORY'

while True:
    try:
        birth = int(input('Insert your year of birth: '))
        break
    except Exception:
        print('Please, enter the correct value in the field above!')
        continue


print(voto(birth))
