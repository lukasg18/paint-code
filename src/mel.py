from lark import Lark

class MEL():
    def __init__(self):
        self._grammar = Lark(open('grammar/grammar.lark'))
    
    def parser(self, expression):
        grammar_parse = self._grammar
        try:
            parse_tree = grammar_parse.parse(expression)
            print("expressao aceita: ", parse_tree) 
        except Exception as e:
            print(e)
