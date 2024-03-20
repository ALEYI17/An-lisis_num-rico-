def aitken(g, tol, x1, x2):
    itr = 0
    x = (x1 + x2) / 2
    sequence = [x1, x2]
    while True:
        x = (x1 + x2) / 2
        b = g(x)
        sequence.append(b)
        if len(sequence) >= 3:
            y_n = x1 - ((sequence[-2] - x1)**2) / (b - 2*sequence[-2] + x1)
            if abs(y_n - x1) < tol:
                return y_n,itr
        x1 = x2
        x2 = b
        itr += 1
        if itr > 1000:  
            print("No se pudo alcanzar la convergencia en 1000 iteraciones.")
            return None

# Ejemplo de uso
g = lambda x: (10 - x**3)**0.5 / 2
tolerancia = 1e-6
x1 = 1
x2 = 2
resultado,itr = aitken(g, tolerancia, x1, x2)
print("Aproximación de la raíz:", resultado)
print("Iteraciones:", itr)

