def validar_simbolos(romano: str) -> bool:
    """
    Nivel 1: Verifica que solo existan caracteres romanos válidos.
    """
    alfabeto_valido = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(letra in alfabeto_valido for letra in romano.upper())
