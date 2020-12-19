from graphics import *


# Classe per descrivere un valore all'interno del grafico
class Value:
    def __init__(self, x, y, value=None):
        self.point = Point(x, y)
        self.value = value

    def set_color(self, color):
        self.point.setOutline(color)
