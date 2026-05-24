
import time

def primo_mal_optimizado(numero_a_evaluar):
    if numero_a_evaluar == 0 or numero_a_evaluar == 1: return False
    lista_de_divisores = []
    for posible_divisor in range(1, numero_a_evaluar + 1):
        if numero_a_evaluar % posible_divisor == 0:
            lista_de_divisores.append(posible_divisor)
            
    cantidad_de_divisores = 0
    for elemento in lista_de_divisores: cantidad_de_divisores += 1
    return cantidad_de_divisores == 2

def buscar_primos(limite_superior):
    numeros_primos_encontrados = []
    for numero_actual in range(1, limite_superior + 1):
        if primo_mal_optimizado(numero_actual):
            numeros_primos_encontrados.append(numero_actual)
    return numeros_primos_encontrados


t_inicio = time.time()
primos_original = buscar_primos(limite_global)

tiempo_original = time.time() - t_inicio 

print(f"Total de números primos encontrados: {len(primos_original)}")
print(f"Tiempo de ejecución original: {tiempo_original:.6f} segundos.")