def validar_simbolos(romano: str) -> bool:
    """
    Nivel 1: Verifica que existan caracteres romanos válidos y no esté vacío.
    """
    if not romano:
        return False
    alfabeto_valido = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(letra in alfabeto_valido for letra in romano.upper())
