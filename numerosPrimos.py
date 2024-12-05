
numeros = [];
contador_primos = 0;

for i in range(5):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)
for num in numeros:
    if num > 0:
        is_primo = True
    for v in range (2, num):
        if num % v == 0:
            is_primo = False
            break
    if is_primo:
        contador_primos += 1
print(f"Tienes {contador_primos} numeros primos.")
