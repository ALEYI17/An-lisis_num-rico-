
def metodo_secante(f,tol,x1,x2):
  # Definir las iteraciones
  itr=0
  
  tramo = tol *2

  while tramo > tol:
    xnuevo = x2 - ( f(x2)*(x2-x1) )   / (f(x2) - f(x1) )
    x1 = x2
    x2 = xnuevo
    print(xnuevo)
    itr = itr +1
    tramo = abs(x2-x1)
  return xnuevo,itr


# Definir funcion
fx  = lambda x: x**3 + 4*(x**2) - 10

## Definir tol
tol = 1e-6

## Definir el intervalo
x1= 1
x2=2

raiz , itr_final = metodo_secante(fx,tol,x1,x2)

print(f"La raiz del polinomio es : {raiz}")
print(f"Se demoro {itr_final} iteraciones")