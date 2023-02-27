from NodoEncabezado import NodoEncabezado


class ListaEncabezado:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def insert(self, nuevo: NodoEncabezado):
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = self.ultimo
                self.utlimo = nuevo
            else:
                actual = self.primero
                while actual != None:
                    if nuevo.id < actual.id:
                        nuevo.siguiente = actual
                        nuevo.anterior = actual.anterior
                        actual.anterior.siguiente = nuevo
                        actual.anterior = nuevo
                        break
                    actual = actual.siguiente

    def search(self, id):

        actual = self.primero
        while actual != None:
            print(f"actual id: {actual.id}")
            print(f"id: { id}")
            print(f"actual Sig: {actual.siguiente}")
            if actual.id == id:
                actual.siguiente = None
                print("listo")
                return actual
            # if actual.siguiente == actual:
            #     return None
            actual = actual.siguiente
        return None

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print(actual.id)
            actual = actual.siguiente
