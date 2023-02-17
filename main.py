import xml.sax

from entrada import CeldaViva


class Manejador(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.fila = ""
        self.columna = ""
        self.codigoOrganismo = ""

    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == "celdaViva":
            print("**** celdaViva *****")

    def characters(self, content):
        if self.CurrentData == "fila":
            self.fila = content
        elif self.CurrentData == "columna":
            self.columna = content
        elif self.CurrentData == "codigoOrganismo":
            self.codigoOrganismo = content

    def endElement(self, name):
        if name == "celdaViva":
            celda = CeldaViva(self.fila, self.columna, self.codigoOrganismo)


if __name__ == '__main__':
    print("XML")

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # CLASE
    Handler = Manejador()

    parser.setContentHandler(Handler)

    # parser.parse("entrada.xml")

    print("TERMINO")
