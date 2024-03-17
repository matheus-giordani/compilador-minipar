import ply.yacc as yacc
from minipar_lex import tokens

# Definindo as regras de precedência e associatividade (se necessário)
precedence = (
    ('left', 'SEQ', 'PAR'),
    ('left', 'IF', 'ELSE', 'WHILE'),
    ('left', 'EQUAL'),
    ('left', 'LESSTHAN', 'GREATERTHAN', 'NOTEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'AND', 'OR'),
    ('left', 'CHAN')
)

variaveis = {}  # Dicionário para armazenar as variáveis

# Definindo as regras de produção
def p_programa_minipar(p):
    'programa_minipar : bloco_stmt'
    p[0] = p[1]
    return (p[0])

def p_bloco_stmt(p):
     '''bloco_stmt : bloco_SEQ
                  | bloco_PAR
                  | stmts''' 
     p[0] = p[1]

def p_bloco_SEQ(p):
    'bloco_SEQ : SEQ stmts'
    p[0] = p[2]

def p_bloco_PAR(p):
    'bloco_PAR : PAR stmts'
    p[0] = p[2]

def p_stmts(p):
    '''stmts : stmt
             | stmts stmt'''
    p[0] = p[1]

def p_stmt_atribuicao(p):
    'stmt : atribuicao'
    p[0] = p[1]

def p_stmt_comparacao(p):
    'stmt : comparacao'
    p[0] = p[1]
    
def p_stmt_if(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN LBRACE stmt RBRACE %prec IF
            | IF LPAREN comparacao RPAREN LBRACE stmt RBRACE %prec IF'''
    if(len(p) == 5):
        if((p[3]) == True):
            p[0] = p[5]

def p_stmt_if_else(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN LBRACE single_stmt RBRACE ELSE LBRACE single_stmt RBRACE
            | IF LPAREN comparacao RPAREN LBRACE single_stmt RBRACE ELSE LBRACE single_stmt RBRACE'''
    if((p[3]) == True):
        p[0] = p[5]
    else:
        p[0] = p[7]

def p_single_stmt(p):
    '''single_stmt : atribuicao
                   | comparacao'''
    p[0] = p[1]

def p_stmt_while(p):
    '''stmt : WHILE LPAREN BOOLEAN RPAREN LBRACE stmt RBRACE %prec WHILE
            | WHILE LPAREN comparacao RPAREN LBRACE stmt RBRACE %prec WHILE'''
    while(p[3]==True):
        p[0] = p[5]

def p_atribuicao(p):
    'atribuicao : ID EQUAL expr'
    variaveis[p[1]] = p[3]
    p[0] = p[3]

def p_comparacao(p):
    '''comparacao : expr LESSTHAN expr
                  | expr GREATERTHAN expr
                  | expr NOTEQUAL expr'''
    p[0] = eval(f"{p[1]} {p[2]} {p[3]}")
def p_expr(p):
    '''expr : c_channel
            | ID
            | NUMBER
            | operacao
            | BOOLEAN
            | STRING
            | LPAREN expr RPAREN
            | LPAREN c_channel RPAREN'''  # Adiciona a opção para c_channel dentro de LPAREN/RPAREN
    if isinstance(p[1], str):
        p[0] = variaveis.get(p[1], None)
    else:
        p[0] = p[1]
    
def p_operacao(p):
    '''operacao : adicao
                | subtracao
                | multiplicacao
                | divisao'''
    p[0] = p[1]
    
def p_adicao(p):
    '''adicao : NUMBER PLUS NUMBER
                | ID PLUS ID    
                | ID PLUS NUMBER'''
    if isinstance(p[1], int) and isinstance(p[3], int):
        p[0] = p[1] + p[3]
    elif isinstance(p[1], str) and isinstance(p[3], str):
        p[0] = variaveis.get(p[1], '') + variaveis.get(p[3], '')
    elif isinstance(p[1], str) and isinstance(p[3], int):
        p[0] = str(variaveis.get(p[1], '')) + str(p[3])  # Converta o valor da variável para string
    elif isinstance(p[1], int) and isinstance(p[3], str):
        p[0] = str(p[1]) + variaveis.get(p[3], '')  # Converta o valor da variável para string
    else:
        print("Operação de adição inválida: tipos incompatíveis")

    

def p_subtracao(p):
    'subtracao : NUMBER MINUS NUMBER'
    p[0] = p[1] - p[3]

def p_multiplicacao(p):
    'multiplicacao : NUMBER TIMES NUMBER'
    p[0] = p[1] * p[3]

def p_divisao(p):
    'divisao : NUMBER DIVIDE NUMBER'
    p[0] = p[1] / p[3]

def p_c_channel(p):
    'c_channel : CHAN ID ":" ID "," ID'
# Adicione outras regras de produção conforme necessário para tipos_var, INPUT, OUTPUT, etc.

# Função de tratamento de erros
errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print("ERRO: ", p)

# Criando o analisador
parser = yacc.yacc()

t = "r"

# Codigo de teste 

entrada = '''
SEQ
    a = 1 + 2
    while (a<10)
    {
        
        a = a + 1
    }
    '''
result = parser.parse(entrada)
print(result)
print(variaveis)
