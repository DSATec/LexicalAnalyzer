import string

def lexerAritmetico(expresiones):
    tokens = []
    for linea in expresiones:
        # Tokenizar la línea
        palabra = ''
        in_numero_cientifico = False
        for char in linea:
            if char in string.whitespace:
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
            elif char in ('+', '*', '=', '^', '(', ')'):
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                tokens.append((char, determinar_tipo(char)))
            elif char in '/':
                if palabra:
                    if palabra[-1] == '/':
                        palabra = linea.split("//", 1)[1].rstrip()
                        tokens.append(( '//' + palabra, determinar_tipo('//' + palabra)))
                        palabra = ''
                        in_numero_cientifico = False
                        break
                    else:
                        tokens.append((palabra, determinar_tipo(palabra)))
                        palabra = ''
                        in_numero_cientifico = False
                palabra += char

            elif char == '-' or char.isdigit() or char in ('.', 'E', 'e'):
                palabra += char
                if char in ('E', 'e'):
                    in_numero_cientifico = True
            elif char.isalpha():
                if palabra and palabra[-1] == '/':
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                palabra += char
            else:
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
        if palabra:
            tokens.append((palabra, determinar_tipo(palabra)))
    return tokens

def determinar_tipo(token):
    if token.startswith('//'):
        return 'Comentario'
    elif token.replace('-','').isdigit():
        return 'Entero'
    elif '.' in token or 'E' in token or 'e' in token and token.replace('.', '').replace('E' or 'e', '').replace('-','').isdigit():
        return 'Real'
    elif token in ('+', '-'):
        return 'Suma' if token == '+' else 'Resta'
    elif token in ('*', '/', '^'):
        return 'Multiplicación' if token == '*' else 'División' if token == '/' else 'Potencia'
    elif token == '(':
        return 'Paréntesis que abre'
    elif token == ')':
        return 'Paréntesis que cierra'
    elif token == '=':
        return 'Asignación'
    elif token.isalpha():
        return 'Variable'
    else:
        return 'Identificador'

def main():
    # Leer el archivo de entrada
    with open('input.txt', 'r') as archivo:
        expresiones = archivo.readlines()

    # Tokenizar las expresiones
    tokens = lexerAritmetico(expresiones)

    # Imprimir la tabla de tokens
    print("Token\t\t\t\tTipo")
    print("------------------------------------------------------")
    for token, tipo in tokens:
        print(f"{token}\t\t\t\t{tipo}")

main()
