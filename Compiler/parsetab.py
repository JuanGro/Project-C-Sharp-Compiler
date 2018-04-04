
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IF ELSE DO WHILE INT BOOL STRING ID PLUS MINUS TIMES DIVIDE LOR LAND LT LE GT GE EQ NE EQUALS LPAREN RPAREN LBRACE RBRACE SEMI DIGIT\n    statement : expression_statement\n              | selection_statement\n              | iteration_statement\n    \n    type_specifier : INT\n                      | BOOL\n                      | STRING\n    expression_statement : declaration_expression SEMIdeclaration_expression : assignment_expressiondeclaration_expression : type_specifier declaration_expressionselection_statement : IF LPAREN logical_expression RPAREN LBRACE statement RBRACEselection_statement : selection_statement ELSE LBRACE statement RBRACEiteration_statement : WHILE LPAREN logical_expression RPAREN statementiteration_statement : DO statement WHILE LPAREN logical_expression RPAREN SEMIassignment_expression : additive_expressionassignment_expression : assignment_expression assignment_operators additive_expressionlogical_expression : equality_expressionlogical_expression : logical_expression logical_operators equality_expressionequality_expression : relational_expressionequality_expression : equality_expression equality_operators relational_expressionrelational_expression : additive_expressionrelational_expression : relational_expression relational_operators additive_expressionadditive_expression : multiplicative_expressionadditive_expression : additive_expression additive_operators multiplicative_expressionmultiplicative_expression : primary_expressionmultiplicative_expression : multiplicative_expression multiplicative_operators primary_expression\n    assignment_operators : EQUALS\n    \n    logical_operators : LAND\n                      | LOR\n    \n    equality_operators : EQ\n                       | NE\n    \n    relational_operators : LT\n                         | GT\n                         | LE\n                         | GE\n    \n    additive_operators : PLUS\n                       | MINUS\n    \n    multiplicative_operators : TIMES\n                             | DIVIDE\n    \n    primary_expression :  ID\n                       |  DIGIT\n    '
    
_lr_action_items = {'IF':([0,8,33,56,59,],[6,6,6,6,6,]),'WHILE':([0,2,3,4,8,20,23,33,56,58,59,63,67,68,],[7,-1,-2,-3,7,-7,39,7,7,-11,7,-12,-10,-13,]),'DO':([0,8,33,56,59,],[8,8,8,8,8,]),'INT':([0,8,10,12,13,14,33,56,59,],[12,12,12,-4,-5,-6,12,12,12,]),'BOOL':([0,8,10,12,13,14,33,56,59,],[13,13,13,-4,-5,-6,13,13,13,]),'STRING':([0,8,10,12,13,14,33,56,59,],[14,14,14,-4,-5,-6,14,14,14,]),'ID':([0,8,10,12,13,14,21,22,24,25,27,28,29,30,31,32,33,45,46,47,48,49,50,51,52,53,54,55,56,57,59,],[17,17,17,-4,-5,-6,17,17,17,-26,17,-35,-36,17,-37,-38,17,17,-27,-28,17,-29,-30,17,-31,-32,-33,-34,17,17,17,]),'DIGIT':([0,8,10,12,13,14,21,22,24,25,27,28,29,30,31,32,33,45,46,47,48,49,50,51,52,53,54,55,56,57,59,],[18,18,18,-4,-5,-6,18,18,18,-26,18,-35,-36,18,-37,-38,18,18,-27,-28,18,-29,-30,18,-31,-32,-33,-34,18,18,18,]),'$end':([1,2,3,4,20,58,63,67,68,],[0,-1,-2,-3,-7,-11,-12,-10,-13,]),'RBRACE':([2,3,4,20,43,58,63,65,67,68,],[-1,-2,-3,-7,58,-11,-12,67,-10,-13,]),'ELSE':([3,58,67,],[19,-11,-10,]),'SEMI':([5,9,11,15,16,17,18,26,40,41,42,66,],[20,-8,-14,-22,-24,-39,-40,-9,-15,-23,-25,68,]),'LPAREN':([6,7,39,],[21,22,57,]),'EQUALS':([9,11,15,16,17,18,40,41,42,],[25,-14,-22,-24,-39,-40,-15,-23,-25,]),'PLUS':([11,15,16,17,18,37,40,41,42,62,],[28,-22,-24,-39,-40,28,28,-23,-25,28,]),'MINUS':([11,15,16,17,18,37,40,41,42,62,],[29,-22,-24,-39,-40,29,29,-23,-25,29,]),'LT':([15,16,17,18,36,37,41,42,61,62,],[-22,-24,-39,-40,52,-20,-23,-25,52,-21,]),'GT':([15,16,17,18,36,37,41,42,61,62,],[-22,-24,-39,-40,53,-20,-23,-25,53,-21,]),'LE':([15,16,17,18,36,37,41,42,61,62,],[-22,-24,-39,-40,54,-20,-23,-25,54,-21,]),'GE':([15,16,17,18,36,37,41,42,61,62,],[-22,-24,-39,-40,55,-20,-23,-25,55,-21,]),'EQ':([15,16,17,18,35,36,37,41,42,60,61,62,],[-22,-24,-39,-40,49,-18,-20,-23,-25,49,-19,-21,]),'NE':([15,16,17,18,35,36,37,41,42,60,61,62,],[-22,-24,-39,-40,50,-18,-20,-23,-25,50,-19,-21,]),'RPAREN':([15,16,17,18,34,35,36,37,38,41,42,60,61,62,64,],[-22,-24,-39,-40,44,-16,-18,-20,56,-23,-25,-17,-19,-21,66,]),'LAND':([15,16,17,18,34,35,36,37,38,41,42,60,61,62,64,],[-22,-24,-39,-40,46,-16,-18,-20,46,-23,-25,-17,-19,-21,46,]),'LOR':([15,16,17,18,34,35,36,37,38,41,42,60,61,62,64,],[-22,-24,-39,-40,47,-16,-18,-20,47,-23,-25,-17,-19,-21,47,]),'TIMES':([15,16,17,18,41,42,],[31,-24,-39,-40,31,-25,]),'DIVIDE':([15,16,17,18,41,42,],[32,-24,-39,-40,32,-25,]),'LBRACE':([19,44,],[33,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,8,33,56,59,],[1,23,43,63,65,]),'expression_statement':([0,8,33,56,59,],[2,2,2,2,2,]),'selection_statement':([0,8,33,56,59,],[3,3,3,3,3,]),'iteration_statement':([0,8,33,56,59,],[4,4,4,4,4,]),'declaration_expression':([0,8,10,33,56,59,],[5,5,26,5,5,5,]),'assignment_expression':([0,8,10,33,56,59,],[9,9,9,9,9,9,]),'type_specifier':([0,8,10,33,56,59,],[10,10,10,10,10,10,]),'additive_expression':([0,8,10,21,22,24,33,45,48,51,56,57,59,],[11,11,11,37,37,40,11,37,37,62,11,37,11,]),'multiplicative_expression':([0,8,10,21,22,24,27,33,45,48,51,56,57,59,],[15,15,15,15,15,15,41,15,15,15,15,15,15,15,]),'primary_expression':([0,8,10,21,22,24,27,30,33,45,48,51,56,57,59,],[16,16,16,16,16,16,16,42,16,16,16,16,16,16,16,]),'assignment_operators':([9,],[24,]),'additive_operators':([11,37,40,62,],[27,27,27,27,]),'multiplicative_operators':([15,41,],[30,30,]),'logical_expression':([21,22,57,],[34,38,64,]),'equality_expression':([21,22,45,57,],[35,35,60,35,]),'relational_expression':([21,22,45,48,57,],[36,36,36,61,36,]),'logical_operators':([34,38,64,],[45,45,45,]),'equality_operators':([35,60,],[48,48,]),'relational_operators':([36,61,],[51,51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression_statement','statement',1,'p_statement','parser.py',10),
  ('statement -> selection_statement','statement',1,'p_statement','parser.py',11),
  ('statement -> iteration_statement','statement',1,'p_statement','parser.py',12),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',19),
  ('type_specifier -> BOOL','type_specifier',1,'p_type_specifier','parser.py',20),
  ('type_specifier -> STRING','type_specifier',1,'p_type_specifier','parser.py',21),
  ('expression_statement -> declaration_expression SEMI','expression_statement',2,'p_expression_statement_1','parser.py',27),
  ('declaration_expression -> assignment_expression','declaration_expression',1,'p_declaration_expression_1','parser.py',31),
  ('declaration_expression -> type_specifier declaration_expression','declaration_expression',2,'p_declaration_expression_2','parser.py',34),
  ('selection_statement -> IF LPAREN logical_expression RPAREN LBRACE statement RBRACE','selection_statement',7,'p_selection_statement_1','parser.py',38),
  ('selection_statement -> selection_statement ELSE LBRACE statement RBRACE','selection_statement',5,'p_selection_statement_2','parser.py',42),
  ('iteration_statement -> WHILE LPAREN logical_expression RPAREN statement','iteration_statement',5,'p_iteration_statement_1','parser.py',47),
  ('iteration_statement -> DO statement WHILE LPAREN logical_expression RPAREN SEMI','iteration_statement',7,'p_iteration_statement_2','parser.py',51),
  ('assignment_expression -> additive_expression','assignment_expression',1,'p_assignment_expression_1','parser.py',56),
  ('assignment_expression -> assignment_expression assignment_operators additive_expression','assignment_expression',3,'p_assignment_expression_2','parser.py',60),
  ('logical_expression -> equality_expression','logical_expression',1,'p_logical_expression_1','parser.py',65),
  ('logical_expression -> logical_expression logical_operators equality_expression','logical_expression',3,'p_logical_expression_2','parser.py',69),
  ('equality_expression -> relational_expression','equality_expression',1,'p_equality_expression_1','parser.py',74),
  ('equality_expression -> equality_expression equality_operators relational_expression','equality_expression',3,'p_equality_expression_2','parser.py',78),
  ('relational_expression -> additive_expression','relational_expression',1,'p_relational_expression_1','parser.py',83),
  ('relational_expression -> relational_expression relational_operators additive_expression','relational_expression',3,'p_relational_expression_2','parser.py',87),
  ('additive_expression -> multiplicative_expression','additive_expression',1,'p_additive_expression_1','parser.py',92),
  ('additive_expression -> additive_expression additive_operators multiplicative_expression','additive_expression',3,'p_additive_expression_2','parser.py',96),
  ('multiplicative_expression -> primary_expression','multiplicative_expression',1,'p_multiplicative_expression_1','parser.py',101),
  ('multiplicative_expression -> multiplicative_expression multiplicative_operators primary_expression','multiplicative_expression',3,'p_multiplicative_expression_2','parser.py',105),
  ('assignment_operators -> EQUALS','assignment_operators',1,'p_assignment_operators','parser.py',111),
  ('logical_operators -> LAND','logical_operators',1,'p_logical_operators','parser.py',117),
  ('logical_operators -> LOR','logical_operators',1,'p_logical_operators','parser.py',118),
  ('equality_operators -> EQ','equality_operators',1,'p_equality_operators','parser.py',124),
  ('equality_operators -> NE','equality_operators',1,'p_equality_operators','parser.py',125),
  ('relational_operators -> LT','relational_operators',1,'p_relational_operators','parser.py',131),
  ('relational_operators -> GT','relational_operators',1,'p_relational_operators','parser.py',132),
  ('relational_operators -> LE','relational_operators',1,'p_relational_operators','parser.py',133),
  ('relational_operators -> GE','relational_operators',1,'p_relational_operators','parser.py',134),
  ('additive_operators -> PLUS','additive_operators',1,'p_additive_operators','parser.py',141),
  ('additive_operators -> MINUS','additive_operators',1,'p_additive_operators','parser.py',142),
  ('multiplicative_operators -> TIMES','multiplicative_operators',1,'p_multiplicative_operators','parser.py',148),
  ('multiplicative_operators -> DIVIDE','multiplicative_operators',1,'p_multiplicative_operators','parser.py',149),
  ('primary_expression -> ID','primary_expression',1,'p_primary_expression','parser.py',155),
  ('primary_expression -> DIGIT','primary_expression',1,'p_primary_expression','parser.py',156),
]
