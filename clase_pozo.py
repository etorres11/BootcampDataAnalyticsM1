class Pozo:

    def __init__(
        self,
        nombre,
        campo,
        petroleo,
        agua,
        gas
    ):
        self.nombre = nombre
        self.campo = campo
        self.petroleo = petroleo
        self.agua = agua
        self.gas = gas

    def mostrar_informacion(self):
        return {
            "nombre": self.nombre,
            "campo": self.campo,
            "petroleo": self.petroleo,
            "agua": self.agua,
            "gas": self.gas
        }

    def produccion_liquida(self):
        return calcular_liquido(
            self.petroleo,
            self.agua
        )

    def bsw(self):
        return calcular_bsw(
            self.petroleo,
            self.agua
        )

    def gor(self):
        return calcular_gor(
            self.gas,
            self.petroleo
        )