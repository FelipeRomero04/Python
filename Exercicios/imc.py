altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite o seu peso: (kg) '))

if altura.is_integer():  #para caso a altura esteja como inteiro
    altura = altura / 100

imc = peso/(altura * altura)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Essa pessoa esta ABAIXO DO PESO IDEAL! Aumente seu consumo calórico.')
elif imc < 25:
    print('Essa pessoa está no PESO IDEAL! Mantenha sua alimentação.')
elif imc < 30:
    print('Essa pessoa esta com SOBREPESO! Regule sua alimentação.')
elif imc <= 40:
    print('Você está OBESO! Talvez esteja comendo mais do que pense.')
else:
    print('Você esta com OBESIDADE MORBIDA! Procure um ajuda IMEDIATAMENTE.')
