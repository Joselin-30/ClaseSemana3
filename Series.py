# Serie sumatoria de n
def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l

#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    
#Tarea Joselin Medina:
def factorial(n):
  """
  Esta función calcula el factorial de un número.

  Args:
    n: El número del cual se calculará el factorial.

  Returns:
    El factorial de n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)