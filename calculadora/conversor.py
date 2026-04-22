from calculadora.error import ExpresionInvalida


def romano_a_entero(romano: str) -> int:
    """
    Nivel 6: Conversión total con validaciones integradas.
    """
    if not romano or not isinstance(romano, str):
        raise ExpresionInvalida("Entrada no válida")

    romano = romano.upper()
    v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    permitidas = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    for letra in romano:
        if letra not in v:
            raise ExpresionInvalida("Símbolos inválidos")

    for letra in ['V', 'L', 'D']:
        if romano.count(letra) > 1:
            raise ExpresionInvalida("Repetición inválida de V, L o D")

    for letra in ['I', 'X', 'C', 'M']:
        if letra * 4 in romano:
            raise ExpresionInvalida("Repetición inválida de I, X, C o M")

    i = 0
    ultimo_valor = 4000
    while i < len(romano):
        if i + 1 < len(romano) and v[romano[i]] < v[romano[i+1]]:
            combinacion = romano[i:i+2]
            if combinacion not in permitidas:
                raise ExpresionInvalida("Restas prohibidas")
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
