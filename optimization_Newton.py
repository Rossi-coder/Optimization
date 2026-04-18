
def Newton_optimizacion(f_prime, f_double_prime, x0, tol=1e-6, max_iter=100):
    """
    Encuentra el mínimo de una función usando el método de Newton.
    """
    x = x0
    for i in range(max_iter):
        df = f_prime(x)
        ddf = f_double_prime(x)
        
        # Fórmula de Newton para optimización
        if ddf == 0:
            print("La segunda derivada es cero. No se puede continuar.")
            break
            
        x_new = x - df / ddf
        
        # Verificar convergencia
        if abs(x_new - x) < tol:
            print(f"Convergencia alcanzada en {i+1} iteraciones.")
            return x_new
        
        x = x_new
        print(f"Iteración {i+1}: x = {x:.6f}")
        
    return x

# --- Ejemplo de uso ---
# Función: f(x) = x^2 + 16/x
# Primera derivada: f'(x) = 2x - 16/x^2
# Segunda derivada: f''(x) = 2 + 32/x^3

f_p = lambda x: 2*x - 16/(x**2)
f_pp = lambda x: 2 + 32/(x**3)

# Punto inicial
x_inicial = 1.0

# Ejecutar el método
minimo = Newton_optimizacion(f_p, f_pp, x_inicial)
print(f"El mínimo aproximado es: {minimo:.6f}")
