from lark import Lark, Tree
import turtle

class MEL():
    def __init__(self):
        self._grammar = Lark(open('grammar/grammar.lark'))
    
    def parser(self, expression):
        grammar_parse = self._grammar
        try:
            parse_tree = grammar_parse.parse(expression)
            for inst in parse_tree.children:
                self.run_instruction(inst)
            print("expressao aceita: ", parse_tree) 
        except Exception as e:
            print(e)

    def run_instruction(self, t):
        if t.data == 'action':
            for inst in t.children:
                self.run_action(inst)

        elif t.data == 'code_block':
            for inst in t.children:
                self.run_code_block(inst)
        
        elif t.data == 'loop':
            for inst in t.children:
                self.run_loop(inst)

        elif t.data == 'clear':
            for inst in t.children:
                self.run_clear(inst)

        elif t.data == 'function':
            for inst in t.children:
                self.run_function(inst)

        elif t.data == 'assign':
            for inst in t.children:
                self.run_assign(inst)
    
    def run_action(self, t):
        if t.data == 'movement':
            print("func movement")
        
        elif t.data == 'custom_color':
            for inst in t.children:
                self.run_custom_color(inst)
        
        elif t.data == 'custom_background':
            for inst in t.children:
                self.run_custom_background(inst)
        
    def run_code_block(self, t):
        print("func code_block")
        for inst in t.children:
            self.run_instruction(inst)
    
    def run_loop(self, t):
        print("func run_loop")
        for i in range(len(t.children)):
            ident_loop, count, block = t.children[i].children
            for i in range(int(count)):
                self.run_instruction(block)

    def run_clear(self, t):
        print("func clear")
    
    def run_function(self, t):
        print("func function")
        self.run_code_block(t)

    def run_assign(self, t):
        if t.data == 'custom_color':
            print("func custom_color")
        
        elif t.data == 'lambda':
            print("func lambda")

        else:
            print("number")
    
    def run_custom_color(self, t):
        for inst in t.children:
            if isinstance(inst, Tree) and inst.data == 'rgb':
                print("func rgb")
            else:
                print("color")
    
    def run_custom_background(self, t):
        for inst in t.children:
            if isinstance(inst, Tree) and inst.data == 'rgb':
                print("func rgb")
            else:
                print("color")