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