tabla = [1,2,3,4,5,6,7,8]
n = int(input('Introduzca el valor que desea encontrar:'))
i = 0
j = len(tabla)
m = (i+j)/2

class tablas:
  def  __init__(self,tabla,n,i,j):
    self.i= i
    self.j= j
    self.n= n
    
  def busqueda_numero (self):
    
    if self.i > self.j:
      return'No hay ningún valor en la posición seleccionada'
      
    else:
      self.m = m
      if tabla[self.m] == n:
        return self.m
      elif tabla[self.m] > n:
        print (busqueda_numero(self))
        return busqueda_numero (self,self.m -1)
      else:
        return busqueda_numero (self, self.m + 1)
        
  
  resultado = tablas(tabla,n,j,i)
  print(resultado.busqueda_numero())