__author__ = 'Juanma'


class Empresa():
    """Clase empleado de una empresa"""
    def __init__(self, nombre_empresa, cif, razon_social):
        """Metodo constructor de la clase empresa

        :param nombre_empresa: Es el nombre que tendra la empresa.
        :param cif: Es el identificador fiscal de la empresa(CIF).
        :param razon_social: Es un nombre empresa.
        :type nombre_empresa: String.
        :type cif: String.
        :type razon_social: String.
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.listaDepartamentos = []
