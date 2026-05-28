"""
main.py - Aplicación principal del Sistema de Usuarios
Instituto Tecnológico Superior de Lerdo
Programación Orientada a Objetos - Corte 3

Demuestra herencia, polimorfismo, menú interactivo y lista de usuarios.
"""

from admin import Admin
from cliente import Cliente
from invitado import Invitado
from usuario import Usuario

# ─────────────────────────────────────────────
#  Lista global de usuarios (desafío: lista)
# ─────────────────────────────────────────────
lista_usuarios = []

def crear_usuarios_demo():
    """Crea al menos 1 admin, 1 cliente y 1 invitado como datos de ejemplo."""
    lista_usuarios.append(Admin("Carlos Mendoza", "carlos@itsl.edu.mx", nivel_acceso=5))
    lista_usuarios.append(Admin("Laura Ríos",    "laura@itsl.edu.mx",  nivel_acceso=3))
    lista_usuarios.append(Cliente("Ana Torres",   "ana@gmail.com",  puntos=1200))
    lista_usuarios.append(Cliente("Luis Herrera",  "luis@gmail.com", puntos=350))
    lista_usuarios.append(Invitado("Visitante1",  "visita1@temp.com"))
    lista_usuarios.append(Invitado("Visitante2",  "visita2@temp.com"))

def mostrar_todos():
    """Muestra datos y acceso de todos los usuarios (polimorfismo)."""
    print("\n" + "="*55)
    print("  LISTA COMPLETA DE USUARIOS")
    print("="*55)
    for i, usuario in enumerate(lista_usuarios, 1):
        tipo = type(usuario).__name__  # Nombre de la clase real
        print(f"\n[{i}] {tipo}")
        usuario.mostrar_datos()
        usuario.acceso_sistema()
        print("-"*55)

def saludar_todos():
    """Llama al método saludar() de cada usuario (polimorfismo)."""
    print("\n" + "="*55)
    print("  SALUDOS DEL SISTEMA")
    print("="*55)
    for usuario in lista_usuarios:
        usuario.saludar()

def agregar_usuario():
    """Permite agregar un nuevo usuario mediante entrada del teclado."""
    print("\n--- AGREGAR USUARIO ---")
    print("Tipo: 1) Admin  2) Cliente  3) Invitado")
    opcion = input("Selecciona tipo: ").strip()

    nombre = input("Nombre: ").strip()
    email  = input("Email: ").strip()

    try:
        if opcion == "1":
            nivel = int(input("Nivel de acceso (1-5): ").strip())
            lista_usuarios.append(Admin(nombre, email, nivel))
        elif opcion == "2":
            puntos = int(input("Puntos iniciales: ").strip())
            lista_usuarios.append(Cliente(nombre, email, puntos))
        elif opcion == "3":
            lista_usuarios.append(Invitado(nombre, email))
        else:
            print("  Opción inválida.")
            return
        print(f"  Usuario '{nombre}' agregado correctamente.")
    except ValueError as e:
        print(f"  Error: {e}")

def menu():
    """Menú interactivo principal."""
    print("\n" + "★"*55)
    print("   SISTEMA DE USUARIOS — ITSLerdo POO Corte 3")
    print("★"*55)

    crear_usuarios_demo()  # Carga datos de ejemplo al iniciar

    while True:
        print("\n╔══════════════════════════╗")
        print("║        MENÚ PRINCIPAL    ║")
        print("╠══════════════════════════╣")
        print("║  1. Ver todos los usuarios║")
        print("║  2. Saludar a todos      ║")
        print("║  3. Agregar usuario      ║")
        print("║  4. Salir                ║")
        print("╚══════════════════════════╝")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_todos()
        elif opcion == "2":
            saludar_todos()
        elif opcion == "3":
            agregar_usuario()
        elif opcion == "4":
            print("\n  Hasta luego. Cerrando sistema...\n")
            break
        else:
            print("  Opción no válida. Intenta de nuevo.")

# ─────────────────────────────────────────────
#  Punto de entrada
# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu()
