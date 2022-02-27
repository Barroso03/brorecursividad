# brorecursividad
 <h1 align="center">	Recursividad</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio]()

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


```
***


## Palindromos:<a name="id2"></a>

```

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

