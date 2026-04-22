from calculadora.error import ExpresionInvalida
from calculadora.expresion import evaluar


def main():
    """
    Nivel 9: Punto de entrada de la aplicación.
    """
    print("========================================")
    print("   CALCULADORA DE NÚMEROS ROMANOS")
    print("      (Escribe 'salir' para terminar)")
    print("========================================")

    while True:
        try:
            entrada = input("\nCalculadora > ")
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("¡Adiós! Gracias por usar la calculadora.")
                break
            resultado = evaluar(entrada)
            print(f"Resultado: {resultado}")
        except ExpresionInvalida as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()
