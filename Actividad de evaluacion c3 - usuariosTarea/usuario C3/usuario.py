"""
usuario.py - Clase base del sistema de usuarios
Instituto Tecnológico Superior de Lerdo
Programación Orientada a Objetos - Corte 3
"""

import re  # Para validación de email

class Usuario:
    """Clase base que modela un usuario genérico del sistema."""

    def __init__(self, nombre, email):
        # Validar email antes de asignarlo
        if not self._validar_email(email):
            raise ValueError(f"Email inválido: {email}")
        self.nombre = nombre
        self.email = email

    def _validar_email(self, email):
        """Valida que el email tenga un formato correcto."""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return re.match(patron, email) is not None

    def mostrar_datos(self):
        """Muestra los datos básicos del usuario."""
        print(f"  Nombre : {self.nombre}")
        print(f"  Email  : {self.email}")

    def acceso_sistema(self):
        """Define el nivel de acceso (será sobrescrito por las clases derivadas)."""
        print(f"  [{self.nombre}] Acceso genérico al sistema.")

    def saludar(self):
        """Saluda al usuario con un mensaje personalizado."""
        print(f"  ¡Hola, {self.nombre}! Bienvenido al sistema.")
