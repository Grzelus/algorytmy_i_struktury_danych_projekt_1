import random

n = int(input("wygeneruj n liczb: "))
min_value = int(input("Podaj minimalną wartość losowanych elementów: "))
max_value = int(input("Podaj maksymalną wartość losowanych elementów: "))

def generate(n,min_value, max_value):
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []

    output = [random.randint(min_value,max_value) for _ in range(n)]
    return output
    