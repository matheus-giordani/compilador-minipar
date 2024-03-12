
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSEQPARleftIFELSEWHILEleftEQUALleftLESSTHANGREATERTHANNOTEQUALleftPLUSMINUSleftTIMESDIVIDEleftANDORleftCHANAND ASPAS BOOLEAN CHAN COMMENT DIVIDE ELSE EQUAL ERR_STRING FALSE GREATERTHAN ID IF LESSTHAN LPAREN MINUS NOTEQUAL NUMBER OR PAR PLUS RPAREN SEQ STRING TIMES TRUE WHILEprograma_minipar : bloco_stmtbloco_stmt : bloco_SEQ\n                  | bloco_PAR\n                  | stmtsbloco_SEQ : SEQ stmtsbloco_PAR : PAR stmtsstmts : stmt\n             | stmts stmtstmt : atribuicaostmt : IF LPAREN BOOLEAN RPAREN stmt %prec IFstmt : IF LPAREN BOOLEAN RPAREN stmt ELSE stmtstmt : WHILE LPAREN BOOLEAN RPAREN stmt %prec WHILEatribuicao : ID EQUAL exprexpr : c_channel\n            | ID\n            | NUMBER\n            | BOOLEAN\n            | STRING\n            | LPAREN expr RPAREN\n            | LPAREN c_channel RPARENc_channel : CHAN ID ":" ID "," ID'
    
_lr_action_items = {'SEQ':([0,],[6,]),'PAR':([0,],[7,]),'IF':([0,5,6,7,8,9,13,14,15,21,22,23,24,25,26,29,30,34,35,36,37,39,41,43,],[10,10,10,10,-7,-9,-8,10,10,-15,-13,-14,-16,-17,-18,10,10,-10,-12,-19,-20,10,-11,-21,]),'WHILE':([0,5,6,7,8,9,13,14,15,21,22,23,24,25,26,29,30,34,35,36,37,39,41,43,],[11,11,11,11,-7,-9,-8,11,11,-15,-13,-14,-16,-17,-18,11,11,-10,-12,-19,-20,11,-11,-21,]),'ID':([0,5,6,7,8,9,13,14,15,18,21,22,23,24,25,26,27,28,29,30,34,35,36,37,38,39,41,42,43,],[12,12,12,12,-7,-9,-8,12,12,21,-15,-13,-14,-16,-17,-18,21,33,12,12,-10,-12,-19,-20,40,12,-11,43,-21,]),'$end':([1,2,3,4,5,8,9,13,14,15,21,22,23,24,25,26,34,35,36,37,41,43,],[0,-1,-2,-3,-4,-7,-9,-8,-5,-6,-15,-13,-14,-16,-17,-18,-10,-12,-19,-20,-11,-21,]),'ELSE':([9,21,22,23,24,25,26,34,35,36,37,41,43,],[-9,-15,-13,-14,-16,-17,-18,-10,-12,-19,-20,-11,-21,]),'LPAREN':([10,11,18,27,],[16,17,27,27,]),'EQUAL':([12,],[18,]),'BOOLEAN':([16,17,18,27,],[19,20,25,25,]),'NUMBER':([18,27,],[24,24,]),'STRING':([18,27,],[26,26,]),'CHAN':([18,27,],[28,28,]),'RPAREN':([19,20,21,24,25,26,31,32,36,37,43,],[29,30,-15,-16,-17,-18,36,37,-19,-20,-21,]),':':([33,],[38,]),',':([40,],[42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa_minipar':([0,],[1,]),'bloco_stmt':([0,],[2,]),'bloco_SEQ':([0,],[3,]),'bloco_PAR':([0,],[4,]),'stmts':([0,6,7,],[5,14,15,]),'stmt':([0,5,6,7,14,15,29,30,39,],[8,13,8,8,13,13,34,35,41,]),'atribuicao':([0,5,6,7,14,15,29,30,39,],[9,9,9,9,9,9,9,9,9,]),'expr':([18,27,],[22,31,]),'c_channel':([18,27,],[23,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa_minipar","S'",1,None,None,None),
  ('programa_minipar -> bloco_stmt','programa_minipar',1,'p_programa_minipar','synth.py',20),
  ('bloco_stmt -> bloco_SEQ','bloco_stmt',1,'p_bloco_stmt','synth.py',23),
  ('bloco_stmt -> bloco_PAR','bloco_stmt',1,'p_bloco_stmt','synth.py',24),
  ('bloco_stmt -> stmts','bloco_stmt',1,'p_bloco_stmt','synth.py',25),
  ('bloco_SEQ -> SEQ stmts','bloco_SEQ',2,'p_bloco_SEQ','synth.py',28),
  ('bloco_PAR -> PAR stmts','bloco_PAR',2,'p_bloco_PAR','synth.py',31),
  ('stmts -> stmt','stmts',1,'p_stmts','synth.py',34),
  ('stmts -> stmts stmt','stmts',2,'p_stmts','synth.py',35),
  ('stmt -> atribuicao','stmt',1,'p_stmt_atribuicao','synth.py',38),
  ('stmt -> IF LPAREN BOOLEAN RPAREN stmt','stmt',5,'p_stmt_if','synth.py',41),
  ('stmt -> IF LPAREN BOOLEAN RPAREN stmt ELSE stmt','stmt',7,'p_stmt_if_else','synth.py',44),
  ('stmt -> WHILE LPAREN BOOLEAN RPAREN stmt','stmt',5,'p_stmt_while','synth.py',47),
  ('atribuicao -> ID EQUAL expr','atribuicao',3,'p_atribuicao','synth.py',50),
  ('expr -> c_channel','expr',1,'p_expr','synth.py',53),
  ('expr -> ID','expr',1,'p_expr','synth.py',54),
  ('expr -> NUMBER','expr',1,'p_expr','synth.py',55),
  ('expr -> BOOLEAN','expr',1,'p_expr','synth.py',56),
  ('expr -> STRING','expr',1,'p_expr','synth.py',57),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr','synth.py',58),
  ('expr -> LPAREN c_channel RPAREN','expr',3,'p_expr','synth.py',59),
  ('c_channel -> CHAN ID : ID , ID','c_channel',6,'p_c_channel','synth.py',62),
]
