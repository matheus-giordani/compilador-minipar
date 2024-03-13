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
    'programa_minipar : stmt'



def p_stmt(p):
    '''stmt :   bloco_SEQ
                | bloco_PAR
                | stmt  '''  

def p_stmts(p):
    '''stmts : stmt 
             | stmts stmt'''

def p_bloco_SEQ(p):
    'bloco_SEQ : SEQ stmts'

def p_bloco_PAR(p):
    'bloco_PAR : PAR stmts'

def p_stmt_atribuicao(p):
    'stmt : atribuicao'

# trocar stmt por expr?????
def p_stmt_if(p):
    'stmt : IF expr LCURLY stmt RCURLY  %prec IF'



def p_stmt_if_else(p):
    'stmt : IF expr stmt ELSE stmt'

    
def p_stmt_while(p):
    'stmt : WHILE expr stmt %prec WHILE'

def p_atribuicao(p):
    'atribuicao : ID EQUAL expr'
    
def p_comp(p):
    '''comp :    NUMBER LESSTHAN NUMBER
               | NUMBER GREATERTHAN NUMBER
               | NUMBER EQUAL NUMBER
               | NUMBER NOTEQUAL 
               | comp AND comp
               | comp OR comp
               '''
    
    
def p_expr(p):
    '''expr : c_channel
            | ID
            | NUMBER
            | BOOLEAN
            | STRING
            | NUMBER PLUS NUMBER
            | NUMBER MINUS NUMBER
            | NUMBER TIMES NUMBER
            | NUMBER DIVIDE NUMBER
            | LPAREN comp  RPAREN
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
SEQ
    
    if (1 > 0) { 1 + 1 }
     
'''

result = parser.parse(entrada)
