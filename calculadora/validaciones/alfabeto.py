def validar_simbolos(romano: str) -> bool:
    """
    Nivel 1: Valida que la cadena contenga solo caracteres romanos permitidos.
    """
    if not romano:
        return False
        
    alfabeto_valido = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    
    for letra in romano.upper():
        if letra not in alfabeto_valido:
            return False
            
    return True