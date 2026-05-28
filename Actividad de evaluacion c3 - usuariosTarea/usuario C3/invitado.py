"""
invitado.py - Clase derivada Invitado
Instituto Tecnológico Superior de Lerdo
Programación Orientada a Objetos - Corte 3
"""

from usuario import Usuario

class Invitado(Usuario):
    """Clase derivada que modela un invitado (acceso mínimo).
    Hereda de Usuario sin agregar atributos propios.
    """

    def __init__(self, nombre, email):
        # Llama al constructor del padre
        super().__init__(nombre, email)

    def acceso_sistema(self):
        """Sobrescribe acceso_sistema para acceso muy restringido."""
        print(f"  [{self.nombre}] ⚠ Acceso INVITADO - Solo lectura.")
        print(f"  Solo puede ver contenido público. Regístrate para más funciones.")

    def saludar(self):
        """Saludo personalizado para invitado con acceso limitado."""
        print(f"  Hola, {self.nombre}. Tienes acceso de invitado (solo lectura).")
