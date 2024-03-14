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

# Definindo as regras de produção
def p_programa_minipar(p):
    'programa_minipar : bloco_stmt'

def p_bloco_stmt(p):
     '''bloco_stmt : bloco_SEQ
                  | bloco_PAR
                  | stmts''' 

def p_bloco_SEQ(p):
    'bloco_SEQ : SEQ stmts'

def p_bloco_PAR(p):
    'bloco_PAR : PAR stmts'

def p_stmts(p):
    '''stmts : stmt
             | stmts stmt'''

def p_stmt_atribuicao(p):
    'stmt : atribuicao'
    
def p_stmt_if(p):
    'stmt : IF LPAREN BOOLEAN RPAREN expr %prec IF'

def p_stmt_if_else(p):
    'stmt : IF LPAREN BOOLEAN RPAREN stmt ELSE stmt'

def p_stmt_while(p):
    'stmt : WHILE LPAREN BOOLEAN RPAREN stmt %prec WHILE'

def p_atribuicao(p):
    'atribuicao : ID EQUAL expr'
    
def p_expr(p):
    '''expr : c_channel
            | ID
            | NUMBER
            | BOOLEAN
            | STRING
            | LPAREN expr RPAREN
            | LPAREN c_channel RPAREN'''  # Adiciona a opção para c_channel dentro de LPAREN/RPAREN

def p_c_channel(p):
    'c_channel : CHAN ID ":" ID "," ID'
# Adicione outras regras de produção conforme necessário para tipos_var, INPUT, OUTPUT, etc.

# Função de tratamento de erros
errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print("ERRO: ",p)

# Criando o analisador
parser = yacc.yacc()

# Exemplo de uso do analisador
entrada = '''
PAR
    if ( True )
        teste = 2
    else
        teste2 = 4
    
'''

t = "r"


result = parser.parse(entrada)
