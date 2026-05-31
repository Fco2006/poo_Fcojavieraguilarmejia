# Sistema de Usuarios con Herencia en Python

## . Nombre del Proyecto
**Sistema de Gestión de Usuarios con Herencia** — Aplicación orientada a objetos en Python que modela distintos tipos de usuarios usando herencia y polimorfismo.

---

## . Objetivo del Proyecto
Aplicar los conceptos de **herencia** y **polimorfismo** en Python creando una clase base `Usuario` y clases derivadas (`Admin`, `Cliente`, `Invitado`), reutilizando atributos y métodos, y demostrando cómo cada tipo de usuario tiene comportamientos y permisos distintos.

---

## . Problema que Resuelve
Una plataforma digital necesita controlar distintos tipos de usuarios:
- **Administradores:** acceso total al sistema.
- **Clientes:** acceso estándar con sistema de puntos.
- **Invitados:** acceso limitado de solo lectura.

Todos comparten información básica (nombre, email), pero cada uno tiene permisos y comportamientos diferentes. El sistema evita duplicar código usando herencia.

---

## . Tecnologías Utilizadas
| Tecnología | Uso |
|------------|-----|
| Python 3.x | Lenguaje principal del proyecto |
| POO (Clases y Herencia) | Modelado del sistema de usuarios |
| Terminal / CMD | Entorno de ejecución |

---

## . Conceptos Aplicados
- **Herencia:** las clases `Admin`, `Cliente` e `Invitado` heredan de `Usuario`
- **Polimorfismo:** sobreescritura del método `acceso_sistema()` en cada clase
- **`super()`:** llamada al constructor de la clase padre
- **Constructores (`__init__`):** inicialización de atributos propios y heredados
- **Encapsulamiento:** separación de responsabilidades por clase
- **Validación de email**
- **Menú interactivo** en consola
- **Recorrido polimórfico** de lista de usuarios

---


## . Instrucciones de Ejecución

1. Asegurarse de tener **Python 3.x** instalado:
   ```bash
   python --version
   ```
2. Clonar o descargar la carpeta del proyecto.
3. Navegar a la carpeta del proyecto en la terminal:
   ```bash
   cd ruta/del/proyecto
   ```
4. Ejecutar el programa principal:
   ```bash
   python main.py
   ```

### Estructura de archivos
```
proyecto_usuarios/
├── usuario.py      ← Clase base Usuario
├── admin.py        ← Clase Admin (hereda de Usuario)
├── cliente.py      ← Clase Cliente (hereda de Usuario)
├── invitado.py     ← Clase Invitado (hereda de Usuario)
└── main.py         ← Programa principal, crea e interactúa con los usuarios
```

---

## . Reflexión Personal

### ¿Qué aprendí?
Aprendí a usar herencia en Python de forma práctica: cómo una clase hija puede reutilizar el constructor del padre con `super().__init__()` y al mismo tiempo agregar sus propios atributos. También comprendí el polimorfismo al ver cómo el mismo método `acceso_sistema()` se comporta diferente dependiendo del tipo de objeto.

### ¿Qué fue difícil?
Lo más difícil fue entender cuándo usar `super()` y cuándo no, especialmente al agregar atributos propios de la clase hija sin perder los del padre. También me costó organizar los archivos en módulos separados e importarlos correctamente.

### ¿Qué mejoraría?
- Agregar una **interfaz gráfica** con `tkinter` para hacer el sistema más visual.
- Implementar **persistencia de datos** guardando los usuarios en un archivo JSON.
- Añadir más niveles de herencia (por ejemplo, `AdminSuperior` que herede de `Admin`).
- Mejorar la validación de email con expresiones regulares (`re` module).

---

*Proyecto desarrollado como actividad de evaluación ABPj Corte 3 — Programación Orientada a Objetos | Ingeniería Informática | ITSL*
