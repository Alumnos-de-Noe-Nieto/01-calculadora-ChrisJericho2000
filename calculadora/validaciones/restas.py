def validar_restas(romano: str) -> bool:
    """
    Nivel 5: Valida las 6 restas permitidas y prohíbe repeticiones 
    del sustraendo (ej: IIV) o restas no estándar (ej: IL).
    """
    romano = romano.upper()
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    permitidas = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    
    i = 0
    while i < len(romano) - 1:
        actual = romano[i]
        siguiente = romano[i+1]
        
        # Detectamos si hay una resta (valor menor antes de uno mayor)
        if valores[actual] < valores[siguiente]:
            # REGLA 1: Solo las 6 combinaciones oficiales
            if (actual + siguiente) not in permitidas:
                return False
            
            # REGLA 2: No se puede repetir el símbolo que resta (ej: IIV es False)
            # Si hay un carácter antes y es igual al actual, es inválido
            if i > 0 and romano[i-1] == actual:
                return False
            
            # Saltamos ambos caracteres porque ya validamos el par
            i += 2
        else:
            i += 1
            
    return True