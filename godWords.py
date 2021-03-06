from lark import Lark

my_grammar = """
?start: phrase_list

phrase_list: phrase+

?phrase: assignment
            | if_phrase
            | else_phrase
            | while_phrase
            | print_phrase
            | add_phrase
            | sub_phrase
            | continue_phrase

assignment: "I define" var "to be" expression "."

var: NAME

if_phrase: "Oschon says: if" expression ", then," phrase_list "Thal says end."
else_phrase: "Oschon then says: if not," phrase_list "Thal says end."
while_phrase: "Nal says: while" expression "," phrase_list "Thal says end."
print_phrase: "I declare" expression "."
add_phrase: "I add" expression "to" var "."
sub_phrase: "I remove" expression "from" var "." 
continue_phrase: "Also," phrase_list


?expression: var
            |literal
            |expression "is greater than" expression -> gt
            |expression "is less than" expression -> lt
            |expression "is greater or equal to" expression -> ge
            |expression "is less or equal to" expression -> le
            |expression "is identical to" expression -> eq
            |expression "is not identical to" expression -> nq
literal: NUMBER



%import common.CNAME -> NAME
%import common.WS
%import common.INT -> NUMBER 
%ignore WS
"""

def translate(t):

  if t.data == 'phrase_list':
    return '\n'.join(map(translate, t.children))
  
  elif t.data == 'if_phrase':
    condition, block = t.children
    return 'if' + ' (' + translate(condition) + '): \n '+ translate(block) + '\n'
  
  elif t.data == 'else_phrase':
    block = t.children[0]
    return 'else:' + '\n ' + translate(block) + '\n'

  elif t.data == 'while_phrase':
    condition, block = t.children
    return 'while'+' (' + translate(condition) + '): \n ' + translate(block) + '\n'
  
  elif t.data == 'continue_phrase':
    phrase = t.children[0]
    return ' '+translate(phrase)

  elif t.data == 'print_phrase':
    exp = t.children[0]
    return 'print(' + translate(exp) + ')'
  
  elif t.data == 'add_phrase':
    exp, var = t.children
    return translate(var) + '=' + translate(var) + '+' + translate(exp)
  
  elif t.data == 'sub_phrase':
    exp, var = t.children
    return translate(var) + '=' + translate(var) + '-' + translate(exp)
  
  elif t.data == 'var':
    return t.children[0]
  
  elif t.data == 'literal':
    return t.children[0]
  
  elif t.data == 'gt':
    lhs, rhs = t.children
    return translate(lhs) + ' > ' + translate(rhs)
  
  elif t.data == 'lt':
    lhs,rhs = t.children
    return translate(lhs) + ' < ' + translate(rhs)
  
  elif t.data == 'ge':
    lhs,rhs = t.children
    return translate(lhs) + '>=' + translate(rhs)
  
  elif t.data == 'le':
    lhs,rhs = t.children
    return translate(lhs) + '<=' + translate(rhs)
  
  elif t.data  == 'eq':
    lhs,rhs = t.children
    return translate(lhs) + '==' + translate(rhs)
  
  elif t.data == 'nq':
    lhs,rhs = t.children
    return translate(lhs) + '!=' +translate(rhs)
  
  elif t.data == 'assignment':
    lhs, rhs = t.children
    return translate(lhs) + ' = ' + translate(rhs)
  
  else:
    raise SyntaxError("bad tree")


parser = Lark(my_grammar)
print("Please input the demo name: ")
fileName = input()
program = open(fileName, "r")
parse_tree = parser.parse(program.read())
print(translate(parse_tree))
#print(parse_tree.pretty())
