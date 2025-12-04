# src/main.py

from agente_codificador import AgenteCodificador


def mostrar_tabla_codigos(tabla_codigos):
    print("\n=== Tabla de Códigos (Clave de Sesión) ===")
    for simbolo, codigo in sorted(tabla_codigos.items(), key=lambda x: (len(x[1]), x[0])):
        # Representar caracteres especiales de forma visible
        if simbolo == " ":
            simb_repr = "<espacio>"
        elif simbolo == "\n":
            simb_repr = "<nueva_linea>"
        elif simbolo == "\t":
            simb_repr = "<tab>"
        else:
            simb_repr = simbolo
        print(f"'{simb_repr}': {codigo}")


def main():
    print("=== PROTOCOLO FANTASMA – TERMINAL DE MANDO ===")
    print("Introduzca el mensaje clasificado a ofuscar:")

    mensaje = input("> ")

    agente = AgenteCodificador()

    secuencia_bits, arbol_raiz, tabla_codigos = agente.codificar(mensaje)

    if arbol_raiz is None:
        print("\n[!] Mensaje vacío. No hay nada que codificar.")
        return

    mostrar_tabla_codigos(tabla_codigos)

    print("\n=== Transmisión Codificada ===")
    print(secuencia_bits)

    mensaje_recuperado = agente.decodificar(secuencia_bits, arbol_raiz)

    print("\n=== Verificación de Integridad ===")
    print("Mensaje decodificado:")
    print(mensaje_recuperado)

    if mensaje_recuperado == mensaje:
        print("\n[OK] Integridad verificada: el mensaje decodificado coincide con el original.")
    else:
        print("\n[ALERTA] Integridad comprometida: el mensaje decodificado NO coincide con el original.")


if __name__ == "__main__":
    main()
