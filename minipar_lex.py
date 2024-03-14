import ply.lex as lex
from ply.lex import TOKEN

saidas = []

def add_lista_saida(t,err):
    saidas.append((t.lineno, t.value, err))

# Palavras-chave reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'True': 'TRUE',
    'False': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'SEQ': 'SEQ',
    'PAR': 'PAR',
    'CHAN': 'CHAN'
}
# Lista de tokens
tokens = ['ID', 'EQUAL', 'LPAREN', 'RPAREN','NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LESSTHAN', 'GREATERTHAN', 'NOTEQUAL',"STRING", 'BOOLEAN',  'ASPAS', 'ERR_STRING', 'COMMENT'
] + list(reserved.values()) # Adiciona as palavras reservadas na lista de tokens

# Expressões regulares para tokens simples
t_IF = r'if'
t_COMMENT = r'\#.*'
t_ELSE = r'else'
t_WHILE = r'while'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_NOTEQUAL = r'!='
t_AND = r'and'
t_OR = r'or'
t_ASPAS = r'\"'
t_SEQ = r'SEQ'
t_PAR = r'PAR'
t_CHAN = r'CHAN'

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

identifier = r'[a-zA-Z_][a-zA-Z_0-9]*'


# Tratamento de números inteiros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'("[^"]*")'
    return t 

# Tratamento de strings
def t_ERR_STRING(t):
    r'"[^("|\n?)]*'
    return t 

     

# Tratamento de booleanos
def t_BOOLEAN(t): #Fazer o boleano identificar expressões como true ou false
    r'True|False'
    t.type = 'BOOLEAN'
    return t

# Tratamento de identificadores
@TOKEN(identifier)
def t_ID(t):
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Tratamento de quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)




# Construa o analisador léxico
lexer = lex.lex()

# # Exemplo de teste
# example_input = '''
# SEQ
#     result = True
#     i = 1
#     WHILE (i <= 10)
#         IF (i>2 and i != 0 and result)
#             result = result and False
#         i = i + 1
#     #testando comentarios
# PAR
#     j = 1
#     WHILE (j <= 10)
#         IF (j>2 and j != 0 and result)
#             result = result and False
#         j = j + 1
# '''

# lexer.input(example_input)

# # Exiba os tokens encontrados
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
