"""
admin.py - Clase derivada Admin
Instituto Tecnológico Superior de Lerdo
Programación Orientada a Objetos - Corte 3
"""

from usuario import Usuario

class Admin(Usuario):
    """Clase derivada que modela un administrador del sistema.
    Hereda de Usuario y agrega nivel_acceso.
    """

    def __init__(self, nombre, email, nivel_acceso):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, email)
        # Validar que nivel_acceso sea entero entre 1 y 5
        if not isinstance(nivel_acceso, int) or not (1 <= nivel_acceso <= 5):
            raise ValueError("El nivel de acceso debe ser un entero entre 1 y 5.")
        self.nivel_acceso = nivel_acceso  # Atributo propio de Admin

    def mostrar_datos(self):
        """Muestra datos del administrador, incluyendo nivel de acceso."""
        super().mostrar_datos()  # Reutiliza el método del padre
        print(f"  Nivel de acceso: {self.nivel_acceso}")

    def acceso_sistema(self):
        """Sobrescribe acceso_sistema para dar acceso total al administrador."""
        print(f"  [{self.nombre}] ✔ Acceso ADMINISTRADOR - Nivel {self.nivel_acceso}.")
        print(f"  Puede gestionar usuarios, configurar el sistema y ver reportes.")
