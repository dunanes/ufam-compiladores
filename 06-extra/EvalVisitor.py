from re import M
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser

class AddressOutput():
  def __init__(self):
    self.translation = ""
    self.count = 1
    self.if_count = 1
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
    if size > 3:
      for operando in range(1,size,2):
        pos1 = myLine[operando-1][1]
        pos2 = myLine[operando][1]
        pos3 = myLine[operando+1][1]
        
        if operando == 1:
          self.translation += f"T{self.count} = {pos1} {pos2} {pos3}\n"
          
        elif operando < size:
          self.translation += f"T{self.count} = T{self.count} {pos2} {pos3}\n"
      self.translation += f"return T{self.count} \n"

    elif size == 3:
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
    minhaLinha=[]
    numeroLinha=myLine[0][0]
    for i in myLine:
      minhaLinha.append(i[1])
    precedencia=[]
    if len(minhaLinha) <=5:
      print("---Minha nova linha=",minhaLinha)
      print(list(enumerate(minhaLinha)))
      precedencia=minhaLinha
      print('********finally=',precedencia)
      for i in range(len(precedencia)):
        precedencia[i]=(numeroLinha,precedencia[i])
      return precedencia

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
      for pos,char in enumerate(minhaLinha): 
        if char in copia_simbolos:
          valor_caractere=copia_simbolos.index(char)
          if valor_caractere > maior and pos not in lista_pos_maiores:
            maior=valor_caractere
            pos_maior=pos
      esquerda=minhaLinha[pos_maior-1]
      direita=minhaLinha[pos_maior+1]
      if esquerda.find('(') == -1 and esquerda.find(')') == -1 and direita.find('(') == -1 and direita.find(')') == -1: #nao tem parenteses
        minhaLinha[pos_maior-1] = '(' + minhaLinha[pos_maior-1]
        minhaLinha[pos_maior+1] = minhaLinha[pos_maior+1] + ')'
      
      lista_pos_maiores.append(pos_maior)

      print(f"Maior da linha {copia_simbolos[maior]} e posicao {pos_maior}")

    print("---Minha nova linha=",minhaLinha)
    print(list(enumerate(minhaLinha)))
    print("vetor com precedencia")

    precedencia=[]
    tamanhoMinhaLinha=len(minhaLinha)
    i=0
    while(i < tamanhoMinhaLinha):
      atual=minhaLinha[i]
      print('atual = ',atual)
      if atual.find('(') != -1 and atual.find(')') == -1:
        atual = minhaLinha[i] + minhaLinha[i+1] + minhaLinha[i+2]
        i+=3
      else:
        i+=1
      
      precedencia.append(atual)

    print('********finally=',precedencia)
    print()
    print()
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

    if not ehIf and not ehWhile and not ehReturn: 
      if size > 5:
        if myLine[1][1] not in especiais:
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
      self.openWhile(myLine, lineNum)
    
    elif ehReturn:
      self.openReturn(myLine, finalVar, size)


class EvalVisitor(MiniCVisitor):

  def __init__(self):
    self.symbol_table = {}
    self.function_names={}
    self.linhas = {}
    self.function_args = {}
    self.contador=0
    self.erros = []
    self.escope = "global"
    self.unarios = []
    self.translator = AddressOutput()
    self.binaryControler = 0
    self.symbols = ['*','/','%','+','-','<','>','<=','>=','==','!=','=','*=','/=','%=','+=','-=']
  def avaliacaoExpressao(self, numero_linha,tipo1,conteudo):
    for item in conteudo:
        if item in self.symbols: continue
        tipo2=None
        nome_intermediario=item
        index_parenteses=nome_intermediario.find('(')

  
  def avaliacaoFuncao(self,numero_linha:int,chamada_da_funcao:str):
    eh_mesmo_tamanho = False
    nome_funcao = chamada_da_funcao.split('(')[0]

    lista_argumentos = chamada_da_funcao.split('(')[1]
    numero_de_argumentos_chamada=0

    if len(lista_argumentos) > 1:
      numero_de_argumentos_chamada=chamada_da_funcao.count(',')+1

    tipos_original = self.function_args[nome_funcao]
    numero_de_argumentos_declaracao=len(tipos_original)

    if numero_de_argumentos_chamada != numero_de_argumentos_declaracao:
      self.add_error_alt(f"Expected '{numero_de_argumentos_declaracao}' args but received '{numero_de_argumentos_chamada}' in the '{nome_funcao}' function",numero_linha)
    else:
      eh_mesmo_tamanho = True
      
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
        nome_intermediario=args_individuais[i]
        achei_simbolo=False
        for char in self.symbols:
          if char in nome_intermediario:
            achei_simbolo = True
            break
        if achei_simbolo:
          continue
        
        index_parenteses=nome_intermediario.find('(')

        eh_funcao=False
        if index_parenteses > 0:
          eh_funcao=True
        elif index_parenteses == 0:
          continue

        nome2=nome_intermediario.split('(')[0]

        if eh_funcao and nome2 not in self.function_names:
          self.add_error_alt(f"Error function '{nome2}' not declared",numero_linha)
          continue
        elif eh_funcao and nome2 in self.function_names:
          tipo2=self.function_names[nome2]

        if nome2.isdigit():
          tipo2 = 'int'
        elif len(nome2) == 3 and nome2[0] == "'" and nome2[2] == "'" and ord(nome2[1]) <=127:
          tipo2 = 'char'

        
        variableExists=False
        for key in self.symbol_table:
          if nome2 in self.symbol_table[key]:
            variableExists = True
            break
        
        if not variableExists and tipo2 is None and len(lista_argumentos)>1: #consertar para nome2 nao vazio  nao cair em variavel nao declarada
          self.add_error_alt(f"Error variable a aaa '{nome2}' not declared.", numero_linha)
          continue
        
        for escopos in self.symbol_table:
          for vars in self.symbol_table[escopos]:
            if nome2 ==  vars:
              tipo2 = self.symbol_table[escopos][vars]
          
        if tipo2 != tipos_original[i]:
          self.add_error_alt(f"Expected type '{tipos_original[i]}' but received '{tipo2}' in position {i+1} in function '{nome_funcao}'", numero_linha)



  def avaliacaoLinhaInteira(self,dicio) :
    for numero_linha, conteudo in dicio.items():
      tipo1=None
      nome_intermediario=conteudo[0]
      index_parenteses=nome_intermediario.find('(')

      eh_funcao=False

      if index_parenteses>0:
        eh_funcao=True
      elif index_parenteses==0:
        self.avaliacaoExpressao(numero_linha,)
        continue

      nome1=nome_intermediario.split('(')[0]
       
      if  eh_funcao and nome1 not in self.function_names:
        self.add_error_alt(f"Error function '{nome1}' not declared", numero_linha)
      elif eh_funcao and nome1 in self.function_names:
        tipo1=self.function_names[nome1]
        self.avaliacaoFuncao(numero_linha,conteudo[0])

      if nome1.isdigit():
        tipo1='int'
      elif len(nome1) == 3 and nome1[0] == "'" and nome1[2] == "'" and ord(nome1[1]) <=127:
        tipo1='char'

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

      for item in conteudo:
        if item == nome1: continue
        if item in self.symbols: continue
        
        tipo2=None
        nome_intermediario=item
        index_parenteses=nome_intermediario.find('(')

        eh_funcao=False
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
          self.avaliacaoFuncao(numero_linha,item)

        if nome2.isdigit():
          tipo2='int'
        elif len(nome2) == 3 and nome2[0] == "'" and nome2[2] == "'" and ord(nome2[1]) <=127:
          tipo2='char'

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

        if tipo1 is not None and tipo2 is not None and tipo1 != tipo2:
          self.add_error_alt(f"Error incompatible types '{tipo1}' and '{tipo2}'",numero_linha)
        elif tipo2 is None:
          self.add_error_alt(f"Error unknow expression",numero_linha)

  def __del__(self):
    dicio = {}

    for chave, valor in self.unarios:
      if chave not in dicio:
        dicio[chave] = []
      dicio[chave].append(valor)

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
    self.escope = ctx.parentCtx.getChild(1).getChild(0).getText() # nome da função
    nome = self.escope
    paramList = [ ]
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
          
    self.function_args[self.escope] = lista_argumentos
    self.translator.openFunction(nome,paramList)
    super().visitFunction_body(ctx)
    self.translator.closeFunction()
  
  def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
    lista=list(ctx.getChildren())
    tipo_funcao = ctx.getChild(0).getText()
    nome_funcao = ctx.getChild(1).getText().split('(')[0]

    if nome_funcao in self.symbol_table:
      self.add_error(f"Error function '{nome_funcao}' already declared.", ctx)
    else:
      self.function_names[nome_funcao] = tipo_funcao
    return self.visitChildren(ctx)

  def visitFunction_header(self, ctx: MiniCParser.Function_headerContext):
    return self.visitChildren(ctx)
  
  
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
  
  def visitBinary(self, ctx: MiniCParser.BinaryContext):
    l = list(ctx.getChildren())
    for i in range(len(l)):
      self.binaryControler += 1
      if str(l[i].__class__.__name__) == "BinaryContext" and l[i].getChildCount() > 1:
        l2 = l[i]
        self.visit(l2)
        
      else:
        l2 = l[i]
        self.unarios.append((ctx.start.line,l2.getText()))
      self.binaryControler -= 1
    if self.binaryControler == 0:
      copia= self.unarios.copy()
      if ctx.parentCtx.parentCtx.getChild(0).getText() == 'if':
        self.translator.addBinary(copia,ctx.start.line,ehIf=True) 
      elif ctx.parentCtx.parentCtx.getChild(0).getText() == 'while':
        self.translator.addBinary(copia,ctx.start.line,ehIf=False,ehWhile=True) 
      elif ctx.parentCtx.parentCtx.getChild(0).getText() == 'return':
        self.translator.addBinary(copia,ctx.start.line,ehReturn=True)
      else:
        self.translator.addBinary(copia,ctx.start.line)
  def visitStatement(self, ctx: MiniCParser.StatementContext):
    l = list(ctx.getChildren())
    
    if l[0].getText() == 'while':
      self.visit(l[2])
      self.visit(l[4])
      self.translator.closeWhile()  


    elif l[0].getText() == 'if':
      self.visit(l[2])
      self.visit(l[4])
      
      if len(l) > 5:
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