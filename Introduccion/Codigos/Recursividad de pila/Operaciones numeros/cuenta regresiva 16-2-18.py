def cuenta_regresiva(valor):
      #print(valor)
      if valor>0:   # seguir - verde
            print(valor)
            cuenta_regresiva (valor-1)
      else:
            if (valor<=0): # parar - rojo
                  return 0
