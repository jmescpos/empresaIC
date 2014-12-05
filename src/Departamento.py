__author__ = 'Juanma'

class Departamento():
    """Esta clase representa a un departamento"""

    def __init__(self, nombre_depto, d_depto):
        """Constructor clase departamento.

        Se encarga de inicializar los atributos
        correspondientes de la clase departamento.
        :param nombre_depto: Nombre del departamento.
        :param d_depto: Departamento.
        :type nombre_depto: String.
        :type d_depto: String.
        """
        self.nombre_depto = nombre_depto
        self.d_depto = d_depto
        self.listaEmpleados = []

    def aniadir_empleado(self,empleado):
        """Metodo para introducir empleados al departamento

        Se encarga de introducir un objeto de tipo
        empleado al departamento que invoca el metodo.

        :param empleado: Objeto de tipo empleado.
        :type empleado: Empleado.
        """
        self.listaEmpleados.append(empleado)

    def get_salario_total(self):
        """Metodo que calcula el salario total de los empleados

        Este metodo se encarga de calcular el salario total de
        todos los empleados para ello recorrera
        todos los empleados y sumara su atributo salario,
         devolvera una variable con la suma
        total del salario de los empleados.

        :return cantidad: Devuelve la suma de los salarios.
        :rtype cantidad: Float.
        """
        cantidad = 0.0
        for empleado in self.listaEmpleados:
            cantidad = cantidad + empleado.get_salario()
        print 'Salario total de empleados:', cantidad
        return cantidad

    def get_nombre_depto(self):
        """Metodo get del atributo nombre_depto

        Este metodo devolvera el atributo nombre_depto de la
        instancia departamento queinvoca el metodo.

        :return: Devuelve le nombre del departamento.
        :rtype: String.
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """Metodo que devuelve el salario mensual de un empleado

        Este metod sera el encargado de sumar los salario
         mensuales de la lista de empleados.
        Para ello multiplicar el salario por 12 meses.

        :return c: Devuelve la cantidad de salario mensual del empleado.
        :rtype c: Float.
        """
        c = 0.0
        for empleado in self.listaEmpleados:
            c += empleado.get_salario_mensual() * 12
        return c