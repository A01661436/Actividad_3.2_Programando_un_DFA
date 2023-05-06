import re

def lexerAritmetico(archivo):
    # Expresiones regulares para reconocer los distintos tipos de tokens
    regex_real = r'[+-]?\d+\.\d*(?:[eE][+-]?\d+)?|[+-]?\d*(?:\.\d+)(?:[eE][+-]?\d+)?|[+-]?\d+[eE][+-]?\d+'
    regex_ent = r'[+-]?\d+'
    regex_op_asig = r'='
    regex_op_suma = r'\+'
    regex_op_resta = r'-'
    regex_op_mult = r'\*'
    regex_op_div = r'/'
    regex_op_pot = r'\^'
    regex_par_izq = r'\('
    regex_par_der = r'\)'
    regex_var = r'[a-zA-Z_]\w*'
    regex_com = r'#[^\n]*'


    # Tabla de tokens
    tokens = []

    # Abrir archivo de texto y analizar cada línea
    with open(archivo, 'r') as f:
        for linea in f:
            # Eliminar espacios en blanco y saltos de línea
            linea = linea.strip()

            # Buscar tokens en la línea
            while linea:
                # Reales
                match = re.match(regex_real, linea)
                if match:
                    tokens.append(('Real', match.group()))
                    linea = linea[len(match.group()):]
                    continue

                # Enteros
                match = re.match(regex_ent, linea)
                if match:
                    tokens.append(('Entero', match.group()))
                    linea = linea[len(match.group()):]
                    continue

                # Operadores de asignación
                match = re.match(regex_op_asig, linea)
                if match:
                    tokens.append(('Operador de Asignación', match.group()))
                    linea = linea[1:]
                    continue

                # Operadores de suma
                match = re.match(regex_op_suma, linea)
                if match:
                    tokens.append(('Operador de Suma', match.group()))
                    linea = linea[1:]
                    continue

                # Operadores de resta
                match = re.match(regex_op_resta, linea)
                if match:
                    tokens.append(('Operador de Resta', match.group()))
                    linea = linea[1:]
                    continue

                # Operadores de multiplicación
                match = re.match(regex_op_mult, linea)
                if match:
                    tokens.append(('Operador de Multiplicación', match.group()))
                    linea = linea[1:]
                    continue

                # Operadores de división
                match = re.match(regex_op_div, linea)
                if match:
                    tokens.append(('Operador de División', match.group()))
                    linea = linea[1:]
                    continue

                # Operadores de potencia
                match = re.match(regex_op_pot, linea)
                if match:
                    tokens.append(('Operador de Potencia', match.group()))
                    linea = linea[1:]
                    continue

                # Paréntesis que abre
                match = re.match(regex_par_izq, linea)
                if match:
                    tokens.append(('Paréntesis de Apertura', match.group()))
                    linea = linea[1:]
                    continue

                # Paréntesis que cierra
                match = re.match(regex_par_der, linea)
                if match:
                    tokens.append(('Paréntesis de Cierre', match.group()))
                    linea = linea[1:]
                    continue

                # Variables
                match = re.match(regex_var, linea)
                if match:
                    tokens.append(('Variable', match.group()))
                    linea = linea[len(match.group()):]
                    continue

                # Comentarios
                match = re.match(regex_com, linea)
                if match:
                    tokens.append(('Comentario', match.group()))
                    linea = ''
                    continue

                # Si no se reconoce el token, se ignora
                linea = linea[1:]

    # Imprimir tabla de tokens
    print('{:<25}{:<15}'.format('Token', 'Tipo'))
    for token in tokens:
        print('{:<25}{:<15}'.format(token[1], token[0]))

lexerAritmetico("ejemplo.txt")