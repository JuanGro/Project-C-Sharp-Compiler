
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IF ELSE DO WHILE INT BOOL STRING CONSOLE WRITELINE READLINE TRUE FALSE ID CONSTANT PLUS MINUS TIMES DIVIDE LOR LAND LT LE GT GE EQ NE EQUALS LPAREN RPAREN LBRACE RBRACE DOT SEMI STRING_SENTENCE DIGITstatement_list : emptystatement_list : statementstatement_list : statement_list statement\n    statement : expression_statement\n              | selection_statement\n              | iteration_statement\n    expression_statement : declaration_expression SEMIexpression_statement : empty SEMIexpression_statement : input_expression SEMIexpression_statement : output_expression SEMIdeclaration_expression : assignment_expressiondeclaration_expression : type_specifier declaration_expressionselection_statement : IF conditional_expression block_statement_listselection_statement : selection_statement ELSE block_statement_listiteration_statement : WHILE conditional_expression block_statement_listiteration_statement : DO block_statement_list WHILE conditional_expressionblock_statement_list : LBRACE statement_list RBRACEconditional_expression : LPAREN logical_expression RPARENassignment_expression : variable_expressionassignment_expression : assignment_expression EQUALS logical_expressionassignment_expression : assignment_expression EQUALS input_expressionlogical_expression : equality_expressionlogical_expression : logical_expression logical_operators equality_expressionequality_expression : relational_expressionequality_expression : equality_expression equality_operators relational_expressionrelational_expression : math_expressionrelational_expression : relational_expression relational_operators math_expressionmath_expression : primary_expressionmath_expression : math_expression math_operators primary_expressioninput_expression : CONSOLE DOT READLINE LPAREN RPARENoutput_expression : CONSOLE DOT WRITELINE conditional_expression\n    type_specifier : INT\n                   | BOOL\n                   | STRING\n    \n    logical_operators : LAND\n                      | LOR\n    \n    equality_operators : EQ\n                       | NE\n    \n    relational_operators : LT\n                         | GT\n                         | LE\n                         | GE\n    \n    math_operators : PLUS\n                   | MINUS\n                   | TIMES\n                   | DIVIDE\n    \n    primary_expression :  variable_expression\n                       |  DIGIT\n                       |  STRING_SENTENCE\n                       |  boolean_expression\n    \n    variable_expression : ID\n                        | CONSTANT\n    \n    boolean_expression : TRUE\n                       | FALSE\n    empty : '
    
_lr_action_items = {'SEMI':([0,1,2,3,4,5,6,7,8,9,13,16,20,21,22,23,24,26,27,28,33,35,37,38,40,41,42,43,44,45,46,47,48,49,50,52,53,54,58,75,76,79,80,81,82,83,84,],[-55,-55,24,-2,-4,-5,-6,26,27,28,-11,-19,-51,-52,-3,24,-8,-7,-9,-10,-55,-12,-14,-13,-22,-24,-26,-28,-47,-48,-49,-50,-53,-54,-15,-55,-20,-21,-18,-16,-17,-31,-23,-25,-27,-29,-30,]),'IF':([0,1,2,3,4,5,6,22,24,26,27,28,33,37,38,50,52,58,75,76,],[10,10,-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,10,-14,-13,-15,10,-18,-16,-17,]),'WHILE':([0,1,2,3,4,5,6,22,24,26,27,28,32,33,37,38,50,52,58,75,76,],[11,11,-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,51,11,-14,-13,-15,11,-18,-16,-17,]),'DO':([0,1,2,3,4,5,6,22,24,26,27,28,33,37,38,50,52,58,75,76,],[12,12,-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,12,-14,-13,-15,12,-18,-16,-17,]),'CONSOLE':([0,1,2,3,4,5,6,22,24,26,27,28,33,34,37,38,50,52,58,75,76,],[15,15,-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,15,55,-14,-13,-15,15,-18,-16,-17,]),'INT':([0,1,2,3,4,5,6,14,17,18,19,22,24,26,27,28,33,37,38,50,52,58,75,76,],[17,17,-1,-2,-4,-5,-6,17,-32,-33,-34,-3,-8,-7,-9,-10,17,-14,-13,-15,17,-18,-16,-17,]),'BOOL':([0,1,2,3,4,5,6,14,17,18,19,22,24,26,27,28,33,37,38,50,52,58,75,76,],[18,18,-1,-2,-4,-5,-6,18,-32,-33,-34,-3,-8,-7,-9,-10,18,-14,-13,-15,18,-18,-16,-17,]),'STRING':([0,1,2,3,4,5,6,14,17,18,19,22,24,26,27,28,33,37,38,50,52,58,75,76,],[19,19,-1,-2,-4,-5,-6,19,-32,-33,-34,-3,-8,-7,-9,-10,19,-14,-13,-15,19,-18,-16,-17,]),'ID':([0,1,2,3,4,5,6,14,17,18,19,22,24,26,27,28,30,33,34,37,38,50,52,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,],[20,20,-1,-2,-4,-5,-6,20,-32,-33,-34,-3,-8,-7,-9,-10,20,20,20,-14,-13,-15,20,-18,20,-35,-36,20,-37,-38,20,-39,-40,-41,-42,20,-43,-44,-45,-46,-16,-17,]),'CONSTANT':([0,1,2,3,4,5,6,14,17,18,19,22,24,26,27,28,30,33,34,37,38,50,52,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,],[21,21,-1,-2,-4,-5,-6,21,-32,-33,-34,-3,-8,-7,-9,-10,21,21,21,-14,-13,-15,21,-18,21,-35,-36,21,-37,-38,21,-39,-40,-41,-42,21,-43,-44,-45,-46,-16,-17,]),'$end':([0,1,2,3,4,5,6,22,24,26,27,28,37,38,50,58,75,76,],[-55,0,-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,-14,-13,-15,-18,-16,-17,]),'RBRACE':([2,3,4,5,6,22,24,26,27,28,33,37,38,50,52,58,75,76,],[-1,-2,-4,-5,-6,-3,-8,-7,-9,-10,-55,-14,-13,-15,76,-18,-16,-17,]),'ELSE':([5,37,38,76,],[25,-14,-13,-17,]),'LPAREN':([10,11,51,56,57,],[30,30,30,78,30,]),'LBRACE':([12,25,29,31,58,],[33,33,33,33,-18,]),'EQUALS':([13,16,20,21,40,41,42,43,44,45,46,47,48,49,53,54,80,81,82,83,84,],[34,-19,-51,-52,-22,-24,-26,-28,-47,-48,-49,-50,-53,-54,-20,-21,-23,-25,-27,-29,-30,]),'DOT':([15,55,],[36,77,]),'PLUS':([20,21,42,43,44,45,46,47,48,49,82,83,],[-51,-52,71,-28,-47,-48,-49,-50,-53,-54,71,-29,]),'MINUS':([20,21,42,43,44,45,46,47,48,49,82,83,],[-51,-52,72,-28,-47,-48,-49,-50,-53,-54,72,-29,]),'TIMES':([20,21,42,43,44,45,46,47,48,49,82,83,],[-51,-52,73,-28,-47,-48,-49,-50,-53,-54,73,-29,]),'DIVIDE':([20,21,42,43,44,45,46,47,48,49,82,83,],[-51,-52,74,-28,-47,-48,-49,-50,-53,-54,74,-29,]),'LT':([20,21,41,42,43,44,45,46,47,48,49,81,82,83,],[-51,-52,66,-26,-28,-47,-48,-49,-50,-53,-54,66,-27,-29,]),'GT':([20,21,41,42,43,44,45,46,47,48,49,81,82,83,],[-51,-52,67,-26,-28,-47,-48,-49,-50,-53,-54,67,-27,-29,]),'LE':([20,21,41,42,43,44,45,46,47,48,49,81,82,83,],[-51,-52,68,-26,-28,-47,-48,-49,-50,-53,-54,68,-27,-29,]),'GE':([20,21,41,42,43,44,45,46,47,48,49,81,82,83,],[-51,-52,69,-26,-28,-47,-48,-49,-50,-53,-54,69,-27,-29,]),'EQ':([20,21,40,41,42,43,44,45,46,47,48,49,80,81,82,83,],[-51,-52,63,-24,-26,-28,-47,-48,-49,-50,-53,-54,63,-25,-27,-29,]),'NE':([20,21,40,41,42,43,44,45,46,47,48,49,80,81,82,83,],[-51,-52,64,-24,-26,-28,-47,-48,-49,-50,-53,-54,64,-25,-27,-29,]),'RPAREN':([20,21,39,40,41,42,43,44,45,46,47,48,49,78,80,81,82,83,],[-51,-52,58,-22,-24,-26,-28,-47,-48,-49,-50,-53,-54,84,-23,-25,-27,-29,]),'LAND':([20,21,39,40,41,42,43,44,45,46,47,48,49,53,80,81,82,83,],[-51,-52,60,-22,-24,-26,-28,-47,-48,-49,-50,-53,-54,60,-23,-25,-27,-29,]),'LOR':([20,21,39,40,41,42,43,44,45,46,47,48,49,53,80,81,82,83,],[-51,-52,61,-22,-24,-26,-28,-47,-48,-49,-50,-53,-54,61,-23,-25,-27,-29,]),'DIGIT':([30,34,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[45,45,45,-35,-36,45,-37,-38,45,-39,-40,-41,-42,45,-43,-44,-45,-46,]),'STRING_SENTENCE':([30,34,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[46,46,46,-35,-36,46,-37,-38,46,-39,-40,-41,-42,46,-43,-44,-45,-46,]),'TRUE':([30,34,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[48,48,48,-35,-36,48,-37,-38,48,-39,-40,-41,-42,48,-43,-44,-45,-46,]),'FALSE':([30,34,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[49,49,49,-35,-36,49,-37,-38,49,-39,-40,-41,-42,49,-43,-44,-45,-46,]),'READLINE':([36,77,],[56,56,]),'WRITELINE':([36,],[57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,33,],[1,52,]),'empty':([0,1,33,52,],[2,23,2,23,]),'statement':([0,1,33,52,],[3,22,3,22,]),'expression_statement':([0,1,33,52,],[4,4,4,4,]),'selection_statement':([0,1,33,52,],[5,5,5,5,]),'iteration_statement':([0,1,33,52,],[6,6,6,6,]),'declaration_expression':([0,1,14,33,52,],[7,7,35,7,7,]),'input_expression':([0,1,33,34,52,],[8,8,8,54,8,]),'output_expression':([0,1,33,52,],[9,9,9,9,]),'assignment_expression':([0,1,14,33,52,],[13,13,13,13,13,]),'type_specifier':([0,1,14,33,52,],[14,14,14,14,14,]),'variable_expression':([0,1,14,30,33,34,52,59,62,65,70,],[16,16,16,44,16,44,16,44,44,44,44,]),'conditional_expression':([10,11,51,57,],[29,31,75,79,]),'block_statement_list':([12,25,29,31,],[32,37,38,50,]),'logical_expression':([30,34,],[39,53,]),'equality_expression':([30,34,59,],[40,40,80,]),'relational_expression':([30,34,59,62,],[41,41,41,81,]),'math_expression':([30,34,59,62,65,],[42,42,42,42,82,]),'primary_expression':([30,34,59,62,65,70,],[43,43,43,43,43,83,]),'boolean_expression':([30,34,59,62,65,70,],[47,47,47,47,47,47,]),'logical_operators':([39,53,],[59,59,]),'equality_operators':([40,80,],[62,62,]),'relational_operators':([41,81,],[65,65,]),'math_operators':([42,82,],[70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> empty','statement_list',1,'p_statement_list_1','parser.py',11),
  ('statement_list -> statement','statement_list',1,'p_statement_list_2','parser.py',15),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_3','parser.py',19),
  ('statement -> expression_statement','statement',1,'p_statement','parser.py',25),
  ('statement -> selection_statement','statement',1,'p_statement','parser.py',26),
  ('statement -> iteration_statement','statement',1,'p_statement','parser.py',27),
  ('expression_statement -> declaration_expression SEMI','expression_statement',2,'p_expression_statement_1','parser.py',33),
  ('expression_statement -> empty SEMI','expression_statement',2,'p_expression_statement_2','parser.py',37),
  ('expression_statement -> input_expression SEMI','expression_statement',2,'p_expression_statement_3','parser.py',41),
  ('expression_statement -> output_expression SEMI','expression_statement',2,'p_expression_statement_4','parser.py',45),
  ('declaration_expression -> assignment_expression','declaration_expression',1,'p_declaration_expression_1','parser.py',50),
  ('declaration_expression -> type_specifier declaration_expression','declaration_expression',2,'p_declaration_expression_2','parser.py',54),
  ('selection_statement -> IF conditional_expression block_statement_list','selection_statement',3,'p_selection_statement_1','parser.py',59),
  ('selection_statement -> selection_statement ELSE block_statement_list','selection_statement',3,'p_selection_statement_2','parser.py',63),
  ('iteration_statement -> WHILE conditional_expression block_statement_list','iteration_statement',3,'p_iteration_statement_1','parser.py',68),
  ('iteration_statement -> DO block_statement_list WHILE conditional_expression','iteration_statement',4,'p_iteration_statement_2','parser.py',72),
  ('block_statement_list -> LBRACE statement_list RBRACE','block_statement_list',3,'p_block_statement_list_1','parser.py',77),
  ('conditional_expression -> LPAREN logical_expression RPAREN','conditional_expression',3,'p_conditional_expression_1','parser.py',82),
  ('assignment_expression -> variable_expression','assignment_expression',1,'p_assignment_expression_1','parser.py',87),
  ('assignment_expression -> assignment_expression EQUALS logical_expression','assignment_expression',3,'p_assignment_expression_2','parser.py',91),
  ('assignment_expression -> assignment_expression EQUALS input_expression','assignment_expression',3,'p_assignment_expression_3','parser.py',95),
  ('logical_expression -> equality_expression','logical_expression',1,'p_logical_expression_1','parser.py',100),
  ('logical_expression -> logical_expression logical_operators equality_expression','logical_expression',3,'p_logical_expression_2','parser.py',104),
  ('equality_expression -> relational_expression','equality_expression',1,'p_equality_expression_1','parser.py',109),
  ('equality_expression -> equality_expression equality_operators relational_expression','equality_expression',3,'p_equality_expression_2','parser.py',113),
  ('relational_expression -> math_expression','relational_expression',1,'p_relational_expression_1','parser.py',118),
  ('relational_expression -> relational_expression relational_operators math_expression','relational_expression',3,'p_relational_expression_2','parser.py',122),
  ('math_expression -> primary_expression','math_expression',1,'p_math_expression_1','parser.py',127),
  ('math_expression -> math_expression math_operators primary_expression','math_expression',3,'p_math_expression_2','parser.py',131),
  ('input_expression -> CONSOLE DOT READLINE LPAREN RPAREN','input_expression',5,'p_input_expression','parser.py',136),
  ('output_expression -> CONSOLE DOT WRITELINE conditional_expression','output_expression',4,'p_output_expression','parser.py',141),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',147),
  ('type_specifier -> BOOL','type_specifier',1,'p_type_specifier','parser.py',148),
  ('type_specifier -> STRING','type_specifier',1,'p_type_specifier','parser.py',149),
  ('logical_operators -> LAND','logical_operators',1,'p_logical_operators','parser.py',155),
  ('logical_operators -> LOR','logical_operators',1,'p_logical_operators','parser.py',156),
  ('equality_operators -> EQ','equality_operators',1,'p_equality_operators','parser.py',162),
  ('equality_operators -> NE','equality_operators',1,'p_equality_operators','parser.py',163),
  ('relational_operators -> LT','relational_operators',1,'p_relational_operators','parser.py',169),
  ('relational_operators -> GT','relational_operators',1,'p_relational_operators','parser.py',170),
  ('relational_operators -> LE','relational_operators',1,'p_relational_operators','parser.py',171),
  ('relational_operators -> GE','relational_operators',1,'p_relational_operators','parser.py',172),
  ('math_operators -> PLUS','math_operators',1,'p_math_operators','parser.py',178),
  ('math_operators -> MINUS','math_operators',1,'p_math_operators','parser.py',179),
  ('math_operators -> TIMES','math_operators',1,'p_math_operators','parser.py',180),
  ('math_operators -> DIVIDE','math_operators',1,'p_math_operators','parser.py',181),
  ('primary_expression -> variable_expression','primary_expression',1,'p_primary_expression','parser.py',187),
  ('primary_expression -> DIGIT','primary_expression',1,'p_primary_expression','parser.py',188),
  ('primary_expression -> STRING_SENTENCE','primary_expression',1,'p_primary_expression','parser.py',189),
  ('primary_expression -> boolean_expression','primary_expression',1,'p_primary_expression','parser.py',190),
  ('variable_expression -> ID','variable_expression',1,'p_variable_expression','parser.py',196),
  ('variable_expression -> CONSTANT','variable_expression',1,'p_variable_expression','parser.py',197),
  ('boolean_expression -> TRUE','boolean_expression',1,'p_boolean_expression','parser.py',203),
  ('boolean_expression -> FALSE','boolean_expression',1,'p_boolean_expression','parser.py',204),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',209),
]
