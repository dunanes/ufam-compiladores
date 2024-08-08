# **Trabalho-Compiladores**

Um repositório para o nosso trabalho de compiladores, que envolve transformar um código na linguagem MiniC para um código capaz de ser executado no EduMips64.

## Passos para rodar

Para rodar os códigos, é necessário Python 3 e o runtime ANTLR4 para Python, instalado via `pip`.

**Passo 1**: Criar um ambiente virtual (opcional):

Para criar um ambiente virtual:

```bash
# Isso vai criar um ambiente virtual chamado comp

python3 -m venv comp

# Para entrar no ambiente virtual

source comp/bin/activate

```

> Após entrar no ambiente virtual, podemos usar o python3 apenas digitando `python` no terminal.

**Passo 2**: Instalar o runtime do ANTLR4

Após criar e entrar no ambiente virtual, instalamos o runtime do ANTLR4:

```bash
# Atualizar o pip

pip install --upgrade pip

# Instalar os requerimentos

pip install -r requirements.txt
```

Após instalar os requerimentos, podemos rodar os códigos normalmente.

**Passo 3**: Rodar os programas em python para gerar o código

Para gerar o código de três endereços e depois o código para ser executado no EduMIPS:

```bash
# Usar o código main.py para transformar código em .c para código de três endereços:

python main.py codigo.c

# Como exemplo: python main.py exemplos/ex13.c

# #

# Em seguida, convertemos o código de três endereços em código para edumips:

python mips.py tac.txt

# Como exemplo: python mips.py ./output/tac.txt
```

O código `main.py` tem sempre como saída o arquivo `tac.txt` na pasta `output`.

O código `mips.py` tem sempre como saída o arquivo `mips.txt` na pasta `output`.

O arquivo `./output/mips.txt` é o que pode ser usado no EduMips64.

> Ao rodar os códigos para outro arquivo em C, os anteriores serão substituídos.

## Alternativa para rodar os códigos

**Alternativamente**, usar o script para gerar os dois códigos a partir de um código em C:

```bash
# Garantir que o script é executável:

chmod +x run.sh

# Usar o script:

./run.sh codigo.c
```

Com isso o código será gerado e colocado na pasta output. O código mips.txt é o que pode ser usado no EduMips64.

## Integrantes da equipe

Integrantes:
Arthur Matias
Bianka Vasconcelos
Micael Viana
Daniel Nunes
