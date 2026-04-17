from calculadora.error import ExpresionInvalida

def romano_a_entero(romano: str) -> int:
    """
    Nivel 6: Conversión total con validaciones integradas para evitar errores de módulos.
    """
    if not romano or not isinstance(romano, str):
        raise ExpresionInvalida("Entrada no válida")

    romano = romano.upper()
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    permitidas = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    # --- ESCUDO DE VALIDACIONES INTEGRADO ---
    
    # 1. Símbolos válidos
    for letra in romano:
        if letra not in v:
            raise ExpresionInvalida("Símbolos inválidos")

    # 2. Repeticiones prohibidas (V, L, D no se repiten)
    for letra in ['V', 'L', 'D']:
        if romano.count(letra) > 1:
            raise ExpresionInvalida("Repetición inválida de V, L o D")

    # 3. Repeticiones máximas (I, X, C, M máximo 3 veces seguidas)
    for letra in ['I', 'X', 'C', 'M']:
        if letra * 4 in romano:
            raise ExpresionInvalida("Repetición inválida de I, X, C o M")

    # 4. Validar Restas y Orden (Lógica combinada)
    i = 0
    ultimo_valor = 4000
    while i < len(romano):
        # Caso de resta
        if i + 1 < len(romano) and v[romano[i]] < v[romano[i+1]]:
            combinacion = romano[i:i+2]
            if combinacion not in permitidas:
                raise ExpresionInvalida("Restas prohibidas")
            # No permitir repetir el símbolo que resta (ej: IIX)
            if i > 0 and romano[i-1] == romano[i]:
                raise ExpresionInvalida("Restas prohibidas")
            
            valor_actual = v[romano[i+1]] - v[romano[i]]
            i += 2
        else:
            valor_actual = v[romano[i]]
            i += 1
        
        if valor_actual > ultimo_valor:
            raise ExpresionInvalida("Orden incorrecto")
        ultimo_valor = valor_actual

    # --- LÓGICA DE CONVERSIÓN ---
    total = 0
    idx = 0
    while idx < len(romano):
        if idx + 1 < len(romano) and v[romano[idx]] < v[romano[idx+1]]:
            total += v[romano[idx+1]] - v[romano[idx]]
            idx += 2
        else:
            total += v[romano[idx]]
            idx += 1
            
    return total