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

def p_stmt_comparacao(p):
    'stmt : comparacao'
    
def p_stmt_if(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN stmt %prec IF
            | IF LPAREN comparacao RPAREN stmt %prec IF'''

def p_stmt_if_else(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN single_stmt ELSE single_stmt
            | IF LPAREN comparacao RPAREN single_stmt ELSE single_stmt'''

def p_single_stmt(p):
    '''single_stmt : atribuicao
                   | comparacao'''

def p_stmt_while(p):
    '''stmt : WHILE LPAREN BOOLEAN RPAREN stmt %prec WHILE
            | WHILE LPAREN comparacao RPAREN stmt %prec WHILE'''

def p_atribuicao(p):
    'atribuicao : ID EQUAL expr'

def p_comparacao(p):
    '''comparacao : expr LESSTHAN expr
                  | expr GREATERTHAN expr
                  | expr NOTEQUAL expr'''
    
def p_expr(p):
    '''expr : c_channel
            | ID
            | NUMBER
            | operacao
            | BOOLEAN
            | STRING
            | LPAREN expr RPAREN
            | LPAREN c_channel RPAREN'''  # Adiciona a opção para c_channel dentro de LPAREN/RPAREN
    
def p_operacao(p):
    '''operacao : expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr AND expr
                | expr OR expr'''

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
    teste = 0
    while ( teste < 5 )
        teste = teste + 1
'''

# Codigo teste
'''
PAR
    if ( True )
        teste = 2
    else
        teste2 = 4
    
'''

t = "r"


result = parser.parse(entrada)
