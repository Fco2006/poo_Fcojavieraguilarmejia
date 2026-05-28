"""
cliente.py - Clase derivada Cliente
Instituto Tecnológico Superior de Lerdo
Programación Orientada a Objetos - Corte 3
"""

from usuario import Usuario

class Cliente(Usuario):
    """Clase derivada que modela un cliente del sistema.
    Hereda de Usuario y agrega puntos de fidelidad.
    """

    def __init__(self, nombre, email, puntos=0):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, email)
        # Validar que los puntos no sean negativos
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos.")
        self.puntos = puntos  # Atributo propio de Cliente

    def mostrar_datos(self):
        """Muestra datos del cliente, incluyendo sus puntos."""
        super().mostrar_datos()
        print(f"  Puntos acumulados: {self.puntos}")

    def acceso_sistema(self):
        """Sobrescribe acceso_sistema para acceso de cliente (limitado)."""
        print(f"  [{self.nombre}] ✔ Acceso CLIENTE - {self.puntos} puntos disponibles.")
        print(f"  Puede ver productos, realizar compras y consultar su historial.")
