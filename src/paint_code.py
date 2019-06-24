from lark import Lark, Tree
import turtle

variables = {}

class PaintCode():
    def __init__(self):
        self._grammar = Lark(open('grammar/new-grammar.lark'))
    
    def _isValidVariable(self, key):
        if (not key in variables.keys()):
            raise Exception('Variable "'+key+'" not defined')
    
    def _getRGB(self, children):
        color = {'r': '', 'g': '', 'b': ''}
        key = 'r'
        pos = 0
        keys = ['r', 'g', 'b']

        for item in children:
            if (isinstance(item, Tree) and item.data == 'variable'):
                keyVar = item.children[0].value
                self._isValidVariable(keyVar)
                color[key] = variables[keyVar]
                if pos < 2:
                    pos += 1
                key = keys[pos]
                
            else:
                color[key] += str(item)
                if (len(color[key]) == 3):
                    if pos < 2:
                        pos += 1
                    key = keys[pos]
        return (int(color['r']), int(color['g']), int(color['b']))
    
    def parser(self, expression):
        grammar_parse = self._grammar
        try:
            parse_tree = grammar_parse.parse(expression)
            for inst in parse_tree.children:
                self.run_instruction(inst)
            print("expressao aceita: ", parse_tree) 
            print("variables: ", variables)
        except Exception as e:
            print(e)

    def run_instruction(self, t):
        if t.data == 'action':
            for inst in t.children:
                self.run_action(inst)

        elif t.data == 'assign':
            for inst in t.children:
                self.run_assign(inst)
        
        elif t.data == 'loop':
            for inst in t.children:
                self.run_loop(inst)
    
    def run_action(self, t):
        if t.data == 'movement':
            for inst in t.children:
                self.run_movement(inst)
        
        elif t.data == 'custom_color':
            for inst in t.children:
                self.run_custom_color(inst)
        
        elif t.data == 'custom_background':
            for inst in t.children:
                self.run_custom_background(inst)

        elif t.data == 'clear':
            turtle.clear()

        elif t.data == 'reset':
            turtle.clear()
            turtle.bgcolor('white')
            turtle.color('black')

        elif t.data == 'fill':
            for inst in t.children:
                self.run_fill(inst)

    def run_assign(self, t):
        name = t.children[0].value
        value = t.children[1].value
        variables[name] = int(value)
    
    def run_fill(self, t):
        for child in t.children:
            if(child.type == 'BEGINFILL'):
                turtle.begin_fill()
            elif(child.type == 'ENDFILL'):
                turtle.end_fill()

    def run_loop(self, t):
        number = 0
        for child in t.children:
            if (isinstance(child, Tree) and child.data == "variable"):
                varKey = child.children[0].value
                self._isValidVariable(varKey)
                number = variables[varKey]
            elif (isinstance(child, Tree) and child.data == "code_block"):
                for i in range(number):
                    self.run_code_block(child)
            elif(child.type == 'NUMBER'):
                number = int(child.value)

    def run_code_block(self, t):
        print(t)
        for child in t.children:
            self.run_action(child)

    def run_movement(self, t):
        aux = { 'f': turtle.fd,
                    'b': turtle.bk,
                    'l': turtle.lt,
                    'r': turtle.rt, }
        for child in t.children:
            if (isinstance(child, Tree) and child.data == "variable"):
                varKey = child.children[0].value
                self._isValidVariable(varKey)
                aux[direction](variables[varKey])
            elif(child.type == 'DIRECTION'):
                direction = child
            else:
                aux[direction](int(child))

    def run_custom_color(self, t):
        # color rgb 000 000 000 
        for inst in t.children:
            if isinstance(inst, Tree) and inst.data == 'rgb':
                turtle.colormode(255)
                r,g,b = self._getRGB(inst.children)
                turtle.pencolor((r, g, b))
            else:
                turtle.color(inst)
    
    def run_custom_background(self, t):
        for inst in t.children:
            if isinstance(inst, Tree) and inst.data == 'rgb':
                turtle.colormode(255)
                r,g,b = self._getRGB(inst.children)
                turtle.bgcolor(r,g,b)
            else:
                turtle.bgcolor(inst)

     
