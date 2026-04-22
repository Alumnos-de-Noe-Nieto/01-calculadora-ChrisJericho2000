def validar_restas(romano: str) -> bool:
    """
    Nivel 5: Valida las 6 restas permitidas y prohíbe restas no estándar.
    """
    romano = romano.upper()
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    permitidas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    for i in range(len(romano) - 1):
        actual = romano[i]
        siguiente = romano[i + 1]
        if v[actual] < v[siguiente]:
            # Si hay una resta, debe estar en la lista de permitidas
            if (actual + siguiente) not in permitidas:
                return False
            # No se puede repetir el símbolo que resta (ej. IIX)
            if i > 0 and romano[i - 1] == actual:
                return False
    return True
