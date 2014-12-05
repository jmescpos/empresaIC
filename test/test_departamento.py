from unittest import TestCase
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mockito import *
from src.Departamento import *
from src.Empleado import *


__author__ = 'Juanma'


class TestDepartamento(TestCase):
    """Clase de testeo para la clase departamento"""

    def test_get_salario_total_mensual(self):
        """Metodo que comprueba si el salario total de los empleados funciona correctamente.

        :return self.assertEquals: Comprueba resultado del salario.
        """

        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)

        when(e1).get_salario_mensual().thenReturn(1000)
        when(e2).get_salario_mensual().thenReturn(1000)
        when(e3).get_salario_mensual().thenReturn(1000)

        d = Departamento("Informatica", 1)

        d.aniadir_empleado(e1)
        d.aniadir_empleado(e2)
        d.aniadir_empleado(e3)

        total_salario_mensual = d.get_salario_total_mensual()

        self.assertEquals(total_salario_mensual, 36000)