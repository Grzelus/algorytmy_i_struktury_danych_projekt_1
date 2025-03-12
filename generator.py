import random

n = int(input("wygeneruj n liczb: "))
min_value = int(input("Podaj minimalną wartość losowanych elementów: "))
max_value = int(input("Podaj maksymalną wartość losowanych elementów: "))

def generate(n,min_value, max_value):
    if(n > 10):
        print("generator może stworzyć maksymalnie ciąg 10-elementowy.")
        return []
    
    if(min_value > max_value):
        print("minimalna wartość nie powinna być większa od maksymalnej.")
        return []

    output = [random.randint(min_value,max_value) for _ in range(n)]
    return output
    