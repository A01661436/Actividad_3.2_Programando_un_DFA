import re
import sys

def print_table(data, headers):
    max_widths = [max(len(str(x)) for x in col) for col in zip(*data, headers)]

    format_string = " | ".join(["{:<" + str(width) + "}" for width in max_widths])
    separator = "-+-".join(["-" * width for width in max_widths])

    print(format_string.format(*headers))
    print(separator)

    for row in data:
        print(format_string.format(*row))

def lexerAritmetico(archivo):
    with open(archivo, 'r') as file:
        content = file.readlines()

    table_data = []

    for line in content:
        tokens = token_generator(line.strip())
        for token in tokens:
            table_data.append(token)
    
    print_table(table_data, headers=["Token", "Tipo"])

def token_generator(line):
    state = 0
    lexeme = ''
    tokens = []

    for char in line + '\n':
        state, lexeme = process_char(state, char, lexeme, tokens)
    
    return tokens

def process_char(state, char, lexeme, tokens):
    if state == 0:
        if char.isalpha():
            return 1, char
        elif char.isdigit():
            return 2, char
        elif char == '.':
            return 3, char
        elif char == '-':
            return 7, char
        elif char in "+=*/":
            tokens.append((char, token_type(char)))
            return 0, ''
        elif char == '^':
            tokens.append((char, "Potencia"))
            return 0, ''
        elif char == '(':
            tokens.append((char, "Paréntesis que abre"))
            return 0, ''
        elif char == ')':
            tokens.append((char, "Paréntesis que cierra"))
            return 0, ''
        elif char == '#':
            lexeme = char
            return 8, lexeme
        elif char.isspace():
            return 0, ''
    elif state == 1:
        if char.isalnum() or char == '_':
            return 1, lexeme + char
        else:
            tokens.append((lexeme, "Variable"))
            return process_char(0, char, '', tokens)
    elif state == 2:
        if char.isdigit():
            return 2, lexeme + char
        elif char == '.':
            return 3, lexeme + char
        elif char in 'Ee':
            return 4, lexeme + char
        else:
            tokens.append((lexeme, "Entero"))
            return process_char(0, char, '', tokens)
    elif state == 3:
        if char.isdigit():
            return 3, lexeme + char
        elif char in 'Ee':
            return 4, lexeme + char
        else:
            tokens.append((lexeme, "Real"))
            return process_char(0, char, '', tokens)
    elif state == 4:
        if char.isdigit():
            return 4, lexeme + char
        elif char == '-':
            return 5, lexeme + char
        elif char == '+':
            return 6, lexeme + char
        else:
            tokens.append((lexeme, "Real"))
            return process_char(0, char, '', tokens)
    elif state == 5:
        if char.isdigit():
            return 4, lexeme + char
        else:
            tokens.append((lexeme, "Real"))
            return process_char(0, char, '', tokens)
    elif state == 6:
        if char.isdigit():
            return 4, lexeme + char
        else:
            tokens.append((lexeme, "Real"))
            return process_char(0, char, '', tokens)
    elif state == 7:
        if char.isdigit():
            return 2, lexeme + char
        elif char == '.':
            return 3, lexeme + char
        else:
            tokens.append((lexeme, "Resta"))
            return process_char(0, char, '', tokens)
    elif state == 8:
        if char == '\n':
            tokens.append((lexeme, "Comentario"))
            return 0, ''
        else:
            lexeme += char
            return 8, lexeme
    return state, lexeme

def token_type(char):
    if char == "=":
        return "Asignación"
    elif char == "+":
        return "Suma"
    elif char == "-":
        return "Resta"
    elif char == "*":
        return "Multiplicación"
    elif char == "/":
        return "División"
    elif char == "^":
        return "Potencia"

if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo: ")
    lexerAritmetico(archivo)