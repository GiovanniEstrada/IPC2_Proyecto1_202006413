class NumeroCelda():
    def __init__(self, fila, columna, ):
        self.filas = fila
        self.columnas = columna

    def __str__(self):
        return "filas: " + self.filas + " columnas: " + self.columnas + " codigo organismo: " + self.codigoOrganismo + str(self.id)

    def getFila(self):
        return self.filas

    def getColumna(self):
        return self.columnas
