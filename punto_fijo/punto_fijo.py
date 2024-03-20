def punto_fijo(g,tol,x1,x2):
  itr = 0
  x = (x1+x2)/2
  b = g(x)
  tramo = abs(b-x)
  while tramo > tol:
    x = b
    b = g(x)
    tramo = abs(b-x)
    itr = itr+1
  return b,itr

gx = lambda x: (10 - x**3)**0.5 / 2
tolerancia = 1e-6
x1 =1
x2=2
resultado,itr = punto_fijo(gx,tolerancia,x1,x2)
print(resultado)
print(itr)