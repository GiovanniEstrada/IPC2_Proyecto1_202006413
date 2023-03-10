class CeldaViva():
    def __init__(self, fila, columna, codigoOrganismo):
        self.id = 0
        self.filas = fila
        self.columnas = columna
        self.codigoOrganismo = codigoOrganismo
        self.siguiente = None

    def __str__(self):
        return "filas: " + self.filas + " columnas: " + self.columnas + " codigo organismo: " + self.codigoOrganismo + str(self.id)

    def getFila(self):
        return self.filas

    def getColumna(self):
        return self.columnas

    def getOrganismo(self):
        return self.codigoOrganismo
