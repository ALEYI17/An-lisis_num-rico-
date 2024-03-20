def aitken(sequence):
    accelerated_sequence = []
    for i in range(len(sequence) - 2):
        x_n = sequence[i]
        x_n1 = sequence[i + 1]
        x_n2 = sequence[i + 2]
        y_n = x_n - ((x_n1 - x_n)**2) / (x_n2 - 2*x_n1 + x_n)
        accelerated_sequence.append(y_n)
    return accelerated_sequence
def punto_fijo_acelerado(g, tol, x0, max_iter):
    sequence = [x0]
    for _ in range(max_iter):
        x_next = g(sequence[-1])
        sequence.append(x_next)
        if len(sequence) >= 3:
            accelerated_sequence = aitken(sequence)
            if abs(accelerated_sequence[-1] - sequence[-1]) < tol:
                return accelerated_sequence[-1]
    print("El método de punto fijo acelerado no convergió después de {} iteraciones.".format(max_iter))
    return None


g = lambda x: (10 - x**3)**0.5 / 2
tolerancia = 1e-6
x0 = 1
max_iter = 1000
resultado = punto_fijo_acelerado(g, tolerancia, x0, max_iter)
if resultado is not None:
    print("Aproximación de la raíz:", resultado)