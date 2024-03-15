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
    p[0] = p[1]

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
    '''stmt : IF LPAREN BOOLEAN RPAREN LBRACE stmt RBRACE %prec IF
            | IF LPAREN comparacao RPAREN LBRACE stmt RBRACE %prec IF'''
    if(p[3]):
        p[6]
    


def p_stmt_if_else(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN LBRACE single_stmt RBRACE ELSE LBRACE single_stmt RBRACE
            | IF LPAREN comparacao RPAREN single_stmt ELSE single_stmt'''
    if(p[3]):
        p[6]

def p_single_stmt(p):
    '''single_stmt : atribuicao
                   | comparacao'''

def p_stmt_while(p):
    '''stmt : WHILE LPAREN BOOLEAN RPAREN stmt %prec WHILE
            | WHILE LPAREN comparacao RPAREN stmt %prec WHILE'''

def p_atribuicao(p):
    'atribuicao : ID ASSIGN expr'
    p[0] = p[1] = p[3]

def p_comparacao(t):
    '''comparacao : expr LESSTHAN expr
                  | expr GREATERTHAN expr
                  | expr NOTEQUAL expr
                  | expr GREATEROREQUAL expr
                  | expr LESSTHANOREQUAL expr
                  | expr EQUAL expr
                  '''
    if()
    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    
def p_expr(p):
    '''expr : c_channel
            | ID
            | NUMBER
            | operacao
            | BOOLEAN
            | STRING
            | LPAREN expr RPAREN
            | LPAREN c_channel RPAREN'''  # Adiciona a opção para c_channel dentro de LPAREN/RPAREN
    if(len(p)==2):
        p[0] = p[1]
        return
    if(len(p)==3):
        p[0] = p[2]
        
    
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
    if ( teste < 5 ){
        
        teste = teste + 1
    }
'''

# Codigo teste
# '''
# PAR
#     if ( True )
#         teste = 2
#     else
#         teste2 = 4
    
# '''

t = "r"


result = parser.parse(entrada)
