'''
Integrantes: 
Arthur Matias
Bianka Vasconcelos
Micael Viana
Daniel Nunes
'''

import sys
import re

# traduzido = ""
# True pode usar, False não pode usar

traduzido = ""


registradores = {"$zero": True, "$at": True, "$v0": True, "$v1": True, "$a0": True, 
                 "$a1": True, "$a2": True, "$a3": True, "$t0": True, "$t1": True,
                 "$t2": True, "$t3": True, "$t4": True, "$t5": True, "$t6": True, 
                 "$t7": True, "$s0": True, "$s1": True, "$s2": True, "$s3": True, 
                 "$s4": True, "$s5": True, "$s6": True, "$s7": True, "$t8": True, 
                 "$t9": True, "$k0": True, "$k1": True, "$gp":True, "$sp": True,
                 "$fp": True, "$ra": True, "HI": True, "LO": True}

def translate_line(line, instruction_type):
    match(instruction_type):
        case "atribuicao":
            return (translate_att(line))
        case "aritmetica":
            return (translate_arithmetic(line))
        case "if":
            return (translate_if(line))
        case "goto":
            return(translate_goto(line))
        case "label":
            return(translate_label(line))

def decide_instruction(line):
    
    # decide o que a linha representa
    type_of_operation = ""
    linha = line.strip()

    # Caso: If
    if linha.startswith("if"):
        type_of_operation = "if"
    
    # Caso: GOTO
    elif linha.startswith("goto"):
        type_of_operation = "goto"

    # Caso: Label    
    elif linha.endswith(":"):
        type_of_operation = "label"

    # Caso: Aritmética
    elif any(op in linha for op in ['+', '-', '*', '/', '%']):
        type_of_operation = "aritmetica"
    
    # Caso: Atribuição
    elif linha.find("=") != -1:
        type_of_operation = "atribuicao"

    # Retorna o tipo de operação
    return type_of_operation


def translate_att(line):
    global traduzido
    # aqui vamos traduzir o att
    #faz un for de t0 a t6

    for i in range(0,8):
        key = f"$t{i}"
        # Ocupar o reg
        if registradores[key] == True:
            registradores[key] = False     
            break
    
    quebrada = line.split("=")
    var = quebrada[0].strip()
    value = quebrada[1].split("\n")[0]
    traduzido += f"addi {key}, $zero, {value}\n"
    traduzido += f"sw {key}, {var}($zero)\n"
    # Liberar o reg
    registradores[key] = True

    return 1


def translate_arithmetic(line):
    global traduzido

    operadores = {
        '+': 'add',
        '-': 'sub',
        '*': 'mult',
        '/': 'div',
        '%': 'div' # Mod também usa div, só pega o resultado no outro registrador.
    }

    # Encontrar um registrador (?)
    for i in range(0, 8):
        key1 = f"$t{i}"
        if registradores[key1] == True:
            registradores[key1] = False
            break

    # Encontrar outro registrador (i+1 pra evitar o mesmo)
    for j in range(0, 8):
        key2 = f"$t{j}"
        if registradores[key2] == True:
            registradores[key2] = False
            break

    # Dividir variável e resto da expressão
    quebrada = line.split("=")
    var = quebrada[0].strip()
    expr = quebrada[1].strip()

    for op in operadores.keys():
        if op in expr:
            esquerda, direita = expr.split(op)
            esquerda = esquerda.strip()
            direita = direita.strip()

            if esquerda.isdigit():
                traduzido += f"addi {key1}, $zero, {esquerda}\n"
            else:
                traduzido += f"lw {key1}, {esquerda}($zero)\n"

            if direita.isdigit():
                traduzido += f"addi {key2}, $zero, {direita}\n"
            else:
                traduzido += f"lw {key2}, {direita}($zero)\n"

            # Executar a operação
            if op in ['*', '/']:
                traduzido += f"{operadores[op]} {key1}, {key2}\n"
                if op == '/':
                    traduzido += f"mflo {key1}\n"
            elif op == '%':
                # Para a operação de módulo
                traduzido += f"{operadores[op]} {key1}, {key2}\n"
                traduzido += f"mfhi {key1}\n"
            else:
                traduzido += f"{operadores[op]} {key1}, {key1}, {key2}\n"

            traduzido += f"sw {key1}, {var}($zero)\n"
            break

    # Liberar os regs
    registradores[key1] = True
    registradores[key2] = True

    return 1

def translate_if(line):
    global traduzido
    
    operadores = {
        '>=': 'bge',
        '<=': 'ble',
        '==': 'beq',
        '<': 'blt',
        '>': 'bgt',
        '!=': 'bne',
    }

    # Encontrar registradores disponíveis
    for i in range(0, 8):
        key1 = f"$t{i}"
        if registradores[key1]:
            registradores[key1] = False
            break

    for j in range(0, 8):
        key2 = f"$t{j}"
        if registradores[key2]:
            registradores[key2] = False
            break

    # Dividir variável e resto da expressão
    quebrada = line.split()
    esquerda = quebrada[1]
    condicao = quebrada[2]
    direita = quebrada[3]
    label = quebrada[-1]

    print(esquerda, condicao, direita, label)

    if esquerda.isdigit():
        traduzido += f"addi {key1}, $zero, {esquerda}\n"
    else:
        traduzido += f"lw {key1}, {esquerda}($zero)\n"

    if direita.isdigit():
        traduzido += f"addi {key2}, $zero, {direita}\n"
    else:
        traduzido += f"lw {key2}, {direita}($zero)\n"

    if condicao == '>=':
        traduzido += f"slt {key1}, {key1}, {key2}\n"
        traduzido += f"beq {key1}, $zero, {label}\n"
    elif condicao == '<=':
        traduzido += f"slt {key1}, {key2}, {key1}\n"
        traduzido += f"beq {key1}, $zero, {label}\n"
    elif condicao == '<':
        traduzido += f"slt {key1}, {key1}, {key2}\n"
        traduzido += f"bne {key1}, $zero, {label}\n"
    elif condicao == '>':
        traduzido += f"slt {key1}, {key2}, {key1}\n"
        traduzido += f"bne {key1}, $zero, {label}\n"
    else:
        traduzido += f"{operadores[condicao]} {key1}, {key2}, {label}\n"

    # Liberar os regs
    registradores[key1] = True
    registradores[key2] = True

    return 1

def translate_goto(line):
    global traduzido
    quebrada = line.split()
    label = quebrada[1]
    traduzido += f"j {label}\n"

def translate_label(line):
    global traduzido
    traduzido += f"{line}"
    return 1

def tres_enderecos_var_para_mips(cod_3_enderecos):
    global traduzido
    traduzido += ".data\n"
    with open(cod_3_enderecos, 'r') as file:
        data = file.readlines()
        
        # print('Data: ', data)
        for line in data:
            line_without_spaces = [word for word in line.split()]
            if line_without_spaces != []:

                #print('Linha atual: ', line_without_spaces)
                if line_without_spaces[0].find("int") == 0 or line_without_spaces[0].find('char') == 0:
                    if line_without_spaces[0] == 'int':
                        traduzido += f"{line_without_spaces[1]}: .space 4\n"
                    elif line_without_spaces[0] == 'char':
                        traduzido += f"{line_without_spaces[1]}: .space 1\n"
                
                
                if line_without_spaces[0].find("T") == 0:
                        var_control_num = line_without_spaces[0][1:]
                        if var_control_num.isdigit():
                            print(var_control_num)
                            traduzido += f"{line_without_spaces[0]}: .space 4\n"
    traduzido += ".text\n"

    return traduzido
    
def tres_enderecos_funcao_para_mips(cod_3_enderecos):
    funcoes_achadas = []
    # print("Estou dentro da função")

    with open(cod_3_enderecos, 'r') as file:
        data = file.readlines()
        
        # regex que acha funções
        regex_funcao = re.compile(r'\w+\s*\([^)]*\)\s*\{', re.DOTALL)   # \w+: acha um ou mais caracteres antes do parentese (nome da funcao)
                                                                        # \s*: pode ter 0 ou mais espaços em branco
                                                                        # \(: busca por um parentese abrindo
                                                                        # [^)]*: busca qualquer caractere menos o parentese fechando (parametros)
                                                                        # \): busca pelo parentese fechando (fim dos parametros da funcao)
                                                                        # \s*: zero ou mais espaços brancos depois do parentese 
                                                                        # \{: procura uma chave abrindo, que será o inicio do código da funcao 
        
        for line in data:
            match = regex_funcao.search(line) # procura pelo regex na string
            if match:
                # print(f"achei a função: {line.strip()}")
                funcoes_achadas.append(line.split("(")[0]) # pega o nome da função
    return funcoes_achadas

def traduz(funcoes_achadas):
    # fazer um tupla que relaciona a função com conteudo
    #ler o arquivo
    global traduzido
    with open(cod_3_enderecos, 'r') as file:
        data = file.readlines()
        for line in data:
            item = line.split("(")[0]
            # print(f"Item {item}")
            if item in funcoes_achadas:
                # print(f"O item {item} é função")
                traduzido += f"{item}:\n"
            elif line[0] == "}":
               None
            else:
                # traduzir o conteúdo de line
                # traduzido += line # linha direto por enquanto
                # verificar o que fazer com essa linha (o que ela é)
                instruction = decide_instruction(line)
                translate_line(line,instruction)
        traduzido += "\nSYSCALL 0"

    
    return traduzido

            
    # if nome_inicio da linha in funcoes_achadas
        #adiciona o incio da funcao traduzida
    # else if linha == "}"
        #adiciona o fin da funcao em mips


def faz_traducao_mips(cod_3_enderecos):
    global traduzido
    traduzido = ""
    # procurando funções...
    funcoes_achadas = tres_enderecos_funcao_para_mips(cod_3_enderecos)
    # print("Achei essas funções: ", funcoes_achadas)
    # procurando declarações de variáveis...
    tres_enderecos_var_para_mips(cod_3_enderecos)
    traduz(funcoes_achadas)

    return traduzido
# (inicio_linha, fim_linha, conteudo_linha)
# criaria arquivo vazio e inseriria no arquivo vazio de acordo com os numeros da tripla



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py nome_do_arquivo")
        sys.exit(1)

    # Obtém o nome do arquivo a partir dos argumentos da linha de comando
    cod_3_enderecos = sys.argv[1]

    # Lê o conteúdo do arquivo
    try:
        with open(cod_3_enderecos, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Arquivo '{cod_3_enderecos}' não encontrado.")
        sys.exit(1)

    traducao = faz_traducao_mips(cod_3_enderecos)
    print(traducao)
    print()


    with open('./output/mips.txt', 'w') as file:
        file.write(traducao)
    print("Gravado no arquivo output/mips.txt")
    






# print(nome_arquivo)
# funcoes = tres_enderecos_funcao_para_mips(nome_arquivo)
# a = tres_enderecos_var_para_mips(traduzido, nome_arquivo)
# print(a)
# print(funcoes)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # verificar se tem parentese para identificar uma função
