from dataclasses import dataclass
from calculadora.error import ExpresionInvalida

@dataclass
class Token:
    """Representa una pieza de la expresión (Número, Operador o Espacio)."""
    tipo: str
    valor: str
    posicion: int

def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Nivel 7.1: Función principal que coordina la tokenización y la validación.
    """
    if not expresion or not expresion.strip():
        return []
    
    # Intentamos convertir el texto en tokens
    tokens = tokenizar_expresion(expresion)
    
    # Validamos que la estructura sea correcta (ej: Romano + Romano)
    if not validar_estructura_tokens(tokens):
        raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
        
    return tokens

def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Nivel 7.2: Convierte la cadena de texto en una lista de objetos Token.
    """
    tokens = []
    i = 0
    while i < len(expresion):
        char = expresion[i]
        
        if char == ' ':
            tokens.append(Token('ESPACIO', ' ', i))
            i += 1
        elif char == '+':
            tokens.append(Token('SUMA', '+', i))
            i += 1
        elif char == '-':
            tokens.append(Token('RESTA', '-', i))
            i += 1
        elif char.upper() in 'IVXLCDM':
            inicio = i
            while i < len(expresion) and expresion[i].upper() in 'IVXLCDM':
                i += 1
            tokens.append(Token('ROMANO', expresion[inicio:i].upper(), inicio))
        else:
            # Si hay algo que no es romano, espacio, + o -, lanzamos error
            raise ExpresionInvalida(f"Carácter inválido '{char}' en posición {i}")
            
    return tokens

def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Nivel 7.3: Verifica la alternancia correcta: ROMANO -> OPERADOR -> ROMANO.
    """
    # Quitamos los espacios para validar solo el contenido real
    limpios = [t for t in tokens if t.tipo != 'ESPACIO']
    
    # Una operación mínima requiere 3 elementos (A + B)
    if len(limpios) < 3:
        return False
        
    # El número de elementos debe ser impar (A + B o A + B - C...)
    if len(limpios) % 2 == 0:
        return False
        
    for i, t in enumerate(limpios):
        if i % 2 == 0:
            # Posiciones 0, 2, 4... DEBEN ser números romanos
            if t.tipo != 'ROMANO':
                return False
        else:
            # Posiciones 1, 3, 5... DEBEN ser operadores
            if t.tipo not in ['SUMA', 'RESTA']:
                return False
                
    return True