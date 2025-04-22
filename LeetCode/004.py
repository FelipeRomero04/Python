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

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    percentage_safe = temperature * neutrons_produced_per_second
    percentage_threshold = 90 * threshold / 100
    print(percentage_safe)
    print(percentage_threshold)

fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)





