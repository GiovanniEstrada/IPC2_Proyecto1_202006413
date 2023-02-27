from CeldaViva import CeldaViva


class Muestra():
    def __init__(self, filas, columnas, descripcion, codigo, celdasVivas: CeldaViva):
        self.filas = filas
        self.columnas = columnas
        self.celdasVivas = celdasVivas
        self.siguiente = None

    # def __str__(self):
    #     return "id: " + self.id + " nombre: " + self.nombre + " subelementos: \n" + str(self.subElementos.recorrer())
