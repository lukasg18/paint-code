from lark import Lark

class MEL():
    def __init__(self):
        self._grammar = Lark(open('grammar/grammar.lark'), start='expr')
    
    def parser(self, expression):
        grammar_parse = self._grammar
        try:
            parse_tree = grammar_parse.parse(expression)
            print("expressao aceita: ", parse_tree) 
        except:
            print("expressao invalida")
