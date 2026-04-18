import numpy as np

# 1. Definir la función a minimizar (f(x) = x^2 - 4x + 5)
def f(x):
    return x**2 - 4*x + 5

# 2. Definir la derivada de la función (f'(x) = 2x - 4)
def gradient(x):
    return 2*x - 4

# 3. Algoritmo de descenso del gradiente
def gradient_descent(start_x, learning_rate, n_iterations, tolerance=1e-6):
    x = start_x
    history = []
    
    for i in range(n_iterations):
        grad = gradient(x)
        
        # Actualizar x: x_new = x_old - alpha * gradiente
        x_new = x - learning_rate * grad
        
        history.append(x_new)
        
        # Verificar convergencia (si el cambio es casi nulo)
        if abs(x_new - x) < tolerance:
            print(f"Convergencia alcanzada en la iteración {i}")
            break
            
        x = x_new
        
    return x, history

# --- Configuración ---
start_x = 10      # Punto inicial
lr = 0.1          # Tasa de aprendizaje (paso)
iterations = 50   # Máximo número de iteraciones

# --- Ejecución ---
minimum_x, path = gradient_descent(start_x, lr, iterations)

print(f"Mínimo encontrado en x = {minimum_x}")
print(f"Valor de f(x) en el mínimo = {f(minimum_x)}")
