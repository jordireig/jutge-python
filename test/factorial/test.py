from jutge import read

def factorial (n):
  if n == 0: return 1
  return n * factorial(n-1)
  
x = read(int)
print(factorial(x))