# ejercicio-3-algoritmos


# 🕵️‍♂️ Asunto: Misión - Desarrollo del "Protocolo Fantasma"

> **Agente, su misión, si decide aceptarla, es desarrollar un nuevo sistema de codificación de transmisiones.**
>
> Nuestros canales estándar han sido comprometidos. Necesitamos un método de ofuscación dinámico para enviar inteligencia vital a nuestros agentes de campo.

Llamamos a este sistema **"Protocolo Fantasma"**. En lugar de usar una clave de cifrado fija, el protocolo genera una clave de codificación única basada en la frecuencia del contenido del propio mensaje. Esto lo hace resistente al análisis de patrones estándar del enemigo.

Su objetivo es construir un prototipo funcional en **Python** usando **Programación Orientada a Objetos** y una estructura de datos de **árbol de codificación (Huffman)**.

Esta misión evalúa su capacidad para:

  * El diseño de algoritmos.
  * La manipulación de estructuras de datos complejas (árboles y colas de prioridad).
  * La organización de código limpio y reutilizable.

-----

## *⚠️ Este mensaje no se autodestruirá, pero su entorno virtual (venv) deberá ser eliminado tras la entrega para no dejar rastro.*

## 🎯 Objetivos de la Misión (Evaluación)

Su éxito en esta operación dependerá de su capacidad para:

1.  Diseñar clases encapsuladas y robustas para la estructura del árbol (`NodoCodigo`).
2.  Implementar el algoritmo de construcción de árbol desde una cola de prioridad (`heapq`).
3.  Dominar los recorridos de árbol (**DFS**) para generar tablas de codificación y para la decodificación.
4.  Organizar su "software de espionaje" en una estructura de proyecto profesional y desplegable (`src/`, `README.md`).

-----

## ⚙️ Parámetros de la Misión (Requisitos Funcionales)

### 📊 Análisis Táctico (Frecuencias)

El sistema debe escanear cualquier mensaje (`string`) y determinar la frecuencia de aparición de cada simbolo (carácter).

### 🌳 Construcción del Árbol de Códigos

A partir del análisis de frecuencias, debe construir el árbol de codificación binario.

  * Use una **cola de prioridad (min-heap)** del módulo `heapq` para ensamblar el árbol.
  * Esto garantiza que los símbolos más frecuentes tengan las rutas de bits más cortas (más cerca de la raíz).

### 🗝️ Generación de la "Clave" (Tabla de Códigos)

El sistema debe recorrer el árbol (usando un algoritmo de búsqueda en profundidad - **DFS**) para generar la "clave" de codificación (un diccionario, ej. `'A': '01'`, `'!': '101'`) para cada símbolo.

### 🔒 Codificación (Ofuscación)

Implementar un método `codificar(mensaje)` que use la clave generada para convertir el mensaje de texto plano en una secuencia de bits ofuscada (representada como un string de `'0'` y `'1'`).

### 🔓 Decodificación (Recuperación)

Implementar un método `decodificar(secuencia_bits, arbol_raiz)` que use el árbol raíz (que actúa como la "llave maestra" de esta transmisión) para decodificar la secuencia de bits y recuperar el mensaje original exacto y sin pérdida de información.

### 🧳 Estructura del Maletín (Proyecto)

Mantener la estructura de proyecto profesional (`src/`, `README.md`, `requirements.txt`).

  * El `README.md` debe contener las "Instrucciones de Operación" (cómo ejecutar el `main.py`).

-----

## 🚀 Fases de la Operación (Desglose)

### Fase 1: El Componente 'Nodo' (Modelado POO)

Implemente la clase `NodoCodigo` (o `NodoHuffman`) en `src/nodo_codigo.py`.

**Atributos:**

  * `simbolo`: El carácter (para nodos hoja) o `None` (para nodos internos).
  * `frecuencia`: El peso del nodo (suma de frecuencias).
  * `izquierda`: Referencia al hijo izquierdo (`NodoCodigo`).
  * `derecha`: Referencia al hijo derecho (`NodoCodigo`).

> **Crucial:** La clase debe implementar el método `__lt__(self, other)` (menor que) basado en la frecuencia. Esto es esencial para que los nodos funcionen en la cola de prioridad (`heapq`).

### Fase 2: El 'Agente' Codificador (Clase Principal)

Implemente la clase `AgenteCodificador` (o `ModuloFantasma`) en `src/agente_codificador.py`. Esta clase orquestará toda la operación.

**Métodos Sugeridos:**

  * `_analizar_frecuencias(self, mensaje) -> Dict[str, int]`

      * Devuelve un diccionario de `simbolo: frecuencia`.

  * `_construir_arbol(self, frecuencias) -> NodoCodigo`

      * Crea un nodo hoja para cada `(simbolo, frecuencia)`.
      * Los añade a una cola de prioridad (`heapq.heappush`).
      * Mientras haya más de un nodo en la cola:
          * Extrae los dos nodos con menor frecuencia (`heapq.heappop`).
          * Crea un nuevo nodo interno (padre) con la suma de sus frecuencias.
          * Inserta el nuevo nodo padre de nuevo en la cola.
      * Devuelve el único nodo que queda (la raíz del árbol).

  * `_generar_tabla_codigos(self, arbol_raiz) -> Dict[str, str]`

      * Implementa un recorrido recursivo (**DFS**) del árbol para construir el diccionario de códigos.

  * `codificar(self, mensaje) -> (str, NodoCodigo)`

      * Llama a `_analizar_frecuencias`.
      * Llama a `_construir_arbol` (guarda la raíz).
      * Llama a `_generar_tabla_codigos`.
      * Recorre el mensaje y usa la tabla para construir el string de bits.
      * Devuelve la `secuencia_bits` y el `arbol_raiz` (la "llave").

  * `decodificar(self, secuencia_bits, arbol_raiz) -> str`

      * Recorre la `secuencia_bits` bit a bit.
      * Por cada bit, camina por el `arbol_raiz` ('0' = izquierda, '1' = derecha).
      * Cuando llega a un nodo hoja (tiene un `simbolo`), añade ese símbolo al resultado y vuelve a la `arbol_raiz` para el siguiente bit.

### Fase 3: Estructura del Proyecto (Protocolo de Despliegue)

Organice sus herramientas en el maletín estándar. Las pruebas y métricas han sido eliminadas por HQ para agilizar el despliegue.

```text
proyecto-fantasma/
├─ src/
│  ├─ nodo_codigo.py        # Clase NodoCodigo
│  ├─ agente_codificador.py # Clase AgenteCodificador
│  └─ main.py               # CLI para operar el protocolo
├─ requirements.txt         # (Probablemente solo 'pytest' si se añade después)
└─ README.md                # Instrucciones de Operación
```

### Fase 4: La Terminal de Mando (main.py Opcional)

Implemente una **Interfaz de Línea de Comandos** (`main.py`) para que cualquier agente pueda operar el protocolo:

1.  Solicitar un mensaje clasificado por `input()`.
2.  Instanciar el `AgenteCodificador`.
3.  Llamar a `codificar()`.
4.  Mostrar al agente:
      * La tabla de códigos generada (la "clave" de la sesión).
      * La transmisión codificada (el string de bits).
      * El mensaje decodificado (para verificar la integridad de la transmisión).
