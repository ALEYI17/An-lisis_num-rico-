import numpy as np

### Funcion para determinar si la matriz es diagonalmente dominante
def is_diagonally_dominant(A):
    n = len(A)
    #print(n)

    for i in range(0, n):
        row_sum = 0
        for j in range(0, n):
            row_sum += abs(A[i][j])

        row_sum -= abs(A[i][i])

        if abs(A[i][i]) < row_sum:
            return False
    return True
## Funcion para determinar si la matriz es definida positiva
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

## Funcion para enconrar la matriz TJ
def calculate_TJ(matrix_A):
    n = len(matrix_A)
    TJ = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                TJ[i][j] = -matrix_A[i][j] / matrix_A[i][i]

    return TJ

## Funcion para encontar el radio espectral
def calculate_spectral_radius(matrix_TJ):
    eigenvalues, _ = np.linalg.eig(matrix_TJ)
    spectral_radius = np.max(np.abs(eigenvalues))
    return spectral_radius

## Matriz para conseguir omega
def calculate_omega(spectral_radius):
    omega = 2.0 / (1.0 + np.sqrt(1.0 - spectral_radius**2))
    return omega

## Funcion algoritmo SOR
def gauss_seidel_sor(A, b, omega, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)
    normVal = float('inf')
    itr = 0

    while normVal > tol:
      x_old = np.copy(x)

      for i in range(n):
          sigma = 0

          for j in range(i):
              sigma += A[i, j] * x[j]


          for j in range(i + 1, n):
              sigma += A[i, j] * x_old[j]
          print(f"sigma={sigma}")
          x[i] = ((1 - omega) * x_old[i]) + ((omega / A[i, i]) * (b[i] - sigma))

      print(f"x={x}")
      itr += 1
      normVal = np.linalg.norm(x-x_old)
      print(f"nomrval = {normVal}")
      if itr == max_iter:
          print("No converge en el número máximo de iteraciones.")

    return x, itr


## Matriz de prueba
A = np.array([[10, -1,0],
              [-1, 10, -2],
              [0, -2, 10]])

## Vector de resultados
b = np.array([9, 7, 6])

# Tolerance for method
tol = 1e-6
itr = 0

## resultados de diagonal y positiva
print("Es diagonal mente dominante:", is_diagonally_dominant(A))
print("Es definida positiva: ", is_pos_def(A))

# Encontara TJ
TJ = calculate_TJ(A)
print("Matriz TJ:")
print(TJ)

## calcular el radio espectral
spectral_radius = calculate_spectral_radius(TJ)
print("Radio espectral:", spectral_radius)

## Calcular omega
omega = calculate_omega(spectral_radius)
print("Parámetro de relajación omega:", omega)

solution, iterations = gauss_seidel_sor(A, b, omega)

print("Solution of the system is:")
print(solution)
print(f"Converged in {iterations} iterations")