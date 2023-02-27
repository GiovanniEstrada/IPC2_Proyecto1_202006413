class NodoInterno:
    def __init__(self, fila=None, col=None, val=None) -> None:
        self.fila = fila
        self.col = col
        self.valor = val
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
