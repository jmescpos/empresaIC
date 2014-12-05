__author__ = 'Juanma'


class Empleado():
    """Clase empleado de una empresa"""

    def __init__(self, nombre, apellidos, dni, direccion,
                 edad, email, salario):
        """Constructor clase empleado

        :param nombre: Nombre del empleado.
        :param apellidos: Apellidos del empleado.
        :param dni: DNI.
        :param direccion: Direccion del empleado.
        :param edad: Edad del empleado.
        :param email: Correo electronico del empleado.
        :param salario: Sueldo del empleado.
        """
        self.nombre = nombre
        self.apellido = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """Metodo get del atributo salario.

        :return salario: Devuelve salario.
        :rtype salario: Float
        """

        return self.salario

    def get_dni(self):
        """Metodo get del atributo dni.

        :return dni: Devuelve el dni.
        :rtype dni: String."""
        return self.dni

    def get_nombre_apellidos(self):
        """Metodo get que devuelve el atributo nombre y apellido.

        :return nombre_apellido: Devuelve nombre y el apellido.
        :rtype nombre_apellidos: String."""
        return self.nombre + ' ' + self.apellido

    def get_edad(self):
        """Metodo get del atributo edad.

        :return edad: Devuelve la edad.
        :rtype edad: Int."""
        return self.edad

    def get_email(self):
        """Metodo get del atributo email.

        :return edad: Devuelve el email.
        :rtype edad: String."""
        return self.email

    def get_direccion(self):
        """Metodo get del atributo direccion.

        :return edad: Devuelve la direccion.
        :rtype edad: String."""
        return self.direccion

    def get_salario_mensual(self):
        """Metodo que devuelve el salario anual.

        :return self.salario: Devuelve el salario anual.
        :rtype self.salario: Float."""
        return self.salario * 12
