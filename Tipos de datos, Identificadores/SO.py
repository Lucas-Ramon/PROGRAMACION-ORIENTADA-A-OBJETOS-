# Uso de generadores para minimizar el uso de memoria
def generar_numeros(n):
    for i in range(n):
        yield i

# Iteración sobre el generador sin almacenar todos los números en memoria
for num in generar_numeros(1000000):
    print(num)
