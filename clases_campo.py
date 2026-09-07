"""Clase Campo: ejemplo de composición de objetos."""

from clases_pozo import Pozo


class Campo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.pozos = []

    def agregar_pozo(self, pozo):
        if isinstance(pozo, Pozo):
            self.pozos.append(pozo)

    def cantidad_pozos(self):
        return len(self.pozos)

    def produccion_petroleo_total(self):
        total = 0

        for pozo in self.pozos:
            total += pozo.petroleo

        return total

    def listar_pozos(self):
        return [
            pozo.mostrar_informacion()
            for pozo in self.pozos
        ]
