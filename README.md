# SOLUCION-RETO04
_En el codigo llamado "ejercicio en clase" podemos encontrar este mismo_
Para este codigo todo fue mucho mas facil pues tenia bastantes cosas adelantadas, decidi aplicar setters y getters en las subclases con atributos privados y en clase padre con atributos protegidos, realice uno para cada una de las subclases, tambien añadí el metodo de pago muy parecido al que vimos en clase, aceptando tarjeta o efectivo, y para el tema de los descuentos decidi utilizar una especie de comandos que permitieran realizarlos.
_El codigo es el archivo llamado reto04_
 class MenuItem:
    def __init__(self, nombre, precio=int):
          self._nombre=nombre
          self._precio=precio
          
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, otro_nombre):
        if otro_nombre:
            self._nombre = otro_nombre

class Sopa(MenuItem):
    def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.__tipo = tipo  # Atributo privado
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio
    
    def get_tipo(self): # Getter para el atributo tipo
        return self.__tipo

class Bebida(MenuItem):
    def __init__(self, nombre, precio,temperatura):
        super().__init__(nombre,precio)
        self.__temperatura = temperatura # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_temperatura(self): # Getter para el atributo temperatura
        return self.__temperatura

class Postre(MenuItem):
    def __init__(self, nombre, precio,helado):
        super().__init__(nombre,precio)
        self.__helado = helado # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_helado(self): # Getter para el atributo helado
        return self.__helado

class Fruta(MenuItem):
    def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.__tipo = tipo # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_tipo(self): # Getter para el atributo tipo
        return self.__tipo

class Ensalada(MenuItem):
    def __init__(self, nombre, precio,gusto):
        super().__init__(nombre,precio)
        self.__gusto = gusto # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_gusto(self): # Getter para el atributo gusto
        return self.__gusto

class Proteina(MenuItem):
    def __init__(self, nombre, precio,gramaje):
        super().__init__(nombre,precio)
        self.__gramaje = gramaje # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_gramaje(self): # Getter para el atributo gramaje
        return self.__gramaje

class Entradas(MenuItem):
    def __init__(self, nombre, precio,lugar):
        super().__init__(nombre,precio)
        self.__lugar = lugar # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_lugar(self): # Getter para el atributo lugar
        return self.__lugar

class Adicion(MenuItem):
    def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.__tipo = tipo # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_tipo(self): # Getter para el atributo tipo
        return self.__tipo

class Infantil(MenuItem):
    def __init__(self, nombre, precio,contenido):
        super().__init__(nombre,precio)
        self.__contenido = contenido # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio
    
    def get_contenido(self): # Getter para el atributo contenido
        return self.__contenido

class Quesos(MenuItem):
    def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.__tipo = tipo # Atributo privado
        
    def get_precio(self):
        return self._precio
    def set_precio(self, otro_precio):
        if otro_precio:
            self._precio = otro_precio

    def get_tipo(self): # Getter para el atributo tipo
        return self.__tipo


class Orden:
    global descuento
    descuento=0
    def __init__(self,contenido=list):
      self.contenido=contenido

    def agregar_articulos(self, Item):
        self.contenido.append(Item)

    def total(self):
        suma=0
        for i in self.contenido:
            suma = i._precio + suma
        if descuento!=0:
            suma=suma*descuento
        print(suma)
            

    def descuentos(self,tipo):
        self.tipo = tipo
        match tipo:
            case "Proteina+Ensalada":
                        descuento=0.85
            case "Proteina+Fruta":
                descuento=0.80
            case "Postre+Postre":
                descuento=0.90
            case "Bebida+Adicion":
                descuento=0.90
            case "Infantil+Postre":
                descuento=0.75

    def Items(self):
        for i in self.contenido:
            print(i._nombre)
            
class Pago:
  def __init__(self):
      pass

  def pagar(self, total):
    raise NotImplementedError("Subclases deben implementar el metodo")

class Tarjeta(Pago):
    def __init__(self,tipo):
        super().__init__()
        self.tipo = tipo

    def pagar(self, total):
        print(f"Pagando {total} con tarjeta {self.tipo} ")

class Efectivo(Pago):
  def __init__(self, dinero_entregado):
    super().__init__()
    self.dinero_entregado = dinero_entregado

  def pagar(self, total):
    if total <= self.dinero_entregado:
        cambio=total-self.dinero_entregado
        print(f"Pago realizado en efectivo. Cambio: {cambio}")
    else:
        faltante=total-self.dinero_entregado
        print(f"Faltan {faltante} para el pago.")

#Ejemplo de uso de las clases
pago1 = Tarjeta("debito")
pago2 = Efectivo(100)

pago1.pagar(50)
pago2.pagar(75)

#Sopas
sopa1 = Sopa("Sopa de pollo", 5000, "clara")
sopa2 = Sopa("Sopa de lentejas", 5200, "espesa")
sopa3 = Sopa("Sopa de verduras", 4800, "ligera")

#Bebidas
bebida1 = Bebida("Limonada", 3000, "fría")
bebida2 = Bebida("Chocolate caliente", 3500, "caliente")
bebida3 = Bebida("Jugo de mango", 3200, "fría")

#Postres
postre1 = Postre("Flan", 4000, False)
postre2 = Postre("Helado de vainilla", 4500, True)
postre3 = Postre("Torta de chocolate", 5000, False)

#Frutas
fruta1 = Fruta("Manzana", 2500, "roja")
fruta2 = Fruta("Banano", 2200, "maduro")
fruta3 = Fruta("Uvas", 2700, "verdes")

#Ensaladas
ensalada1 = Ensalada("Ensalada César", 6000, "ligera")
ensalada2 = Ensalada("Ensalada griega", 5800, "fresca")
ensalada3 = Ensalada("Ensalada tropical", 6200, "dulce")

#Proteínas
proteina1 = Proteina("Pollo asado", 10000, "200g")
proteina2 = Proteina("Pescado al horno", 12000, "180g")
proteina3 = Proteina("Carne a la parrilla", 13000, "250g")

#Entradas
entrada1 = Entradas("Pan de ajo", 2500, "mesa")
entrada2 = Entradas("Mini empanadas", 3000, "cocina")
entrada3 = Entradas("Bastones de queso", 3200, "barra")

#Adiciones
adicion1 = Adicion("Papas a la francesa", 4000, "fritas")
adicion2 = Adicion("Arepa", 1500, "asada")
adicion3 = Adicion("Tajadas", 2000, "dulces")

#Infantil
infantil1 = Infantil("Combo dinosaurio", 8500, "hamburguesa, jugo, sorpresa")
infantil2 = Infantil("Caja mágica", 9000, "nuggets, papas, postre")
infantil3 = Infantil("Mini pizza kit", 8000, "pizza personal, jugo")

#Quesos
queso1 = Quesos("Queso mozzarella", 3500, "blando")
queso2 = Quesos("Queso azul", 3800, "fuerte")
queso3 = Quesos("Queso parmesano", 3600, "curado")

orden = Orden([])

orden.agregar_articulos(sopa1)
orden.agregar_articulos(bebida2)
orden.agregar_articulos(postre3)
orden.agregar_articulos(fruta1)
orden.agregar_articulos(ensalada2)
orden.agregar_articulos(proteina3)
orden.agregar_articulos(entrada1)
orden.agregar_articulos(adicion2)
orden.agregar_articulos(infantil3)
orden.agregar_articulos(queso1)
orden.total()
orden.Items()
orden.descuentos("Postre+Postre")
orden.total()

print(queso1.get_tipo())
print(proteina3.get_gramaje())
print(infantil2.get_contenido())
