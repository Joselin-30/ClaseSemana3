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