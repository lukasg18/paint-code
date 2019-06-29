from lark import Lark, Tree, tree
import turtle

variables = {}
functions = {}

class PaintCode():
    def __init__(self):
        self._grammar = Lark(open('grammar/new-grammar.lark'))
        # turtle.speed(0)
    
    def _isValidVariable(self, key):
        if (not key in variables.keys()):
            raise Exception('Variable "'+key+'" not defined')
    
    def _isValidFunction(self, key):
        if (not key in functions.keys()):
            raise Exception('Function "'+key+'" not defined')
    
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
            print("functions: ", functions)
        except Exception as e:
            print(e)

    def run_instruction(self, t):
        if t.data == 'action':
            for inst in t.children:
                self.run_action(inst)

        elif t.data == 'assign':
            for inst in t.children:
                self.run_assign(inst)

        elif t.data == 'assign_function':
            for inst in t.children:
                self.run_assign_function(inst)
        
        elif t.data == 'loop':
            for inst in t.children:
                self.run_loop(inst)
        
        elif t.data == 'if':
            for inst in t.children:
                self.run_if(inst)
        
        elif t.data == 'tree':
            for inst in t.children:
                self.run_tree(inst)
    
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

        elif t.data == 'call_function':
            for inst in t.children:
                self.run_call_function(inst)
        
        elif t.data == 'speed':
            for inst in t.children:
                self.run_speed(inst)

    def run_tree(self, t):
        tree.pydot__tree_to_png( t, 'saida.png')

    def run_speed(self, t):
        number = int(t.children[0].value)
        turtle.speed(number)

    def run_assign(self, t):
        name = t.children[0].value
        value = t.children[1].value
        variables[name] = int(value)

    def run_assign_function(self, t):
        name = t.children[0].value
        value = t.children[1:]
        functions[name] = value
    
    def run_fill(self, t):
        for child in t.children:
            if(child.type == 'BEGINFILL'):
                turtle.begin_fill()
            elif(child.type == 'ENDFILL'):
                turtle.end_fill()
    
    def run_call_function(self, t):
        name = t.children[0].value
        self._isValidFunction(name)
        for inst in functions[name]:
            self.run_instruction(inst)

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
    
    def _getValueVarOrNumber(self, val):
        if (isinstance(val, Tree)):
            return variables[val.children[0].value]
        return int(val.value)

    def run_if(self, t):
        val1 = self._getValueVarOrNumber(t.children[0])
        cond = t.children[1].value
        val2 = self._getValueVarOrNumber(t.children[2])
        print("val1: ", val1)
        print("val2: ", val2)
        instructions = t.children[3:]
        canRun = False
        if (cond == '>'):
            canRun = val1 > val2
        elif (cond == '>='):
            canRun = val1 >= val2
        elif (cond == '<'):
            canRun = val1 < val2
        elif (cond == '<='):
            canRun = val1 <= val2
        elif (cond == '=='):
            canRun = val1 == val2
        elif (cond == '!='):
            canRun = val1 != val2
        
        if canRun:
            for inst in instructions:
                self.run_instruction(inst)

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

     
