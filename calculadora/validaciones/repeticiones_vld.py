def validar_repeticiones_vld(romano: str) -> bool:
    """
    Nivel 3: Verifica que V, L, D no se repitan.
    """
    romano = romano.upper()
    prohibidos = ['VV', 'LL', 'DD']
    return all(p not in romano for p in prohibidos)
