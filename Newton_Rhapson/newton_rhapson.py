import numpy as np
import sympy as sp

def Newton_Rhapson(f,tol,x0):
  # Definir las iteraciones
  itr=0

  # Definir variable
  x = sp.symbols('x')

  # Calcular la derivada
  f_prime = sp.diff(f(x), x)

  # Convertir a funcion the python
  f_prime_func = sp.lambdify(x, f_prime)

  xi= x0
  
  tramo = tol *2

  while tramo > tol:
    xnuevo = xi - (f(xi)/f_prime_func(xi))
    print(xnuevo)
    itr = itr +1
    tramo = abs(xnuevo-xi)
    xi = xnuevo
  return xi,itr


# Definir funcion
fx  = lambda x: x**3 + 4*(x**2) - 10

## Definir tol
tol = 1e-6

## Definir x0
x0= 1.2

raiz , itr_final = Newton_Rhapson(fx,tol,x0)

print(f"La raiz del polinomio es : {raiz}")
print(f"Se demoro {itr_final} iteraciones")