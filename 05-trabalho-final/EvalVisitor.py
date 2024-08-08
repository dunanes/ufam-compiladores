'''
Representação Intermediária - Trabalho de Compiladores

Integrantes: 
Arthur Matias
Bianka Vasconcelos
Micael Viana
Daniel Nunes

Segue abaixo o Eval Visitor com a análise semântica e representação intermediária.
'''

from re import M
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser

class AddressOutput():
  def __init__(self):
    self.translation = ""
    self.count = 1
    self.if_count = 1 # controla o numero das labels
    self.while_count = 1
    self.while_start=1
    self.while_end=1
    self.symbols = ['*','/','%','+','-','<','>','<=','>=','==','!=','=','*=','/=','%=','+=','-=']

  def addDataDefinition(self,dataDef):
    variables = dataDef.split(",")
    text = variables[0]
    listSize = len(variables)
    if text.find("int") == 0:
      variables[0] = text[3:]
      lasVarSize = len(variables[listSize-1])
      variables[listSize-1] = variables[listSize-1][0:lasVarSize-1] 
      type = text[0:3]
    elif text.find("char") == 0:
      variables[0] = text[4:]
      lasVarSize = len(variables[listSize-1])
      variables[listSize-1] = variables[listSize-1][0:lasVarSize-1]
      type = text[0:4]      
   
    for var in variables:
      self.translation += type + " "
      self.translation += var
      self.translation += "\n"

  def openIf(self,lineVector:list,lineNum:int):
    finalVar = lineVector[0][1]
    #size = len(lineVector)
    
    
    pos1 = lineVector[2][1] 
    self.translation += "if " +  finalVar + " " + lineVector[1][1] + " " + pos1  + " goto L"+str(self.if_count) + "\n"
    self.if_count += 1
    self.translation += "goto L"+str(self.if_count) + "\n"  
    self.translation += "L"+str(self.if_count-1) + ":\n" 

  def closeIf(self,ehElse = False):
    if not ehElse:
      self.translation += "L" + str(self.if_count) + ":\n" 
    else:
      self.if_count +=1
      self.translation += "L" + str(self.if_count) + ":\n"



  def openWhile(self,lineVector:list,lineNum:int):
    finalVar = lineVector[0][1]
    #size = len(lineVector)
    
    
    pos1 = lineVector[2][1] 
    self.translation += "start"+ str(self.while_start) +":\n"+ "if " +  finalVar + " " + lineVector[1][1] + " " + pos1  + " goto E"+str(self.while_count) + "\n"
    self.while_count += 1
    self.translation += "goto E"+str(self.while_count) + "\n"  
    self.translation += "E"+str(self.while_count-1) + ":\n" 
  
  

  def closeWhile(self):
    self.translation += "goto start" +str(self.while_start) +"\n"
    self.translation += "E" + str(self.while_count) + ":\n" 

    self.while_start+=1

  def openFunction(self,funcName,funcParams):
    #print(funcName)
    # sabemos que é uma função
    # print('PARAMETROS DA FUNCAO: ', funcParams)
    self.translation += f"{funcName}("
    for parametro in funcParams:
      if parametro == funcParams[-1]:
        self.translation += f"{parametro} "
      else:
        self.translation += f"{parametro}, "
      
    
    self.translation += "){\n"



  def closeFunction(self):
    self.translation += "}\n\n"




  def openReturn(self, myLine:list, finalVar:str, size:int):
    if size > 3:#a + b + c + d, return a+b


      for operando in range(1,size,2):
        pos1 = myLine[operando-1][1] # a
        pos2 = myLine[operando][1] # +
        pos3 = myLine[operando+1][1] # b
        
        if operando == 1:
          self.translation += f"T{self.count} = {pos1} {pos2} {pos3}\n"
          
        elif operando < size:
          self.translation += f"T{self.count} = T{self.count} {pos2} {pos3}\n"
      self.translation += f"return T{self.count} \n"

    elif size == 3:    #a=b, return a+b 
      
      pos1 = myLine[0][1]
      pos2 = myLine[1][1]
      pos3 = myLine[2][1]
     
      self.translation += f"return {pos1} {pos2} {pos3}\n"
    else:
      pos1 = myLine[0][1]
      self.translation += f"return {pos1}\n"
    self.count += 1   


  def manipulationString(self,myLine:list):
    print("Linha atual=",myLine[0][0])
    copia_simbolos = self.symbols.copy()
    #copia_simbolos.reverse() #invertir
    # print("self.symbols invertidos=",copia_simbolos)
    minhaLinha=[]
    numeroLinha=myLine[0][0]
    for i in myLine:
      minhaLinha.append(i[1])

    # print("Manipulacao",minhaLinha)

    #if(a > y),return b
    precedencia=[]
    if len(minhaLinha) <=5:
      print("---Minha nova linha=",minhaLinha)
      print(list(enumerate(minhaLinha)))
      precedencia=minhaLinha
      print('********finally=',precedencia)
      for i in range(len(precedencia)):
        precedencia[i]=(numeroLinha,precedencia[i])
      return precedencia


    #remover os simbolos que dao trabalho para precedencia
    copia_simbolos.remove('=')
    copia_simbolos.remove('*=')
    copia_simbolos.remove('/=')
    copia_simbolos.remove('%=')
    copia_simbolos.remove('+=')
    copia_simbolos.remove('-=')
    quantidadeSimbolosTerminaisUnicos=0
    for i in minhaLinha:
      if i in copia_simbolos:
        quantidadeSimbolosTerminaisUnicos+=1


    lista_pos_maiores=[]

    for k in range(quantidadeSimbolosTerminaisUnicos):
      maior=-1
      pos_maior=0

      #encontrar o maior
      for pos,char in enumerate(minhaLinha): 
        if char in copia_simbolos:
          valor_caractere=copia_simbolos.index(char)
          if valor_caractere > maior and pos not in lista_pos_maiores:
            maior=valor_caractere
            pos_maior=pos

      #colocar parenteses na esquerda da esquerda
      #colocar parenteses na direita da direita
      esquerda=minhaLinha[pos_maior-1]
      direita=minhaLinha[pos_maior+1]
      #if '(' not in esquerda and ')' not in esquerda:
      if esquerda.find('(') == -1 and esquerda.find(')') == -1 and direita.find('(') == -1 and direita.find(')') == -1: #nao tem parenteses
        minhaLinha[pos_maior-1] = '(' + minhaLinha[pos_maior-1]
        minhaLinha[pos_maior+1] = minhaLinha[pos_maior+1] + ')'
      
      lista_pos_maiores.append(pos_maior)

      print(f"Maior da linha {copia_simbolos[maior]} e posicao {pos_maior}")

    # print("---Minha nova linha=",minhaLinha)
    print("---Minha nova linha=",minhaLinha)
    print(list(enumerate(minhaLinha)))
    print("vetor com precedencia")

    precedencia=[]
    tamanhoMinhaLinha=len(minhaLinha)
    i=0
    while(i < tamanhoMinhaLinha):
      atual=minhaLinha[i]
      print('atual = ',atual)
      #caso especial, abriu o parentese e nao fechou, achou o parentese que abre, mas nao achou o que fecha entao concatena duas strings a frente
      if atual.find('(') != -1 and atual.find(')') == -1:
        atual = minhaLinha[i] + minhaLinha[i+1] + minhaLinha[i+2]
        i+=3
      else:
        i+=1
      
      precedencia.append(atual)

    print('********finally=',precedencia)
    print()
    print()
    #isso retorna um vetor,talvez a melhor saida pra nao mexer com o  resto do codigo seja alguem transformar isso em uma tupla
    for i in range(len(precedencia)):
      precedencia[i]=(numeroLinha,precedencia[i])
    return precedencia





  def addBinary(self,lineVector:list,lineNum:int,ehIf=False,ehWhile=False, ehReturn=False):
    myLine = []
    for item in lineVector:
      if item[0] == lineNum:
        myLine.append(item)
    finalVar = myLine[0][1]
    size = len(myLine)

    especiais=['*=',"+=",'-=','%=','/=']

    #myLine=self.manipulationString(myLine)
    # d = 2 + a * b + c/5
    #d = a * b + c/5 + 2
    if not ehIf and not ehWhile and not ehReturn: 
      if size > 5:
        if myLine[1][1] not in especiais: #senao eh atribuicao especial
          for operando in range(3,size,2):
            pos1 = myLine[operando-1][1]
            pos2 = myLine[operando][1]
            pos3 = myLine[operando+1][1]
            
            if operando == 3:    
              self.translation += 'T' + str(self.count) +" " +'=' + " " + pos1 + " " + pos2 + " " + pos3 + "\n"
              self.count += 1
            elif operando + 2 < size:
              self.translation += 'T' + str(self.count)+ " " +'=' + " " + 'T' + str(self.count-1)+ " " + pos2 + " " + pos3 + "\n"
              self.count += 1
            else:
              self.translation += finalVar+ " " + myLine[1][1] + " " + 'T' + str(self.count-1)+ " " + pos2 + " " + pos3 + "\n"
        else:
           for operando in range(3,size,2):
            pos1 = myLine[operando-1][1]
            pos2 = myLine[operando][1]
            pos3 = myLine[operando+1][1]
            
            if operando == 3:    
              self.translation += 'T' + str(self.count) +" " +'=' + " " + pos1 + " " + pos2 + " " + pos3 + "\n"
              self.count += 1
            elif operando + 2 < size:
              self.translation += 'T' + str(self.count)+ " " +'=' + " " + 'T' + str(self.count-1)+ " " + pos2 + " " + pos3 + "\n"
              self.count += 1
            else:
              self.translation += 'T' + str(self.count)+ " " +'=' + " " + 'T' + str(self.count-1)+ " " + pos2 + " " + pos3 + "\n"
              self.count += 1
              operador_especial = myLine[1][1]
              operador_especial = operador_especial[0]
              self.translation += finalVar+ " " + "=" + " " + finalVar + " " + operador_especial + " " +'T'+ str(self.count-1) +"\n"
      elif size == 5:
        if myLine[1][1] not in especiais:     
          self.translation += finalVar
          pos1 = myLine[2][1]
          pos2 = myLine[3][1]
          pos3 = myLine[4][1]
          self.translation += " " + myLine[1][1]+ " " + pos1 + " " + pos2 + " " + pos3 + "\n"
        else:
          self.translation += 'T' + str(self.count) + " = "
          self.count += 1
          operador_especial = myLine[1][1]
          operador_especial = operador_especial[0]
          pos1 = myLine[2][1]
          pos2 = myLine[3][1]
          pos3 = myLine[4][1] 
          self.translation +=  pos1 + " " + pos2 + " " + pos3 + "\n"
          self.translation += f"{finalVar} = {finalVar} {operador_especial} T{self.count-1}\n"

      else: #b *= a, b = b * a
        self.translation += finalVar

        
        if myLine[1][1] in especiais:
          self.translation += ' ' + '=' + ' ' + finalVar + ' ' + myLine[1][1][0] + ' ' + myLine[2][1] + "\n"
          return

        try:
          pos1 = myLine[2][1] 
        except IndexError:
          print(f"Error: Not enough elements in line: {myLine}")
        self.translation += " " + myLine[1][1]+ " " + pos1 + "\n"
    elif ehIf:
      self.openIf(myLine,lineNum)
    elif ehWhile:
      self.openWhile(myLine, lineNum)    # colocar openWhile
    
    elif ehReturn:
      self.openReturn(myLine, finalVar, size)


class EvalVisitor(MiniCVisitor):

  def __init__(self):
    self.symbol_table = {} #variaveis e seus escopos
    self.function_names={} #nome de funcoes e tipos de funcoes
    self.linhas = {} # dicionário para salvar a informação das linhas do código
    self.function_args = {} # nome e argumentos de uma função
    self.contador=0
    self.erros = []
    self.escope = "global"
    self.unarios = [] # vetor para armazenar os unários
    self.translator = AddressOutput()
    self.binaryControler = 0
    self.symbols = ['*','/','%','+','-','<','>','<=','>=','==','!=','=','*=','/=','%=','+=','-=']
  def avaliacaoExpressao(self, numero_linha,tipo1,conteudo):
      #(5/2+f(n)-c)
    for item in conteudo:
        if item in self.symbols: continue

        #FUNCAO
        tipo2=None
        nome_intermediario=item
        index_parenteses=nome_intermediario.find('(')

  
  def avaliacaoFuncao(self,numero_linha:int,chamada_da_funcao:str):
    # 'factorial(n,2,dec,'2'))'
    #chamada
    eh_mesmo_tamanho = False
    nome_funcao = chamada_da_funcao.split('(')[0]

    lista_argumentos = chamada_da_funcao.split('(')[1]
    numero_de_argumentos_chamada=0

    if len(lista_argumentos) > 1: #significa que tem algo dentro dos parenteses
      numero_de_argumentos_chamada=chamada_da_funcao.count(',')+1

    #print("Numero de argumentos da chamada",numero_de_argumentos_chamada)


    #declaracao
    tipos_original = self.function_args[nome_funcao] # pega os tipos que devem estar nos argumentos
    numero_de_argumentos_declaracao=len(tipos_original)

    #erros
    #quantidade de argumentos
    if numero_de_argumentos_chamada != numero_de_argumentos_declaracao:
      self.add_error_alt(f"Expected '{numero_de_argumentos_declaracao}' args but received '{numero_de_argumentos_chamada}' in the '{nome_funcao}' function",numero_linha)
    else:
      eh_mesmo_tamanho = True
      
    #argumentos = chamada_da_funcao.split('(')[1].split(')') # argumentos passados para a função quando foi chamada
    primeiro_parentese=chamada_da_funcao.find('(')
    ultimo_parentese = chamada_da_funcao.rfind(')')

    argumentos=''
    for i in range(primeiro_parentese+1,ultimo_parentese):
      argumentos += chamada_da_funcao[i]      

    argumentos = argumentos.split(',')
  
    args_individuais = [a.strip() for arg in argumentos for a in arg.split(',')]


    if eh_mesmo_tamanho and len(tipos_original) > 0:
      for i in range(len(args_individuais)):

        tipo2 = None
        #FUNCAO
        nome_intermediario=args_individuais[i]
        #print('nome intermediario: ', nome_intermediario)
        #operadores = "+-*/%"
        achei_simbolo=False
        for char in self.symbols:
          #print('char=',char)
          if char in nome_intermediario:
            achei_simbolo = True
            break
        if achei_simbolo:
          continue
        
        index_parenteses=nome_intermediario.find('(')

        eh_funcao=False
        #ele existe mas nao  eh o primeiro
        if index_parenteses > 0:
#          print("Detectou que eh funcao")
          eh_funcao=True
        elif index_parenteses == 0:
          continue

        nome2=nome_intermediario.split('(')[0]
#        print("NOME2: ",nome2)

        if eh_funcao and nome2 not in self.function_names:
          self.add_error_alt(f"Error function '{nome2}' not declared",numero_linha)
          continue
        elif eh_funcao and nome2 in self.function_names:
          tipo2=self.function_names[nome2]
          # sei que é uma função declarada, agora vamos verificar a lista de args
          #print("CASO RECURSIVO",nome_intermediario)
          #self.avaliacaoFuncao(numero_linha,nome_intermediario)


        #LITERAL
        if nome2.isdigit():
          tipo2 = 'int'
        elif len(nome2) == 3 and nome2[0] == "'" and nome2[2] == "'" and ord(nome2[1]) <=127:
          tipo2 = 'char'

        
        #variavel
        variableExists=False
        for key in self.symbol_table:
          if nome2 in self.symbol_table[key]:
            variableExists = True
            break
        #print("Esse é o nome2 : ", nome2)
        #print(type(nome2))
        #print(len(nome2))
        
        if not variableExists and tipo2 is None and len(lista_argumentos)>1: #consertar para nome2 nao vazio  nao cair em variavel nao declarada
          self.add_error_alt(f"Error variable a aaa '{nome2}' not declared.", numero_linha)
          continue
      
        


        
        for escopos in self.symbol_table:
          for vars in self.symbol_table[escopos]:
            if nome2 ==  vars:
              tipo2 = self.symbol_table[escopos][vars]
          

        # ultima coisa
        # print(f'Esse é o i {i}, e esse é o i+1 {i+1}')
        #print("antes do erro")
        #print('tipos original i: ', tipos_original[i])
        if tipo2 != tipos_original[i]:
          self.add_error_alt(f"Expected type '{tipos_original[i]}' but received '{tipo2}' in position {i+1} in function '{nome_funcao}'", numero_linha)



  def avaliacaoLinhaInteira(self,dicio) :
    # percorrer dict e analisar cada elemento do vetor
    for numero_linha, conteudo in dicio.items():

      #ESQUERDA

      #----funcao
      tipo1=None
      nome_intermediario=conteudo[0]
      index_parenteses=nome_intermediario.find('(')

      eh_funcao=False

      if index_parenteses>0:
        eh_funcao=True
      elif index_parenteses==0:
        self.avaliacaoExpressao(numero_linha,)
        #nao posso avaliar, esse return depende do tipo da funcao em que ele encontra
        continue


      nome1=nome_intermediario.split('(')[0]
       
      if  eh_funcao and nome1 not in self.function_names:
        self.add_error_alt(f"Error function '{nome1}' not declared", numero_linha)
      elif eh_funcao and nome1 in self.function_names:
        tipo1=self.function_names[nome1]
        self.avaliacaoFuncao(numero_linha,conteudo[0])


      #--literal
      if nome1.isdigit():
        tipo1='int'
      elif len(nome1) == 3 and nome1[0] == "'" and nome1[2] == "'" and ord(nome1[1]) <=127:
        tipo1='char'

    
      # --- Variavel ---
      if not eh_funcao:

        variableExists=False
        for key in self.symbol_table:
          if nome1 in self.symbol_table[key]:
            variableExists=True
            break
        if not variableExists and tipo1 is None:
          self.add_error_alt(f"Error variable '{nome1} not declared'",numero_linha)

        for escopos in self.symbol_table:
          for vars in self.symbol_table[escopos]:
            if nome1 == vars:
              tipo1 = self.symbol_table[escopos][vars]


      #DIREITA
      #pula se for o primeiro ou se for simbolo terminal
      for item in conteudo:
        # vamos analisar os itens do vetor
        # Verificando o identificador da direita
        
        if item == nome1: continue
        if item in self.symbols: continue
        
        # --- Função ---
        tipo2=None
        nome_intermediario=item
        index_parenteses=nome_intermediario.find('(')

        eh_funcao=False
        #ele existe mas nao  eh o primeiro
        if index_parenteses > 0:
          eh_funcao=True
        elif index_parenteses == 0:
          self.avaliacaoExpressao(numero_linha,tipo1,nome_intermediario)
          continue

        nome2=nome_intermediario.split('(')[0]

        if eh_funcao and nome2 not in self.function_names:
          self.add_error_alt(f"Error function '{nome2}' not declared",numero_linha)
          continue
        elif eh_funcao and nome2 in self.function_names:
          tipo2=self.function_names[nome2]
          # sei que é uma função declarada, agora vamos verificar a lista de args
          self.avaliacaoFuncao(numero_linha,item)
          

       # print("Nome2=",nome2)

        # --- Literal ---
        if nome2.isdigit():
          tipo2='int'
        elif len(nome2) == 3 and nome2[0] == "'" and nome2[2] == "'" and ord(nome2[1]) <=127:
          tipo2='char'

        # --- Variavel ---
        variableExists=False
        for key in self.symbol_table:
          if nome2 in self.symbol_table[key]:
            variableExists=True
            break
        if not variableExists and tipo2 is None:
          self.add_error_alt(f"Error variable '{nome2} not declared'",numero_linha)
          continue

        for escopos in self.symbol_table:
          for vars in self.symbol_table[escopos]:
            if nome2 == vars:
              tipo2 = self.symbol_table[escopos][vars]

        #print(f"Tipo 1: {tipo1} e Tipo 2: {tipo2}\n")

        if tipo1 is not None and tipo2 is not None and tipo1 != tipo2:
          self.add_error_alt(f"Error incompatible types '{tipo1}' and '{tipo2}'",numero_linha)
        elif tipo2 is None:
          self.add_error_alt(f"Error unknow expression",numero_linha)


  # processamento dos unários
  def __del__(self):
    #print("Sera=?",self.unarios) # na esquerda a linha, na direita o conteudo
    dicio = {}

    for chave, valor in self.unarios:
      if chave not in dicio:
        dicio[chave] = []
      dicio[chave].append(valor)

#    print('DICIO', dicio)

    self.avaliacaoLinhaInteira(dicio)

    if self.erros:
      print("Semantic Errors:")
      for k in self.erros:
        print(k)
        return
    else:
      print("No semantic errors")
      print(self.translator.translation)

      with open('./output/tac.txt', 'w') as file:
        file.write(self.translator.translation)
      print("Gravado no arquivo output/tac.txt")
        
      

      
      

    # print(self.symbol_table)


  def visitProgram(self, ctx: MiniCParser.ProgramContext):
    self.symbol_table[self.escope] = {}
    result = super().visitProgram(ctx)
    return result


  def add_error(self, message, ctx):
    line = ctx.start.line
    self.erros.append(f"Line {line}: {message} ")

  def add_error_alt(self, message, line):
    self.erros.append(f"Line {line}: {message} ")
    

      
  def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext):
    lista_argumentos = []
    # aqui seleciona o nome da funcao
    self.escope = ctx.parentCtx.getChild(1).getChild(0).getText() # nome da função
    nome = self.escope
    paramList = [ ]
    #print("FUNCAO NOME: ", self.escope)
    parameters = ctx.parentCtx.getChild(1).getChild(1).getChild(1)
    self.symbol_table[self.escope] = {}

    if parameters.getText() != ")":
      l = list(parameters.getChildren())
      size = len(l)
      for index in range(0,size,3):
        var_type = l[index].getText()
        var_name = l[index+1].getText()
        paramList.append(f"{var_type} {var_name}")
        lista_argumentos.append(var_type)

        if var_name in self.symbol_table[self.escope]:
          self.add_error(f" Error variable '{var_name}' already declared.", ctx.parentCtx.getChild(1))
        else:  
          self.symbol_table[self.escope][var_name] = var_type
          
    self.function_args[self.escope] = lista_argumentos # salvando a lista de tipo dos argumentos e o nome da função
    self.translator.openFunction(nome,paramList)
    super().visitFunction_body(ctx)
    self.translator.closeFunction()
    
  

  def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
    lista=list(ctx.getChildren())
    # print("Posicoes")
    # print([(i,j.getText()) for i,j in enumerate(lista)])
    tipo_funcao = ctx.getChild(0).getText()
    #'factorial(intn)'
    nome_funcao = ctx.getChild(1).getText().split('(')[0]

    if nome_funcao in self.symbol_table:
      self.add_error(f"Error function '{nome_funcao}' already declared.", ctx)
    else:
      self.function_names[nome_funcao] = tipo_funcao
    return self.visitChildren(ctx)

  def visitFunction_header(self, ctx: MiniCParser.Function_headerContext):
    return self.visitChildren(ctx)
  
  
  # Verificar declaração de variáveis
  def visitData_definition(self, ctx: MiniCParser.Data_definitionContext):
    l = list(ctx.getChildren())
    tipo = l[0].getText()
    if (str(ctx.parentCtx.parentCtx.__class__.__name__) == "ProgramContext"):  # verifica se está no escopo global
      for i in range(1, len(l), 2):
        nome = l[i].getText()
        if nome in self.symbol_table["global"]:
          self.add_error(f"Error variable '{nome}' already declared.", ctx)
        else:
          self.symbol_table["global"][nome] = tipo
    else:
      for i in range(1, len(l), 2):
        nome = l[i].getText()
        if nome in self.symbol_table[self.escope]:
          self.add_error(f"Error variable '{nome}' already declared.", ctx)
        else:
          self.symbol_table[self.escope][nome] = tipo
    text = ctx.getText()
    self.translator.addDataDefinition(text)
    return self.visitChildren(ctx)
  
  # Verificar compatibilidade dos tipos nas expressões

  def visitBinary(self, ctx: MiniCParser.BinaryContext):
    l = list(ctx.getChildren())
    # print([i.getText() for i in l])
    # print('Contexto: ', str(ctx.__class__.__name__))
    for i in range(len(l)):
      self.binaryControler += 1
      if str(l[i].__class__.__name__) == "BinaryContext" and l[i].getChildCount() > 1:
        # print("Expressão Binária: ")
        l2 = l[i]
#        print(l2.getText())
        self.visit(l2)
        
      else:
        # print('Expressão Unária: ')
        l2 = l[i]
        # print(l2.getText())
        self.unarios.append((ctx.start.line,l2.getText())) # o vetor tem tuplas com a informação da linha
      self.binaryControler -= 1
    if self.binaryControler == 0:
      copia= self.unarios.copy()
      #print("O filho :",ctx.parentCtx.parentCtx.getChild(0).getText())
      if ctx.parentCtx.parentCtx.getChild(0).getText() == 'if':
        self.translator.addBinary(copia,ctx.start.line,ehIf=True) 
      elif ctx.parentCtx.parentCtx.getChild(0).getText() == 'while':
        self.translator.addBinary(copia,ctx.start.line,ehIf=False,ehWhile=True) 
      elif ctx.parentCtx.parentCtx.getChild(0).getText() == 'return': #so trata return que tem direita
        # print('Tem algo na direita do return')
        self.translator.addBinary(copia,ctx.start.line,ehReturn=True)
      else:
        self.translator.addBinary(copia,ctx.start.line)
      # return alguma ;
  def visitStatement(self, ctx: MiniCParser.StatementContext):
    l = list(ctx.getChildren())
    
    # for i,j in enumerate(l):
    #   print(i,j.getText())

    if l[0].getText() == 'while':

      #print("É whileeeeeeeeeeeee")

      #print('l2: ', l[2].getText())
      self.visit(l[2])
      #print('l4: ', l[4].getText())
      self.visit(l[4])



      # self.translator.while_count += 1

      # start_label = "E" + str(self.translator.while_count) # label inicio
      # end_label = "E" + str(self.translator.while_count+1)

      # self.translator.translation += start_label + ":\n"

 

      self.translator.closeWhile()  

      #print("Cheguei")e

    elif l[0].getText() == 'if':
      self.visit(l[2])
      self.visit(l[4])
      
      if len(l) > 5:  # verificar se a lista tem pelo menos 6 elementos
        if l[5] is not None:
          if l[5].getText() == 'else':
              self.translator.translation += "goto L" + str(self.translator.if_count + 1) + "\n"
              self.translator.translation += "L" + str(self.translator.if_count) + ":\n"
              self.visit(l[6])
              self.translator.closeIf(ehElse=True)
      else:
        self.translator.closeIf(ehElse=False)

    elif l[0].getText() == 'return' and len(l) < 3:
      self.translator.translation += 'return' + '\n'
    elif l[0].getText() == 'break':
      self.translator.translation += 'break' + '\n'
    elif l[0].getText() == 'continue':
      self.translator.translation += 'continue' + '\n'
    else:
      return self.visitChildren(ctx)

   

  

 
  
