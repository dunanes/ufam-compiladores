# **Representação intermediária**

Trabalho sobre representação intermediária.

Já está tudo gerado, só precisa rodar. Uns exemplos abaixo:

```bash
# Esse tem tudo
python3 main.py exemplos/exemplao.c
```

Caso queira gerar do zero, utilizar os passos abaixo.

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

Para gerar a representação intermediária, rodar:

```bash
# Usar o código main.py para transformar código em .c para código de três endereços:

python main.py codigo.c
```

O código `main.py` tem sempre como saída o arquivo `tac.txt` na pasta `output`.

> Ao rodar os códigos para outro arquivo em C, os anteriores serão substituídos.
