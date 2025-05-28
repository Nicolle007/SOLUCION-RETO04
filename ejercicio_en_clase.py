import math

class Shape:
    def __init__(self, vertices, bordes, angulos_interiores):
        self._vertices = [] if vertices is None else vertices
        self._bordes = [] if bordes is None else bordes
        self._angulos_interiores = [] if angulos_interiores is None else angulos_interiores

    def get_vertices(self):
        return self._vertices

    def set_name(self, otros_vertices):
        if otros_vertices:
            self._vertices = otros_vertices

    def get_bordes(self):
        return self._bordes

    def set_bordes(self, otros_bordes):
        if otros_bordes:
            self._bordes = otros_bordes

    def get_angulos(self):
        return self._angulos_interiores

    def set_angulos(self, otros_angulos):
        if otros_angulos:
            self._angulos_interiores = otros_angulos

    def is_regular(self):
        c = 0
        regular = True
        while c < len(self._bordes) - 1:
            if (self._bordes[c].longitud == self._bordes[c + 1].longitud and
                self._angulos_interiores[c] == self._angulos_interiores[c + 1]):
                c += 1
            else:
                regular = False
                break
        return regular

    def compute_area(self):
        raise NotImplementedError("Las subclases deben implementar el método")

    def compute_perimeter(self):
        total = 0
        for i in self._bordes:
            total += i.longitud
        return total

    def compute_inner_angles(self):
        total = 0
        for i in self._angulos_interiores:
            total += i
        return total


class Triangulo(Shape):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        raise NotImplementedError("Las subclases deben implementar el método")


class Rectangulo(Shape):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        raise NotImplementedError("Las subclases deben implementar el método")


class Cuadrado(Rectangulo):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        lado = int(self._bordes[0].longitud)
        Area = lado * lado
        return Area


class Isosceles(Triangulo):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        todos_bordes = [i.longitud for i in self._bordes]

        repetido = []
        unico = []
        vistos = set()

        for x in todos_bordes:
            if todos_bordes.count(x) > 1 and x not in vistos:
                repetido.append(x)
                vistos.add(x)
            elif todos_bordes.count(x) == 1:
                unico.append(x)

        cateto = int(unico[0]) / 2
        hipotenusa = int(repetido[0])
        altura = math.sqrt((hipotenusa ** 2) - (cateto ** 2))
        Area = ((cateto * 2) * altura) / 2
        return Area


class Equilatero(Triangulo):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        cateto = int(self._bordes[0].longitud) / 2
        hipotenusa = int(self._bordes[0].longitud)
        altura = math.sqrt((hipotenusa ** 2) - (cateto ** 2))
        Area = ((cateto * 2) * altura) / 2
        return Area


class Escaleno(Triangulo):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        borde_1 = int(self._bordes[0].longitud)
        borde_2 = int(self._bordes[1].longitud)
        borde_3 = int(self._bordes[2].longitud)
        semi_p = (borde_1 + borde_2 + borde_3) / 2
        Area = math.sqrt(semi_p * (semi_p - borde_1) * (semi_p - borde_2) * (semi_p - borde_3))
        return Area


class Tri_Rectangulo(Triangulo):
    def __init__(self, vertices, bordes, angulos_interiores):
        super().__init__(vertices, bordes, angulos_interiores)

    def compute_area(self):
        todos_bordes = [i.longitud for i in self._bordes]
        hipotenusa = max(todos_bordes)
        catetos = [l for l in todos_bordes if l != hipotenusa]
        if len(catetos) != 2:
            raise ValueError("No se encontraron exactamente dos catetos.")
        cateto_1 = catetos[0]
        cateto_2 = catetos[1]
        return (cateto_1 * cateto_2) / 2


class punto:
    def __init__(self, coordenadas=None):
        self.coordenadas = [] if coordenadas is None else coordenadas
        if self.coordenadas:
            self.x = self.coordenadas[0]
            self.y = self.coordenadas[1]
        else:
            self.x = 0
            self.y = 0


class linea:
    def __init__(self, punto_inicial=None, punto_final=None, longitud=0.0):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
        self.longitud = longitud

p1 = punto([0, 0])
p2 = punto([4, 0])
p3 = punto([4, 3])
p4 = punto([0, 3])

p5 = punto([0, 0])
p6 = punto([3, 0])
p7 = punto([1.5, 2.598])  

p8 = punto([0, 0])
p9 = punto([5, 0])
p10 = punto([2, 4])


def calcular_longitud(p_inicio, p_final):
    return math.sqrt((p_final.x - p_inicio.x) ** 2 + (p_final.y - p_inicio.y) ** 2)

l1 = linea(p1, p2, calcular_longitud(p1, p2))
l2 = linea(p2, p3, calcular_longitud(p2, p3))
l3 = linea(p3, p4, calcular_longitud(p3, p4))
l4 = linea(p4, p1, calcular_longitud(p4, p1))

rect_bordes = [l1, l2, l3, l4]
rect_angulos = [90, 90, 90, 90]
rect_vertices = [p1, p2, p3, p4]

le = 3
pA = punto([0,0])
pB = punto([le,0])
pC = punto([le/2, le * math.sqrt(3)/2])

lA = linea(pA, pB, calcular_longitud(pA, pB))
lB = linea(pB, pC, calcular_longitud(pB, pC))
lC = linea(pC, pA, calcular_longitud(pC, pA))

equil_bordes = [lA, lB, lC]
equil_angulos = [60, 60, 60]
equil_vertices = [pA, pB, pC]

pI1 = punto([0,0])
pI2 = punto([6,0])
pI3 = punto([3,4]) 

lI1 = linea(pI1, pI2, calcular_longitud(pI1, pI2))
lI2 = linea(pI2, pI3, calcular_longitud(pI2, pI3))
lI3 = linea(pI3, pI1, calcular_longitud(pI3, pI1))

isos_bordes = [lI1, lI2, lI3]
isos_angulos = [calcular_longitud(pI3, pI1), calcular_longitud(pI2, pI3), calcular_longitud(pI1, pI2)] 
isos_vertices = [pI1, pI2, pI3]


pE1 = punto([0,0])
pE2 = punto([4,0])
pE3 = punto([4,3])

lE1 = linea(pE1, pE2, calcular_longitud(pE1, pE2))
lE2 = linea(pE2, pE3, calcular_longitud(pE2, pE3))
lE3 = linea(pE3, pE1, calcular_longitud(pE3, pE1))

esca_bordes = [lE1, lE2, lE3]
esca_angulos = [60, 90, 30]  
esca_vertices = [pE1, pE2, pE3]

triR_bordes = esca_bordes
triR_angulos = [90, 53.13, 36.87]
triR_vertices = esca_vertices

cuadrado = Cuadrado(vertices=rect_vertices, bordes=rect_bordes, angulos_interiores=rect_angulos)
print(cuadrado.compute_area())

equilatero = Equilatero(vertices=equil_vertices, bordes=equil_bordes, angulos_interiores=equil_angulos)
print(equilatero.compute_area())

isosceles = Isosceles(vertices=isos_vertices, bordes=isos_bordes, angulos_interiores=[70, 40, 70]) 
print( isosceles.compute_area())

escaleno = Escaleno(vertices=esca_vertices, bordes=esca_bordes, angulos_interiores=esca_angulos)
print( escaleno.compute_area())

tri_rectangulo = Tri_Rectangulo(vertices=triR_vertices, bordes=triR_bordes, angulos_interiores=triR_angulos)
print( tri_rectangulo.compute_area())


