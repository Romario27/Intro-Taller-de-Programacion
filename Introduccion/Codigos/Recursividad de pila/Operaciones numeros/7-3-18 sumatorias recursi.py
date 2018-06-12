#fibonacci
def fib():
  num=int(input("Digite el valor:"))
  if isinstance (num,int) and num>0:
    return fib_aux(num)
  else:
    return "Error"


def fib_aux(n):
  if n==0:
    return 1
  elif n==1:
    return 1
  else:
    return fib_aux(n-1) + fib_aux(n-2)
    
    
#--------------------- sumatoria de i **2, con valores de i ==1 hasta i==n tarea para intro---------------------
def suma():
  num=int(input("Digite el valor:"))
  if isinstance (num,int) and num>0:
    return suma_aux(num)
  else:
    return "Error"
    
def suma_aux(num):
  if num==0:
    return 0
  else:
    return num + suma_aux(num-1)
    
#-----------------------------------------------tarea para taller---------------------------------------------
def suma1():
  num=int(input("Digite el valor:"))
  if isinstance (num,int) and num>0:
    return suma1_aux(num)
  else:
    return "Error"
    
def suma1_aux(num):
  if num==0:
    return 0
  else:
    return num*num**3 + suma1_aux(num-1)
    
#------------------------------------------------tarea taller---------------------------------------------------
def suma2():
  n=int(input("Digite el valor:"))
  if isinstance (n,int) and n>0:
    return suma2_aux(n)
  else:
    return "Error"
    
def suma2_aux(n):
  if n==0:
    return 0
  else:
    return n+5*((n*n)**2)  + suma2_aux(n-1)
#----------------------------------------------------#tarea taller---------------------------------------------
def multi():
  n=int(input("Digite el valor:"))
  if isinstance (n,int) and n>0:
    return multi_aux(n)
  else:
    return "Error"
    
def multi_aux(n):
  if n==0:
    return 1
  else:
    return ((3*n)-2) * multi_aux(n-1)
#-----------------------------------------------------tarea taller---------------------------------------------
def operacion():   #sumatoria de productos
  n=int(input("Digite el valor:"))
  if isinstance (n,int) and n>0:
    return suma_aux(n)
  else:
    return "Error"
    
def suma_aux(n):
  if n==0:
    return 0
  else:
    return multi_aux(n) + suma_aux(n-1) 
    
def multi_aux(x):
  if x==0:
    return 1
  else:
    return (3*(x)**2-x)*multi_aux(x-1)
