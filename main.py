import string

def tokenize(expresiones):
    tokens = []
    for linea in expresiones:
        # Eliminar los comentarios
        comentario_index = linea.find('//')
        if comentario_index != -1:
            linea = linea[:comentario_index]
        # Tokenizar la línea
        palabra = ''
        in_numero_cientifico = False
        for char in linea:
            if char in string.whitespace:
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
            elif char in ('+', '*', '/', '=', '^'):
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                tokens.append((char, determinar_tipo(char)))
            elif char == '(':
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                tokens.append((char, 'Paréntesis que abre'))
            elif char == ')':
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                tokens.append((char, 'Paréntesis que cierra'))
            elif char == '-':
                if palabra and (palabra.isdigit() or '.' in palabra):
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                    in_numero_cientifico = False
                palabra += char
                in_numero_cientifico = True
            elif char.isdigit() or char in ('.', 'E', 'e'):
                palabra += char
                if char in ('E', 'e'):
                    in_numero_cientifico = True
            elif char.isalpha():
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
    if token.isdigit():
        return 'Entero'
    elif '.' in token and token.replace('.', '').replace('E', '').isdigit():
        return 'Real'
    elif 'E' in token or 'e' in token:
        return 'Real' if token[-1] != '-' else 'Identificador'
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
    elif token.startswith('//'):
        return 'Comentario'
    else:
        return 'Que rayos es esto???????????????????????'

def main():
    # Leer el archivo de entrada
    with open('input.txt', 'r') as archivo:
        expresiones = archivo.readlines()

    # Tokenizar las expresiones
    tokens = tokenize(expresiones)

    # Imprimir la tabla de tokens
    print("Token\t\tTipo")
    print("-----------------------")
    for token, tipo in tokens:
        print(f"{token}\t\t{tipo}")

if __name__ == "__main__":
    main()
