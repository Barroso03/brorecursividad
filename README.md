 <h1 align="center">	Brorecursividad</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/Barroso03/brorecursividad.git)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea hemos resuelto una serie de ejercicios aplicando el método de la recursividad.

***

## Índice

1. [Dicotomia](#id1)
2. [Palindromos](#id2)
3. [Bandera de Dijkstra](#id3)
***

## Dicotomia:<a name="id1"></a>

```
def dicotonomia_recursiva (tabla, t):
    i = 0
    j = len(tabla)
    if i > j:
        return "Ausente"
    else:
        m = int((i+j)/2)
        if tabla[m] == t:
            return m
        else:
            if tabla[m] < int(t):
            #Esto implica que tabla[m+1] ≤ t ≤ tabla[j] 
            #Recursividad
                print (dicotonomia_recursiva(tabla, t))
                return dicotonomia_recursiva (tabla[m+1:j], t)
            else:
            #Esto implica que tabla[i] ≤ t ≤ tabla[m–1] 
            #Recursividad
                print (dicotonomia_recursiva(tabla, t))
                return dicotonomia_recursiva (tabla[i:m-1], t)

def dicotonomia (tabla, t):
  return dicotonomia_recursiva (tabla, t)

if __name__ == "__main__":
    #Entrada
    tabla = [4,2,6,3,8,7,5,9,1,0]
    t = input("Introduzca el dato a buscar: ")
    
    #Ordenamos tabla
    tabla.sort()

    print ("{} se encuentra en la celda {}".format(t, dicotonomia(tabla,t)))
```
***

## Palindromos:<a name="id2"></a>

```
#Funcion para pasar la frase a mayusculas y eliminar las tildes
def mayusculas_tildes(frase):
    #Hace la conversion si la frase es de tipo string
    if str(frase):
        frase = frase.upper()
        frase = frase.replace(" ", "")
        frase = frase.replace("Á", "A")
        frase = frase.replace("É", "E")
        frase = frase.replace("Í", "I")
        frase = frase.replace("Ó", "O")
        frase = frase.replace("Ú", "U")
    #Si no, no se puede hacer la conversion
    else:
        pass
    return frase

#Esta funcion devuelve un booleano que nos dice si es palindromo o no
def es_palindromo(frase):
    frase = mayusculas_tildes(frase)
    #Llegamos a que no nos quedan mas elementos, por lo tanto sera un palindromo
    if len(frase) == 0:
        return "Palindromo!"
    else:
        #Si el primer caracter coincide con el ultimo
        if frase[0] == frase[-1]:
            #Utilizamos recursividad
            return es_palindromo(frase[1:-1])
        else:
            #Si en algun momento no coincide el primero con el ultimo, no es palindromo :(
            return "No es palindromo :("

if __name__ == '__main__':

    oracion = input("Introduzca una frase molona o un numero: ")
    print (es_palindromo(oracion))
```
***

## Bandera de Dijkstra:<a name="id3"></a>

```
 def reorganizar_colores(self):
    if len(self.bandera) > 0:
      color = self.bandera.pop(0)

    if color == "R":
      self.rojo.append(color)
      return self.bandera
    if color == "A":
      self.azul.append(color)
      return self.bandera
    if color == "V":
      self.verde.append(color)
      return self.bandera
    else:
        resultado_bandera=rojo+verde+azul
        print('La bandera ordenada es la siguiente: {resultado_bandera}')

resultado=organizacion(bandera,rojo,verde,azul)
print(resultado.reorganizar_colores)
    
```
***

