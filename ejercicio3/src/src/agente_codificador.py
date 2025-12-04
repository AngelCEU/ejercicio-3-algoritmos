# src/agente_codificador.py

from typing import Dict, Tuple, Optional
import heapq

# Use absolute import so the module can be executed as a script
from nodo_codigo import NodoCodigo


class AgenteCodificador:
    """
    Agente principal del Protocolo Fantasma.
    Orquesta el análisis de frecuencias, construcción del árbol,
    generación de tabla de códigos, codificación y decodificación.
    """

    def _analizar_frecuencias(self, mensaje: str) -> Dict[str, int]:
        """
        Analiza el mensaje y devuelve un diccionario símbolo -> frecuencia.
        """
        frecuencias: Dict[str, int] = {}
        for caracter in mensaje:
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
        return frecuencias

    def _construir_arbol(self, frecuencias: Dict[str, int]) -> Optional[NodoCodigo]:
        """
        Construye el árbol de Huffman usando una cola de prioridad (heapq).
        Devuelve la raíz del árbol.
        """
        # Caso borde: mensaje vacío
        if not frecuencias:
            return None

        heap = []

        # Crear nodo hoja por cada símbolo y añadir al heap
        for simbolo, freq in frecuencias.items():
            nodo = NodoCodigo(simbolo, freq)
            heapq.heappush(heap, nodo)

        # Caso borde: solo un tipo de símbolo
        if len(heap) == 1:
            # Crear nodo raíz con un solo hijo para evitar código vacío
            unico = heapq.heappop(heap)
            raiz = NodoCodigo(None, unico.frecuencia)
            raiz.izquierda = unico
            heapq.heappush(heap, raiz)

        # Combinar hasta que quede un solo nodo (la raíz)
        while len(heap) > 1:
            nodo1 = heapq.heappop(heap)
            nodo2 = heapq.heappop(heap)

            padre = NodoCodigo(None, nodo1.frecuencia + nodo2.frecuencia)
            padre.izquierda = nodo1
            padre.derecha = nodo2

            heapq.heappush(heap, padre)

        return heap[0]

    def _generar_tabla_codigos(self, arbol_raiz: NodoCodigo) -> Dict[str, str]:
        """
        Recorre el árbol con DFS para generar la tabla de códigos
        símbolo -> cadena de bits.
        """
        tabla: Dict[str, str] = {}

        def dfs(nodo: NodoCodigo, prefijo: str):
            if nodo is None:
                return

            if nodo.es_hoja():
                # Caso borde: árbol con un solo símbolo; asignar "0"
                tabla[nodo.simbolo] = prefijo or "0"
                return

            dfs(nodo.izquierda, prefijo + "0")
            dfs(nodo.derecha, prefijo + "1")

        dfs(arbol_raiz, "")
        return tabla

    def codificar(self, mensaje: str) -> Tuple[str, NodoCodigo, Dict[str, str]]:
        """
        Codifica un mensaje de texto plano en una secuencia de bits.

        Devuelve:
            secuencia_bits (str): bits resultantes.
            arbol_raiz (NodoCodigo): raíz del árbol, para decodificación.
            tabla_codigos (Dict[str, str]): tabla símbolo -> bits (para mostrar).
        """
        if mensaje == "":
            return "", None, {}

        frecuencias = self._analizar_frecuencias(mensaje)
        arbol_raiz = self._construir_arbol(frecuencias)
        tabla_codigos = self._generar_tabla_codigos(arbol_raiz)

        secuencia_bits = "".join(tabla_codigos[c] for c in mensaje)
        return secuencia_bits, arbol_raiz, tabla_codigos

    def decodificar(self, secuencia_bits: str, arbol_raiz: NodoCodigo) -> str:
        """
        Decodifica una secuencia de bits usando el árbol raíz.
        """
        if arbol_raiz is None:
            return ""

        if not secuencia_bits:
            # Secuencia vacía -> mensaje vacío
            return ""

        mensaje_decodificado = []
        nodo_actual = arbol_raiz

        for bit in secuencia_bits:
            if bit == "0":
                nodo_actual = nodo_actual.izquierda
            elif bit == "1":
                nodo_actual = nodo_actual.derecha
            else:
                raise ValueError(f"Bit inválido en la secuencia: {bit!r}")
            # Detectar secuencia malformada que lleva a un nodo inexistente
            if nodo_actual is None:
                raise ValueError("Secuencia de bits malformada para el árbol dado (nodo None alcanzado).")

            # Si se llega a una hoja, se recupera el símbolo
            if nodo_actual.es_hoja():
                mensaje_decodificado.append(nodo_actual.simbolo)
                nodo_actual = arbol_raiz

        # Si al terminar la secuencia no hemos vuelto a la raíz, la secuencia está incompleta
        if nodo_actual is not arbol_raiz:
            raise ValueError("Secuencia de bits incompleta: termina a mitad de un código.")

        return "".join(mensaje_decodificado)
