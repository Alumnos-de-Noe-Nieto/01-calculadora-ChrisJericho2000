def validar_repeticiones_icxm(romano: str) -> bool:
    """
    Nivel 2: Valida que I, X, C, M no se repitan más de 3 veces.
    """
    romano = romano.upper()
    prohibidos = ['IIII', 'XXXX', 'CCCC', 'MMMM']
    for p in prohibidos:
        if p in romano:
            return False
    return True