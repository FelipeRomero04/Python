var=input('Digite algo: ')

# print('sua variavel e do tipo {}, é um numero/alfabetico? {}, possui somente letras maisculas? {}, possui somente letras minúsculas? {}'.format(type(var), var.isalnum(), var.isalpha(), var.islower()))

# FORMA GUSTAVO GUANABARA

print('O tipo primitivo desse valor é:' ,type(var))
print('Só tem espaços?' ,var.isspace())
print('Só tem caracteres minusculos?' ,var.islower())
print('É alfabético??' ,var.isalpha())

