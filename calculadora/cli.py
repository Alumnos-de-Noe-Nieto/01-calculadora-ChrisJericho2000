import sys
from calculadora.expresion import evaluar
from calculadora.error import ExpresionInvalida

def main():
    """
    Nivel 9: Punto de entrada de la aplicación.
    Maneja el bucle de la calculadora en la consola.
    """
    print("========================================")
    print("   CALCULADORA DE NÚMEROS ROMANOS")
    print("      (Escribe 'salir' para terminar)")
    print("========================================")

    while True:
        try:
            # Pedimos la operación al usuario
            entrada = input("\nCalculadora > ")
            
            # Opción para cerrar el programa
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("¡Adiós! Gracias por usar la calculadora.")
                break
            
            # Evaluamos la expresión
            resultado = evaluar(entrada)
            print(f"Resultado: {resultado}")

        except ExpresionInvalida as e:
            # Mostramos errores de validación (romanos mal escritos, etc.)
            print(f"Error: {e}")
        except KeyboardInterrupt:
            # Por si el usuario presiona Ctrl+C
            print("\nSaliendo...")
            break
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()