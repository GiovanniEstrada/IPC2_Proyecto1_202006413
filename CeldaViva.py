class CeldaViva():
    def __init__(self, fila, columna, codigoOrganismo):
        self.id = id
        self.filas = fila
        self.columnas = columna
        self.codigoOrganismo = codigoOrganismo
        self.siguiente = None

    def __str__(self):
        return "filas: " + self.filas + " columnas: " + self.columnas + " codigo organismo: " + self.codigoOrganismo
