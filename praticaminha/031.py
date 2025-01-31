linhas = int(input('Digite um numero: '))
item = '*'
espaco = ''

for p in range(1, linhas + 1):
    base = 2 * p - 1
    espaco = linhas - p
    print(' ' * espaco,'*' * base)
   
#     *    
#    ***   
#   *****  
#  ******* 
# *********
  

  # espaco -= ' ' * s

#    base = item * p
#     espaco = linhas - p 
#     print(' '* espaco, base)