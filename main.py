import string

def lexerAritmetico(expresiones):
    tokens = []
    for linea in expresiones:
        # Tokenizar la línea
        palabra = ''
        for char in linea:
            if char in string.whitespace:
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
            elif char in ('+', '*', '=', '^', '(', ')'):
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                tokens.append((char, determinar_tipo(char)))
            elif char in '/':
                if palabra:
                    if palabra[-1] == '/':
                        palabra = linea.split("//", 1)[1].rstrip()
                        tokens.append(( '//' + palabra, determinar_tipo('//' + palabra)))
                        palabra = ''
                        break
                    else:
                        tokens.append((palabra, determinar_tipo(palabra)))
                        palabra = ''
                palabra += char

            elif char.isdigit() or char in ('.', '-', '_', 'E', 'e'):
                palabra += char
            elif char.isalpha():
                if palabra and palabra[-1] == '/':
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                palabra += char
            else:
                if palabra:
                    tokens.append((palabra, determinar_tipo(palabra)))
                    palabra = ''
                tokens.append((char, determinar_tipo(char)))
        if palabra:
            tokens.append((palabra, determinar_tipo(palabra)))
        tokens.append(('', 'Enter'))
    return tokens

def determinar_tipo(token):
    if token.startswith('//'):
        return 'Comentario'
    elif token in ('+', '-'):
        return 'Suma' if token == '+' else 'Resta'
    elif token.isdigit() or (token[0] == '-' and token.count('-') == 1 and token.replace('-', '').isdigit()):
        return 'Entero'
    elif token in ('*', '/', '^'):
        return 'Multiplicación' if token == '*' else 'División' if token == '/' else 'Potencia'
    elif token == '(':
        return 'Paréntesis que abre'
    elif token == ')':
        return 'Paréntesis que cierra'
    elif token == '=':
        return 'Asignación'
    elif token[0].isalpha() and token.replace('_', '').isalnum():
        return 'Variable'
    elif 'e' in token.lower() and token.lower().count('e') == 1:    #Exponencial
        if (determinar_tipo(token[0:token.lower().find('e')]) == 'Entero' or determinar_tipo(token[0:token.lower().find('e')]) == 'Real') and determinar_tipo(token[token.lower().find('e')+1:]) == 'Entero':
            #Si antes de la e hay un entero o un numero real y despues hay un numero entero
            return 'Real'
        else:
            return 'Error'
    elif '.' in token and token.count('.') == 1:    #Float
        if token.replace('.', '').isdigit():
            return 'Real'
        elif token[0] == '-' and token.count('-') == 1 and token.replace('.', '').replace('-', '').isdigit():   #Float negativo
            return 'Real'
        else:
            return 'Error'
    else:
        return 'Error'

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


