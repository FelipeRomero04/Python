def is_criticality_balanced(temperature, neutrons_emitted):
    neutrons_emitted_second = temperature * neutrons_emitted
    
    if temperature < 800 and neutrons_emitted > 500 and neutrons_emitted_second < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_efficient = (generated_power / theoretical_max_power) * 100

    if percentage_efficient >= 80:
        return 'green'
    elif 80 > percentage_efficient >= 60:
        return 'orange'
    elif 60 > percentage_efficient >= 30:
        return 'red'
    else:
        return 'black'

# def fail_safe(temperature, neutrons_produced_per_second, threshold):

#     value_safe = temperature * neutrons_produced_per_second 
#     ninety_percent_threshold = threshold * 0.90
#     ten_percent_threshold = threshold * 0.10

#     menor = maior = False
#     if value_safe < ninety_percent_threshold:
#         return 'LOW'

#     if value_safe >= ninety_percent_threshold and value_safe < threshold:
#         menor = True  #verifica se value_safe esta 10% abaixo do limite(threshold)

#     if not menor and threshold <= value_safe <= threshold + ten_percent_threshold :
#         maior = True  #verifica se value_safe esta 10% acima do limite(threshold)
    
#     if menor or maior:
#         return 'NORMAL'

#     else:
#         return 'DANGER' 
    
    #FORMA RESUMIDA(CHATGPT)


def fail_safe(temperature, neutrons_produced_per_second, threshold):

    value_safe = temperature * neutrons_produced_per_second
    limite_superior = threshold * 1.10 #110% do threshold
    limite_inferior = threshold * 0.9 #90% do threshold

    if value_safe < limite_inferior:
        return 'LOW'
    
    if limite_inferior <= value_safe <= limite_superior:
        return 'NORMAL'

    else:
        return 'DANGER'

print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))




