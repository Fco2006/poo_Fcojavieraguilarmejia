#  Examen Práctico Contra Reloj — Clases en PHP

## . Nombre del Proyecto
**Modelado de Clases en PHP** — Examen práctico donde se define la estructura de clases `Paquete` y `Sensor` con propiedades tipadas, visibilidad y uso de clases nativas de PHP.

---

## . Objetivo del Proyecto
Medir la precisión técnica en la **sintaxis de PHP** y la capacidad de **modelado de datos** mediante la definición correcta de clases con propiedades públicas y privadas con tipado estricto, sin el uso de métodos, en un tiempo limitado de 30 minutos.

---

## . Problema que Resuelve
El examen plantea dos escenarios reales del ámbito informático:

- **FastDelivery:** necesita un molde (clase) para sus paquetes de logística, con datos como código de seguimiento, peso y fragilidad.
- **Sistema de monitoreo de plantas:** requiere una clase `Sensor` con identificador, marca, fecha de última lectura y rango máximo.

Ambos casos demuestran cómo modelar entidades del mundo real en clases PHP antes de agregarles comportamiento.

---

## . Tecnologías Utilizadas
| Tecnología | Uso |
|------------|-----|
| PHP 8.x | Definición de clases con tipado estricto |
| XAMPP / Apache | Servidor local para ejecutar `index.php` |
| `DateTime` | Clase nativa de PHP para manejo de fechas |

---

## . Conceptos Aplicados
- Definición de **clases** en PHP (`class`)
- **Propiedades con visibilidad:** `public`, `private`
- **Tipado estricto** de propiedades (`string`, `float`, `bool`, `int`, `DateTime`)
- **Instanciación de objetos** con `new`
- Asignación de valores a propiedades públicas
- Intento de acceso a propiedad privada (error intencional documentado)
- Uso de `require_once` para importar clases
- Uso de la clase nativa `DateTime` de PHP



## . Instrucciones de Ejecución

1. Instalar **XAMPP** y activar **Apache**.
2. Copiar la carpeta del proyecto en:
   ```
   C:/xampp/htdocs/examen/
   ```
3. Abrir el navegador y acceder a:
   ```
   http://localhost/examen/index.php
   ```
4. Verificar que se muestren los datos asignados a `$paqueteA` y al objeto `$sensor`.

### Estructura de archivos
```
examen/
├── index.php                  ← Instancia y prueba de las clases
└── src/
    └── Logistica/
        ├── Paquete.php        ← Clase con propiedades de paquete
        └── Sensor.php         ← Clase con propiedades de sensor
```

---

## . Reflexión Personal

### ¿Qué aprendí?
Aprendí la importancia del **tipado estricto** en PHP moderno: declarar el tipo de cada propiedad hace el código más robusto y predecible. También comprendí claramente la diferencia entre propiedades `public` (accesibles desde fuera de la clase) y `private` (solo accesibles dentro de ella), y cómo PHP lanza un error fatal si intentas acceder a una propiedad privada desde fuera.

### ¿Qué fue difícil?
La **presión del tiempo** fue el mayor reto: 30 minutos obligan a recordar la sintaxis exacta sin depender de búsquedas. También me costó recordar cómo instanciar correctamente la clase nativa `DateTime` y asignarla como valor de una propiedad.

### ¿Qué mejoraría?
- Agregar **métodos getter y setter** para acceder de forma controlada a la propiedad `costoInterno`.
- Implementar **`declare(strict_types=1)`** al inicio de los archivos para activar el modo estricto completo.
- Agregar un método `mostrarInfo()` a cada clase para facilitar la visualización de los datos.
- Documentar cada propiedad con comentarios PHPDoc para mejor legibilidad.

---

*Proyecto desarrollado como Examen Práctico Contra Reloj Corte 1 — Programación Orientada a Objetos | Ingeniería Informática | ITSL*
