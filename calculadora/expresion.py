from calculadora.parser import evaluar_expresion
from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida

def evaluar(expresion_texto: str) -> int:
    """
    Nivel 8: Orquestación con validaciones semánticas estrictas.
    """
    # 1. Validar expresión vacía o solo espacios (Test 8.13)
    if not expresion_texto or not expresion_texto.strip():
        raise ExpresionInvalida("La expresión no puede estar vacía")

    # 2. Parsear (Esto lanzará ExpresionInvalida si la estructura es mala)
    try:
        tokens = evaluar_expresion(expresion_texto)
    except Exception:
        raise ExpresionInvalida(f"Error al parsear: {expresion_texto}")

    # 3. Limpiar espacios
    limpios = [t for t in tokens if t.tipo != 'ESPACIO']
    
    if not limpios:
        raise ExpresionInvalida("No se encontraron componentes válidos")

    # 4. Procesar la operación
    try:
        # Primer número
        resultado = romano_a_entero(limpios[0].valor)
        
        i = 1
        while i < len(limpios):
            operador = limpios[i].valor
            siguiente_valor = romano_a_entero(limpios[i+1].valor)
            
            if operador == '+':
                resultado += siguiente_valor
            elif operador == '-':
                resultado -= siguiente_valor
            
            i += 2
            
        # 5. Validar resultado (Los romanos no tienen 0 ni negativos) (Test 8.7c)
        if resultado <= 0:
            raise ExpresionInvalida("El resultado debe ser un número romano positivo (mayor a 0)")
            
        return resultado

    except ExpresionInvalida as e:
        # Re-lanzamos cualquier error semántico del conversor (Test 8.9c)
        raise e
    except Exception:
        raise ExpresionInvalida("Error semántico en la expresión")