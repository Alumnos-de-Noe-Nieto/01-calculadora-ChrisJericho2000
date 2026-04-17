def validar_repeticiones_vld(romano: str) -> bool:
    """
    Nivel 3: Valida que V, L, D no se repitan nunca.
    """
    romano = romano.upper()
    prohibidos = ['VV', 'LL', 'DD']
    for p in prohibidos:
        if p in romano:
            return False
    return True