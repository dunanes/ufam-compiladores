from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor

class HtmlOutput():
    
    def __init__(self):
        self.conteudo = ""
        self.count = 0

    def HtmlOutput(self):
        self.count = 0
        self.conteudo = "<html>\n"
        self.conteudo += "<head><title>Formulario</title></head>\n"
        self.conteudo += "<body>\n"
        self.conteudo += "<form>\n"

    def addText(self, cols, rows, s):
        self.conteudo += s + "<br>\n"
        self.conteudo += "<textarea name='Q" + str(self.count) + "' cols='" + str(cols) + "' rows='" + str(rows) + "'></textarea><br>\n"
        self.conteudo += "<br>\n\n"
        self.count += 1
    
    def addRadio(self, s, options):
        self.conteudo += s + "<br>\n"
        for val in options:
            self.conteudo += "<input type='radio' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
        
        self.conteudo += "<br>\n\n"
        self.count+=1
    
    def addCheckBox(self, s , options):
        self.conteudo += s + "<br>\n"
        
        for val in options: 
            self.conteudo += "<input type='checkbox' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
            self.count+=1
        
        self.conteudo += "<br>\n\n"

    ## MODIFICAÇÕES

    def addMenu(self, s, options):
        self.conteudo += s + "<br>\n"
        self.conteudo += "<select name='Q" + str(self.count) + "' id='Q" + str(self.count) + "'>" + "\n"
    
        for val in options: 
            self.conteudo += "<option value='" + val + "'>" + val + "</option>\n"
        
        self.conteudo += "</select><br>\n\n"
        self.count+=1
    
    def addButton(self, label, action):
        self.conteudo += "<br>\n" + label + "<br>\n"
        self.conteudo += "<button type='button' onclick='alert(\"" + action + "\")'>" + label + "</button><br>\n\n"
        self.count+=1


    def close(self):
        self.conteudo += "</form>\n"
        self.conteudo += "</body>\n"
        self.conteudo += "</html>\n"
        print(self.conteudo)


class Visitor(HtmlVisitor):

    def __init__(self):
        self.html = HtmlOutput()

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for questao in l:
            self.visit(questao)

        self.html.close()
       
    def visitQTexto(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 4):
            cols = l[1].getText()
            rows = l[2].getText()
            string = self.visit(l[3])
            
            self.html.addText(cols, rows, string)

    def visitQRadioBox(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addRadio(string, opcoes)
    
    def visitQCheckBox(self, ctx: HtmlParser.QCheckBoxContext):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addCheckBox(string, opcoes)

    def visitOpcoes(self, ctx):
        l = list(ctx.getChildren())
        qtdStr = (len(l) - 2) // 2 # retirando os '()' e ','
        opcoes = []
        
        for i in range(qtdStr + 1):
            opcoes.append(self.visit(ctx.str_(i)))
        
        return opcoes
 
    def visitStr_(self, ctx):
        l = list(ctx.getChildren())
        string = l[0].getText().replace('"','')
        return string

    ## MODIFICAÇÕES

    def visitQMenu(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addMenu(string, opcoes)

    def visitQButton(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            label = self.visit(l[1])
            action = self.visit(l[2])
            self.html.addButton(label, action)


