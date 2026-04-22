def validar_repeticiones_icxm(romano: str) -> bool:
    """
    Nivel 2: Verifica que I, X, C, M no se repitan más de 3 veces.
    """
    romano = romano.upper()
    prohibidos = ['IIII', 'XXXX', 'CCCC', 'MMMM']
    return all(p not in romano for p in prohibidos)
