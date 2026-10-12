from exceptions.tipoParametroIncorretoException import TipoParametroIncorretoException


class TipoDeAtendimento:
    def __init__(self, tipo: str):
        self.tipo = tipo

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise TipoParametroIncorretoException("string")
