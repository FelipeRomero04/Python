# import time

# for _ in range(5):
#     print('.', end='', flush=True)
#     time.sleep(0.5)
# print(' Pronto!')

import sys
import time

sys.stdout = open("output.txt", "w")  # Redireciona stdout para um arquivo (buffer completo)

print("Isso pode demorar a aparecer no arquivo...", end="")  # Nenhum flush automático aqui
time.sleep(5)  # Simulando uma pausa longa

# Agora forçamos a gravação imediata
     
