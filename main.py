# import xml.sax

# from entrada import CeldaViva


# class Manejador(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.fila = ""
#         self.columna = ""
#         self.codigoOrganismo = ""

#     def startElement(self, name, attrs):
#         self.CurrentData = name
#         if name == "celdaViva":
#             print("**** celdaViva *****")
#             print("ID: ")

#     def characters(self, content):
#         if self.CurrentData == "fila":
#             self.fila = content
#         elif self.CurrentData == "columna":
#             self.columna = content
#         elif self.CurrentData == "codigoOrganismo":
#             self.codigoOrganismo = content

#     def endElement(self, name):
#         if name == "celdaViva":
#             celda = CeldaViva(self.fila, self.columna, self.codigoOrganismo)


# if __name__ == '__main__':
#     print("XML")

#     parser = xml.sax.make_parser()
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)

#     # CLASE
#     Handler = Manejador()

#     parser.setContentHandler(Handler)

#     parser.parse("entrada.xml")

#     print("inicio lista")

#     print("TERMINO")

import xml.sax

from ListaSimple import ListaSimple

from ListaDoble import ListaDoble

from SubElemento import SubElemento

from entrada import Muestra
from Matriz import Matriz
from ListaOrganismos import ListaOrganismos
from CeldaViva import CeldaViva
from numeroCelda import NumeroCelda

listaOrganismos = ListaSimple()
listaCeldaViva = ListaSimple()
listaGrid = ListaSimple()
listaMuestras = ListaSimple()


class ManejadorCeldasVivas(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""  # DEFAULT

        self.listadoceldasVivas = None
        self.fila = ""
        self.columna = ""
        self.codigoOrganismo = ""
        self.celdaViva = None
        self.filasMuestra = ""
        self.columnasMuestra = ""
        self.descripcion = ""
        self.nombre = ""
        self.codigo = ""

    # Se llama cuando se encuentra un elemento de apertura
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        # if tag == "listadoCeldasVivas":
        #     self.celdaViva = ListaDoble()

    # Se llama cuando se encuentra contenido entre elementos
    def characters(self, content):

        if self.CurrentData == "fila":
            self.fila = content
        elif self.CurrentData == "columna":
            self.columna = content
        if self.CurrentData == "filas":
            self.filasMuestra = content
        elif self.CurrentData == "columnas":
            self.columnasMuestra = content
        elif self.CurrentData == "codigoOrganismo":
            self.codigoOrganismo = content
        elif self.CurrentData == "descripcion":
            self.descripcion = content
        elif self.CurrentData == "nombre":
            self.nombre = content
        elif self.CurrentData == "codigo":
            self.codigo = content
    # Se llama cuando se encuentra un elemento de cierre

    def endElement(self, tag):
        nMuestra = 0
        if tag == "organismo":
            organismo = ListaOrganismos(self.codigo, self.nombre)
            listaOrganismos.insertarFin(organismo)

        if tag == "celdaViva":
            sub = CeldaViva(self.fila, self.columna, self.codigoOrganismo)
            listaCeldaViva.insertarFin(sub)

        if tag == "muestra":
            nMuestra += 1
            grid = NumeroCelda(self.filasMuestra, self.columnasMuestra)
            listaGrid.insertarFin(grid)

        self.CurrentData = ""


if __name__ == '__main__':
    print("XML")

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # CLASE
    Handler = ManejadorCeldasVivas()

    parser.setContentHandler(Handler)

    parser.parse("entrada.xml")

    print(listaGrid.getFila())
    print("inicio lista")

    # listaOrganismos.recorrer()
    # listaCeldaViva.recorrer()
    # listaCeldaViva.recorrer()

    print(listaCeldaViva.buscar(1))

    print("fin de lista")

    temporal = listaOrganismos.buscar("1")
    print(temporal)

    matriz = Matriz()
    listaCeldaViva.grid(matriz, listaGrid.getFila(), listaGrid.getColumna())

    matriz.graficar()
