import numpy as np
import matplotlib.pyplot as plt

# 1. Definir la función a minimizar f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# 2. Definir el gradiente de la función (derivadas parciales)
# df/dx = 2x, df/dy = 2y
def gradient_f(x, y):
    return np.array([2*x, 2*y])

# 3. Parámetros del descenso de gradiente
learning_rate = 0.1
iterations = 50
# Punto inicial aleatorio
point = np.array([4.0, 3.0]) 

# Para guardar la historia y visualizar
history = [point]

# 4. Algoritmo de Descenso de Gradiente
for i in range(iterations):
    grad = gradient_f(point[0], point[1])
    # Actualización: nuevo_punto = punto_actual - learning_rate * gradiente
    point = point - learning_rate * grad
    history.append(point)
    
    if i % 5 == 0:
        print(f"Iteración {i+1}: x = {point[0]:.4f}, y = {point[1]:.4f}, f(x,y) = {f(point[0], point[1]):.4f}")

print(f"\nMínimo encontrado en: x = {point[0]:.4f}, y = {point[1]:.4f}")

# 5. Visualización
history = np.array(history)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, 20)
plt.plot(history[:, 0], history[:, 1], 'r.-', label='Trayectoria')
plt.plot(point[0], point[1], 'go', label='Mínimo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Descenso de Gradiente 2D')
plt.legend()
plt.colorbar(label='f(x,y)')
plt.show()
