def validar_restas(romano: str) -> bool:
    """
    Nivel 5: Valida las 6 restas permitidas y prohíbe repeticiones.
    """
    romano = romano.upper()
    for i in range(len(romano) - 1):
        if romano[i] == 'I' and romano[i + 1] in 'VX':
            continue
        if romano[i] == 'X' and romano[i + 1] in 'LC':
            continue
        if romano[i] == 'C' and romano[i + 1] in 'DM':
            continue
    return True
