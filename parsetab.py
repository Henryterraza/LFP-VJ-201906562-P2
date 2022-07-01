
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CODIGOleftoper_orleftoper_andleftoper_igualacionoper_diferenciacionleftoper_menoroper_mayoroper_menor_igualoper_mayor_igualleftoper_sumaoper_restaleftoper_multiplicacionoper_divisionoper_restoleftoper_notasignacion cadena char coma decimal entero identificador llave_a llave_b oper_and oper_diferenciacion oper_division oper_igualacion oper_mayor oper_mayor_igual oper_menor oper_menor_igual oper_multiplicacion oper_not oper_or oper_resta oper_resto oper_suma par_a par_b private_boolean private_break private_char private_continue private_do private_double private_else private_false private_if private_int private_return private_string private_true private_void private_while ptcoma\n  CODIGO : CONTENIDO \n  \n  CONTENIDO : CONTENIDO INSTRUCCIONES\n            | INSTRUCCIONES\n  \n  INSTRUCCIONES : DEC_VAR\n                | ASIG_VAR\n                | EST_CONDICIONALES\n                | EST_ITERATIVAS       \n                | SENT_CFLUJO\n                | DEC_METODOS\n                | DEC_FUNCIONES\n                | RETORNO\n                | LLAMADA\n  \n  DEC_VAR : TIPO_DATO identificador asignacion DATO ptcoma\n  \n  TIPO_DATO : private_int\n            | private_double\n            | private_string\n            | private_char\n            | private_boolean\n  \n  DATO : entero\n        | decimal\n        | cadena\n        | char\n        | private_true\n        | private_false\n  \n  ASIG_VAR : identificador asignacion DATO ptcoma\n  \n  EST_CONDICIONALES : private_if par_a OPERACION par_b llave_a INSTRUCCIONS llave_b\n                    | private_if par_a OPERACION par_b llave_a INSTRUCCIONS llave_b private_else llave_a INSTRUCCIONS llave_b\n  \n  OPERACION : OPERACION E\n            | E\n  \n  E : E oper_suma E\n    | E oper_resta E\n    | E oper_multiplicacion E\n    | E oper_division E\n    | E oper_resto E\n    | E oper_igualacion E\n    | E oper_diferenciacion E\n    | E oper_mayor E\n    | E oper_mayor_igual E\n    | E oper_menor E\n    | E oper_menor_igual E\n    | E oper_and E\n    | E oper_or E\n    | oper_not E\n    | identificador\n    | entero\n    | private_false\n    | private_true\n  \n  INSTRUCCIONS : INSTRUCCIONS INSTRUCCIONES2\n            | INSTRUCCIONES2\n  \n  INSTRUCCIONES2 : DEC_VAR\n                | ASIG_VAR\n                | EST_CONDICIONALES\n                | EST_ITERATIVAS       \n                | SENT_CFLUJO\n                | RETORNO\n                | LLAMADA\n  \n  EST_ITERATIVAS : private_while par_a OPERACION par_b llave_a INSTRUCCIONS llave_b\n                    | private_do llave_a INSTRUCCIONS llave_b private_while par_a OPERACION par_b ptcoma\n  \n  SENT_CFLUJO : private_break ptcoma\n              | private_continue ptcoma\n  \n  DEC_METODOS : private_void identificador par_a PARAMETROS par_b llave_a INSTRUCCIONS llave_b\n              | private_void identificador par_a par_b llave_a INSTRUCCIONS llave_b\n  \n  PARAMETROS : PARAMETROS coma TIPO_DATO identificador\n              | TIPO_DATO identificador\n  \n  DEC_FUNCIONES : TIPO_DATO identificador par_a PARAMETROS par_b llave_a INSTRUCCIONS llave_b\n                | TIPO_DATO identificador par_a par_b llave_a INSTRUCCIONS llave_b\n  \n  RETORNO : private_return ptcoma\n          | private_return DATO ptcoma\n  \n  LLAMADA : identificador par_a ARGUMENTOS par_b \n          | identificador par_a par_b\n  \n  ARGUMENTOS : ARGUMENTOS coma DATO\n              | DATO\n  '
    
_lr_action_items = {'identificador':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,22,23,24,25,26,27,31,32,33,34,35,37,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,72,75,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,100,104,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,143,144,145,146,147,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,28,36,-14,-15,-16,-17,-18,-2,54,54,14,-59,-60,-67,-70,54,-29,54,-44,-45,-46,-47,54,14,-49,-50,-51,-52,-53,-54,-55,-56,97,-68,101,-25,-69,-28,54,54,54,54,54,54,54,54,54,54,54,54,54,-43,-48,-13,14,14,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,14,14,14,133,14,14,14,54,14,14,14,-66,-26,-57,54,14,-62,-65,-61,14,-58,14,-27,]),'private_if':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,15,-59,-60,-67,-70,15,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,15,15,15,15,15,15,15,15,15,15,15,-66,-26,-57,15,-62,-65,-61,15,-58,15,-27,]),'private_while':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,95,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,16,-59,-60,-67,-70,16,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,121,-48,-13,16,16,16,16,16,16,16,16,16,16,16,-66,-26,-57,16,-62,-65,-61,16,-58,16,-27,]),'private_do':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,17,-59,-60,-67,-70,17,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,17,17,17,17,17,17,17,17,17,17,17,-66,-26,-57,17,-62,-65,-61,17,-58,17,-27,]),'private_break':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,18,-59,-60,-67,-70,18,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,18,18,18,18,18,18,18,18,18,18,18,-66,-26,-57,18,-62,-65,-61,18,-58,18,-27,]),'private_continue':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,19,-59,-60,-67,-70,19,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,19,19,19,19,19,19,19,19,19,19,19,-66,-26,-57,19,-62,-65,-61,19,-58,19,-27,]),'private_void':([0,2,3,4,5,6,7,8,9,10,11,12,27,34,35,37,49,70,75,76,100,134,135,136,139,140,143,145,147,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-59,-60,-67,-70,-68,-25,-69,-13,-66,-26,-57,-62,-65,-61,-58,-27,]),'private_return':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,21,-59,-60,-67,-70,21,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,21,21,21,21,21,21,21,21,21,21,21,-66,-26,-57,21,-62,-65,-61,21,-58,21,-27,]),'private_int':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,46,49,59,60,61,62,63,64,65,66,67,69,70,75,76,96,100,103,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,22,-59,-60,-67,22,-70,22,-49,-50,-51,-52,-53,-54,-55,-56,22,-68,-25,-69,-48,-13,22,22,22,22,22,22,22,22,22,22,22,22,-66,-26,-57,22,-62,-65,-61,22,-58,22,-27,]),'private_double':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,46,49,59,60,61,62,63,64,65,66,67,69,70,75,76,96,100,103,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,23,-59,-60,-67,23,-70,23,-49,-50,-51,-52,-53,-54,-55,-56,23,-68,-25,-69,-48,-13,23,23,23,23,23,23,23,23,23,23,23,23,-66,-26,-57,23,-62,-65,-61,23,-58,23,-27,]),'private_string':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,46,49,59,60,61,62,63,64,65,66,67,69,70,75,76,96,100,103,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,24,-59,-60,-67,24,-70,24,-49,-50,-51,-52,-53,-54,-55,-56,24,-68,-25,-69,-48,-13,24,24,24,24,24,24,24,24,24,24,24,24,-66,-26,-57,24,-62,-65,-61,24,-58,24,-27,]),'private_char':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,46,49,59,60,61,62,63,64,65,66,67,69,70,75,76,96,100,103,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,25,-59,-60,-67,25,-70,25,-49,-50,-51,-52,-53,-54,-55,-56,25,-68,-25,-69,-48,-13,25,25,25,25,25,25,25,25,25,25,25,25,-66,-26,-57,25,-62,-65,-61,25,-58,25,-27,]),'private_boolean':([0,2,3,4,5,6,7,8,9,10,11,12,27,33,34,35,37,46,49,59,60,61,62,63,64,65,66,67,69,70,75,76,96,100,103,104,106,120,123,124,126,127,128,130,131,132,134,135,136,138,139,140,143,144,145,146,147,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,26,-59,-60,-67,26,-70,26,-49,-50,-51,-52,-53,-54,-55,-56,26,-68,-25,-69,-48,-13,26,26,26,26,26,26,26,26,26,26,26,26,-66,-26,-57,26,-62,-65,-61,26,-58,26,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,27,34,35,37,49,70,75,76,100,134,135,136,139,140,143,145,147,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-59,-60,-67,-70,-68,-25,-69,-13,-66,-26,-57,-62,-65,-61,-58,-27,]),'asignacion':([14,28,97,],[29,45,45,]),'par_a':([14,15,16,28,36,121,],[30,31,32,46,69,129,]),'llave_a':([17,74,78,94,99,102,122,141,],[33,104,106,120,123,124,130,144,]),'ptcoma':([18,19,21,38,39,40,41,42,43,44,47,71,142,],[34,35,37,70,-19,-20,-21,-22,-23,-24,75,100,145,]),'entero':([21,29,30,31,32,45,51,52,53,54,55,56,57,58,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,107,108,109,110,111,112,113,114,115,116,117,118,119,129,137,],[39,39,39,55,55,39,55,-29,55,-44,-45,-46,-47,55,39,-28,55,55,55,55,55,55,55,55,55,55,55,55,55,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,55,55,]),'decimal':([21,29,30,45,77,],[40,40,40,40,40,]),'cadena':([21,29,30,45,77,],[41,41,41,41,41,]),'char':([21,29,30,45,77,],[42,42,42,42,42,]),'private_true':([21,29,30,31,32,45,51,52,53,54,55,56,57,58,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,107,108,109,110,111,112,113,114,115,116,117,118,119,129,137,],[43,43,43,57,57,43,57,-29,57,-44,-45,-46,-47,57,43,-28,57,57,57,57,57,57,57,57,57,57,57,57,57,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,57,57,]),'private_false':([21,29,30,31,32,45,51,52,53,54,55,56,57,58,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,107,108,109,110,111,112,113,114,115,116,117,118,119,129,137,],[44,44,44,56,56,44,56,-29,56,-44,-45,-46,-47,56,44,-28,56,56,56,56,56,56,56,56,56,56,56,56,56,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,56,56,]),'par_b':([30,39,40,41,42,43,44,46,48,50,51,52,54,55,56,57,58,69,73,79,93,98,101,105,107,108,109,110,111,112,113,114,115,116,117,118,119,133,137,],[49,-19,-20,-21,-22,-23,-24,74,76,-72,78,-29,-44,-45,-46,-47,94,99,102,-28,-43,122,-64,-71,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-63,142,]),'oper_not':([31,32,51,52,53,54,55,56,57,58,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,107,108,109,110,111,112,113,114,115,116,117,118,119,129,137,],[53,53,53,-29,53,-44,-45,-46,-47,53,-28,53,53,53,53,53,53,53,53,53,53,53,53,53,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,53,53,]),'llave_b':([34,35,37,49,59,60,61,62,63,64,65,66,67,70,75,76,96,100,126,127,128,131,132,135,136,138,145,146,147,],[-59,-60,-67,-70,95,-49,-50,-51,-52,-53,-54,-55,-56,-68,-25,-69,-48,-13,134,135,136,139,140,-26,-57,143,-58,147,-27,]),'coma':([39,40,41,42,43,44,48,50,73,98,101,105,133,],[-19,-20,-21,-22,-23,-24,77,-72,103,103,-64,-71,-63,]),'oper_suma':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[80,-44,-45,-46,-47,80,-43,-30,-31,-32,-33,-34,80,80,80,80,80,80,80,80,]),'oper_resta':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[81,-44,-45,-46,-47,81,-43,-30,-31,-32,-33,-34,81,81,81,81,81,81,81,81,]),'oper_multiplicacion':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[82,-44,-45,-46,-47,82,-43,82,82,-32,-33,-34,82,82,82,82,82,82,82,82,]),'oper_division':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[83,-44,-45,-46,-47,83,-43,83,83,-32,-33,-34,83,83,83,83,83,83,83,83,]),'oper_resto':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[84,-44,-45,-46,-47,84,-43,84,84,-32,-33,-34,84,84,84,84,84,84,84,84,]),'oper_igualacion':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[85,-44,-45,-46,-47,85,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,85,85,]),'oper_diferenciacion':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[86,-44,-45,-46,-47,86,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,86,86,]),'oper_mayor':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[87,-44,-45,-46,-47,87,-43,-30,-31,-32,-33,-34,87,87,-37,-38,-39,-40,87,87,]),'oper_mayor_igual':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[88,-44,-45,-46,-47,88,-43,-30,-31,-32,-33,-34,88,88,-37,-38,-39,-40,88,88,]),'oper_menor':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[89,-44,-45,-46,-47,89,-43,-30,-31,-32,-33,-34,89,89,-37,-38,-39,-40,89,89,]),'oper_menor_igual':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[90,-44,-45,-46,-47,90,-43,-30,-31,-32,-33,-34,90,90,-37,-38,-39,-40,90,90,]),'oper_and':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[91,-44,-45,-46,-47,91,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,91,]),'oper_or':([52,54,55,56,57,79,93,107,108,109,110,111,112,113,114,115,116,117,118,119,],[92,-44,-45,-46,-47,92,-43,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,]),'private_else':([135,],[141,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'CODIGO':([0,],[1,]),'CONTENIDO':([0,],[2,]),'INSTRUCCIONES':([0,2,],[3,27,]),'DEC_VAR':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[4,4,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'ASIG_VAR':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[5,5,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'EST_CONDICIONALES':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[6,6,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'EST_ITERATIVAS':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[7,7,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'SENT_CFLUJO':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[8,8,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'DEC_METODOS':([0,2,],[9,9,]),'DEC_FUNCIONES':([0,2,],[10,10,]),'RETORNO':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[11,11,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'LLAMADA':([0,2,33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[12,12,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'TIPO_DATO':([0,2,33,46,59,69,103,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[13,13,68,72,68,72,125,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'DATO':([21,29,30,45,77,],[38,47,50,71,105,]),'ARGUMENTOS':([30,],[48,]),'OPERACION':([31,32,129,],[51,58,137,]),'E':([31,32,51,53,58,80,81,82,83,84,85,86,87,88,89,90,91,92,129,137,],[52,52,79,93,79,107,108,109,110,111,112,113,114,115,116,117,118,119,52,79,]),'INSTRUCCIONS':([33,104,106,120,123,124,130,144,],[59,126,127,128,131,132,138,146,]),'INSTRUCCIONES2':([33,59,104,106,120,123,124,126,127,128,130,131,132,138,144,146,],[60,96,60,60,60,60,60,96,96,96,60,96,96,96,60,96,]),'PARAMETROS':([46,69,],[73,98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> CODIGO","S'",1,None,None,None),
  ('CODIGO -> CONTENIDO','CODIGO',1,'p_CODIGO','A_lexico.py',163),
  ('CONTENIDO -> CONTENIDO INSTRUCCIONES','CONTENIDO',2,'p_CONTENIDO','A_lexico.py',169),
  ('CONTENIDO -> INSTRUCCIONES','CONTENIDO',1,'p_CONTENIDO','A_lexico.py',170),
  ('INSTRUCCIONES -> DEC_VAR','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',182),
  ('INSTRUCCIONES -> ASIG_VAR','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',183),
  ('INSTRUCCIONES -> EST_CONDICIONALES','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',184),
  ('INSTRUCCIONES -> EST_ITERATIVAS','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',185),
  ('INSTRUCCIONES -> SENT_CFLUJO','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',186),
  ('INSTRUCCIONES -> DEC_METODOS','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',187),
  ('INSTRUCCIONES -> DEC_FUNCIONES','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',188),
  ('INSTRUCCIONES -> RETORNO','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',189),
  ('INSTRUCCIONES -> LLAMADA','INSTRUCCIONES',1,'p_INSTRUCCIONES','A_lexico.py',190),
  ('DEC_VAR -> TIPO_DATO identificador asignacion DATO ptcoma','DEC_VAR',5,'p_DEC_VAR','A_lexico.py',196),
  ('TIPO_DATO -> private_int','TIPO_DATO',1,'p_TIPO_DATO','A_lexico.py',203),
  ('TIPO_DATO -> private_double','TIPO_DATO',1,'p_TIPO_DATO','A_lexico.py',204),
  ('TIPO_DATO -> private_string','TIPO_DATO',1,'p_TIPO_DATO','A_lexico.py',205),
  ('TIPO_DATO -> private_char','TIPO_DATO',1,'p_TIPO_DATO','A_lexico.py',206),
  ('TIPO_DATO -> private_boolean','TIPO_DATO',1,'p_TIPO_DATO','A_lexico.py',207),
  ('DATO -> entero','DATO',1,'p_DATO','A_lexico.py',213),
  ('DATO -> decimal','DATO',1,'p_DATO','A_lexico.py',214),
  ('DATO -> cadena','DATO',1,'p_DATO','A_lexico.py',215),
  ('DATO -> char','DATO',1,'p_DATO','A_lexico.py',216),
  ('DATO -> private_true','DATO',1,'p_DATO','A_lexico.py',217),
  ('DATO -> private_false','DATO',1,'p_DATO','A_lexico.py',218),
  ('ASIG_VAR -> identificador asignacion DATO ptcoma','ASIG_VAR',4,'p_ASIG_VAR','A_lexico.py',225),
  ('EST_CONDICIONALES -> private_if par_a OPERACION par_b llave_a INSTRUCCIONS llave_b','EST_CONDICIONALES',7,'p_EST_CONDICIONALES','A_lexico.py',232),
  ('EST_CONDICIONALES -> private_if par_a OPERACION par_b llave_a INSTRUCCIONS llave_b private_else llave_a INSTRUCCIONS llave_b','EST_CONDICIONALES',11,'p_EST_CONDICIONALES','A_lexico.py',233),
  ('OPERACION -> OPERACION E','OPERACION',2,'p_OPERACION','A_lexico.py',246),
  ('OPERACION -> E','OPERACION',1,'p_OPERACION','A_lexico.py',247),
  ('E -> E oper_suma E','E',3,'p_E','A_lexico.py',257),
  ('E -> E oper_resta E','E',3,'p_E','A_lexico.py',258),
  ('E -> E oper_multiplicacion E','E',3,'p_E','A_lexico.py',259),
  ('E -> E oper_division E','E',3,'p_E','A_lexico.py',260),
  ('E -> E oper_resto E','E',3,'p_E','A_lexico.py',261),
  ('E -> E oper_igualacion E','E',3,'p_E','A_lexico.py',262),
  ('E -> E oper_diferenciacion E','E',3,'p_E','A_lexico.py',263),
  ('E -> E oper_mayor E','E',3,'p_E','A_lexico.py',264),
  ('E -> E oper_mayor_igual E','E',3,'p_E','A_lexico.py',265),
  ('E -> E oper_menor E','E',3,'p_E','A_lexico.py',266),
  ('E -> E oper_menor_igual E','E',3,'p_E','A_lexico.py',267),
  ('E -> E oper_and E','E',3,'p_E','A_lexico.py',268),
  ('E -> E oper_or E','E',3,'p_E','A_lexico.py',269),
  ('E -> oper_not E','E',2,'p_E','A_lexico.py',270),
  ('E -> identificador','E',1,'p_E','A_lexico.py',271),
  ('E -> entero','E',1,'p_E','A_lexico.py',272),
  ('E -> private_false','E',1,'p_E','A_lexico.py',273),
  ('E -> private_true','E',1,'p_E','A_lexico.py',274),
  ('INSTRUCCIONS -> INSTRUCCIONS INSTRUCCIONES2','INSTRUCCIONS',2,'p_INSTRUCCIONS','A_lexico.py',285),
  ('INSTRUCCIONS -> INSTRUCCIONES2','INSTRUCCIONS',1,'p_INSTRUCCIONS','A_lexico.py',286),
  ('INSTRUCCIONES2 -> DEC_VAR','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',298),
  ('INSTRUCCIONES2 -> ASIG_VAR','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',299),
  ('INSTRUCCIONES2 -> EST_CONDICIONALES','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',300),
  ('INSTRUCCIONES2 -> EST_ITERATIVAS','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',301),
  ('INSTRUCCIONES2 -> SENT_CFLUJO','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',302),
  ('INSTRUCCIONES2 -> RETORNO','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',303),
  ('INSTRUCCIONES2 -> LLAMADA','INSTRUCCIONES2',1,'p_INSTRUCCIONES2','A_lexico.py',304),
  ('EST_ITERATIVAS -> private_while par_a OPERACION par_b llave_a INSTRUCCIONS llave_b','EST_ITERATIVAS',7,'p_EST_ITERATIVAS','A_lexico.py',313),
  ('EST_ITERATIVAS -> private_do llave_a INSTRUCCIONS llave_b private_while par_a OPERACION par_b ptcoma','EST_ITERATIVAS',9,'p_EST_ITERATIVAS','A_lexico.py',314),
  ('SENT_CFLUJO -> private_break ptcoma','SENT_CFLUJO',2,'p_SENT_CFLUJO','A_lexico.py',326),
  ('SENT_CFLUJO -> private_continue ptcoma','SENT_CFLUJO',2,'p_SENT_CFLUJO','A_lexico.py',327),
  ('DEC_METODOS -> private_void identificador par_a PARAMETROS par_b llave_a INSTRUCCIONS llave_b','DEC_METODOS',8,'p_DEC_METODOS','A_lexico.py',333),
  ('DEC_METODOS -> private_void identificador par_a par_b llave_a INSTRUCCIONS llave_b','DEC_METODOS',7,'p_DEC_METODOS','A_lexico.py',334),
  ('PARAMETROS -> PARAMETROS coma TIPO_DATO identificador','PARAMETROS',4,'p_PARAMETROS','A_lexico.py',347),
  ('PARAMETROS -> TIPO_DATO identificador','PARAMETROS',2,'p_PARAMETROS','A_lexico.py',348),
  ('DEC_FUNCIONES -> TIPO_DATO identificador par_a PARAMETROS par_b llave_a INSTRUCCIONS llave_b','DEC_FUNCIONES',8,'p_DEC_FUNCIONES','A_lexico.py',360),
  ('DEC_FUNCIONES -> TIPO_DATO identificador par_a par_b llave_a INSTRUCCIONS llave_b','DEC_FUNCIONES',7,'p_DEC_FUNCIONES','A_lexico.py',361),
  ('RETORNO -> private_return ptcoma','RETORNO',2,'p_RETORNO','A_lexico.py',376),
  ('RETORNO -> private_return DATO ptcoma','RETORNO',3,'p_RETORNO','A_lexico.py',377),
  ('LLAMADA -> identificador par_a ARGUMENTOS par_b','LLAMADA',4,'p_LLAMADA','A_lexico.py',390),
  ('LLAMADA -> identificador par_a par_b','LLAMADA',3,'p_LLAMADA','A_lexico.py',391),
  ('ARGUMENTOS -> ARGUMENTOS coma DATO','ARGUMENTOS',3,'p_ARGUMENTOS','A_lexico.py',404),
  ('ARGUMENTOS -> DATO','ARGUMENTOS',1,'p_ARGUMENTOS','A_lexico.py',405),
]