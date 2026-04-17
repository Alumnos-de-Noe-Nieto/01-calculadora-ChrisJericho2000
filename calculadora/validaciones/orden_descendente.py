def validar_orden_descendente(cadena: str) -> bool:
    """
    Nivel 4: Valida que los símbolos estén en orden descendente.
    """
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    
    i = 0
    while i < len(cadena):
        # Caso: Sustracción (ej: IV, CM)
        if i + 1 < len(cadena) and valores[cadena[i]] < valores[cadena[i+1]]:
            combinacion = cadena[i:i+2]
            if combinacion not in sustracciones:
                return False
            # Regla: No repetir antes de una resta (ej: IIV es mal)
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            # Regla: El que sigue después de la resta debe ser menor al valor restado
            if i + 2 < len(cadena) and valores[cadena[i+2]] >= valores[cadena[i]]:
                return False
            i += 2
        # Caso: Orden normal descendente
        else:
            if i + 1 < len(cadena) and valores[cadena[i]] < valores[cadena[i+1]]:
                return False
            i += 1
    return True