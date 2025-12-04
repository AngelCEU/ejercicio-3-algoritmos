# src/nodo_codigo.py

class NodoCodigo:
    """
    Nodo para el árbol de Huffman (Protocolo Fantasma).

    Atributos:
        simbolo (str | None): carácter del mensaje (solo en hojas).
        frecuencia (int): frecuencia total de este nodo.
        izquierda (NodoCodigo | None): hijo izquierdo.
        derecha (NodoCodigo | None): hijo derecho.
    """
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def es_hoja(self):
        return self.izquierda is None and self.derecha is None

    def __lt__(self, other):
        """
        Permite comparar nodos por frecuencia para usarlos en heapq.
        """
        return self.frecuencia < other.frecuencia

    def __repr__(self):
        return f"NodoCodigo(simbolo={self.simbolo!r}, frecuencia={self.frecuencia})"
