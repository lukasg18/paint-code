# Trabalho Final de LFA 2019/1 - Implementação de uma Linguagem de Domínio Específico (DSL)

Implementação de uma Linguagem de Domínio Específico (DSL), chamada PaintCode, utilizando a ferramenta voltada para o parse de qualquer gramática livre de contexto chamada Lark.

### Informações gerais
- **Autores**: David P. Vilaça, Lucas Gomes Flegler, Tadeu P. M. Junior
- **Linguagem de programação**: Python (versão 3.6.5)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1)

#### Sobre o Lark
Lark é um analisador de gramática livre de contexto. Segundo sua documentação, ele pode analisar qualquer gramática que você lançar nele, não importa o quão complicado ou ambíguo, e fazê-lo de forma eficiente.

#### Sobre o Turtle
Turtle é um módulo Python que oferece funcionalidades para fazermos desenhos na tela, com comandos muito simples. Esse módulo segue a idéia da linguagem de programação Logo, que é muito utilizada em escolas como apoio ao ensino de disciplinas regulares e também para introdução a programação para crianças. A linguagem Logo segue a ideia de um robô que o usuário pode controlar através de comandos simples de movimentação.

#### PaintCode DSL
Este trabalho consiste na implementação de uma Linguagem de Domínio Específico para trabalhar com o módulo Turtle.
O PaintCode permite o desenvolvedor criar desenhos através de códigos. 

### Descrição geral do código fonte
O código fonte está estruturado da seguinte maneira:

```
src
|_ main.py
|_ paint_code.py
|_ paint_code.sh
|_ grammar
   |_ grammar.lark
|_ testes
   |_ example-circle.pc
   |_ example-frac.pc
   |_ example-frac2.pc
   |_ example-if.pc
   |_ example-square.pc
   |_ example_star.pc

```
#### grammar.lark
O arquivo grammar.lark contém a gramática escrita no formato EBNF, posteriomente interpretada pela biblioteca `Lark`.


```TypeScript
start: instruction

instruction: action                 -> action
            |assign                 -> assign
            |assign_function        -> assign_function
            |loop                   -> loop
            |if                     -> if


            
action: movement                -> movement
        |custom_color           -> custom_color
        |custom_background      -> custom_background
        |clear                  -> clear
        |reset                  -> reset
        |fill                   -> fill
        |call_function          -> call_function
        |speed                  -> speed


speed: "speed" NUMBER
movement: "move" (DIRECTION (NUMBER | variable))+ 
fill: BEGINFILL | ENDFILL  
custom_color: "color" (COLOR | rgb)            
custom_background: "bg" (COLOR | rgb)
rgb: "rgb" (("0".."9")~3 | variable) " " (("0".."9")~3 | variable) " " (("0".."9")~3 | variable)
clear: "clear"
reset: "reset"
assign: "var" NAME "=" NUMBER
assign_function: "def" NAME "{" instruction (";" instruction)* "}"
variable: NAME
call_function: NAME "(" ")"
loop: "repeat" (NUMBER | variable) code_block
code_block: "{" action (";" action)* "}"
if: "if" (NUMBER|variable) CONDITION (NUMBER|variable) "{" instruction (";" instruction)* "}"

COLOR: "red" | "green" | "blue" | "white" | "black"
DIRECTION: "f"|"b"|"l"|"r"
NUMBER: ("0".."9")+
NAME: ("a".."z")+
BEGINFILL: "begin-fill"
ENDFILL: "end-fill"
CONDITION: ">=" | "<=" | "!=" | "==" | ">" | "<"

%import common.WS_INLINE
%ignore WS_INLINE

```
Esta gramática se encontra dentro do diretório `grammar` com o nome `grammar.lark`. A extensão de arquivo `.lark` é unica da biblioteca, somente arquivos com esta extensão são analisadas e interpretadas.


#### paint_code.py
É um módulo que contém uma classe única chamada `paint_code`, com a responsabilidade de manipular as instruções de desenho e .<br>
A seguir apresentarei algumas explicações sobre a funcionalidade da biblioteca.
##### Função Lark
Responsável por analisar e interpretar a gramática livre de contexto desenvolvida. Mostrado no trecho de código abaixo:
```python
self._grammar = Lark(open('grammar/grammar.lark'), start='expr')
```
##### Função Parse
Após a análise feita pela função "lark", a função "parse" retorna uma árvore de análise completa. Veja o trecho abaixo:
```python
def parser(self, expression):
        grammar_parse = self._grammar
        try:
            parse_tree = grammar_parse.parse(expression)
            print("expressao aceita: ", parse_tree) 
        except:
            print("expressao invalida")
```


#### main.py
É o módulo principal do programa, que tem como objetivo lê a expressão digitada ou um arquivo com a extensão `.pc` e posteriomente envia para o arquivo `paint_code.py`. Segue o código abaixo:

```python
from paint_code import PaintCode
import argparse


try:
    input = raw_input
except NameError:
    pass

def rpl():
    while True:
        # ignorando espacos
        expr = input('insira a expressao -> ')
        if len(expr) == 0:
            print("Favor inserir uma expressao")
        else:
            PaintCode().parser(expr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="input file")
    args = parser.parse_args() 
    paintCode = PaintCode()
    
    if args.file:
      file = open(args.file, 'r')
      for line in file:
        paintCode.parser(line.strip())
      input('\nPress any key to exit\n')
    else:
      rpl()
    
    return 0

if __name__ == '__main__':
    main()
```
 


### Como executar?
Para execução do projeto é recomendado utilizar uma máquina virtual do python, mas não é obrigatório para o funcionamento da linguagem.<br>
Dentro do diretório “/src” existe um script básico para execução do programa. O comando abaixo mostra como executar.


```shell
source ./paint_code.sh
```
Caso o script falhe, os comandos a seguir mostram como executar o projeto.

* Insira o comando abaixo para criar uma máquina virtual do python
```bash
virtualenv venv --python=python3
```

* Para ativar a maquina insira o comando:
```bash
source venv/bin/activate
```

* Insira o comando abaixo para instalar a biblioteca do lark-parser
```bash
pip install lark-parser
```


### Testando a linguagem

O código do PaintCode pode ser executado de duas maneiras diferentes, executando o arquivo main.py manualmente(esta opção o programador fica livre para escrever seu código) ou informando um arquivo com a extensão do PaintCode “arquivo.pc”. 

#### Teste manual
Insira o comando abaixo dentro do diretório /src.
```shell 
python main.py
```
* Após executar o comando acima a seguinte mensagem aparcerá no console:
```shell
insira a expressão -> |
 ```  

**OBS:** Para desativar o virtual env:
```bash
   $ deactivate
 ```  
#### Teste com arquivos

Todos os arquivos com extensão “.pc” se encontram no diretório “testes/”. Para executar estes arquivos, insira o comando abaixo:

```shell
python main.py --file testes/example-frac2.pc
 ```  

### Informações adicionais
Todo o código fonte está hospedado no [GitHub](https://github.com/lukasg18/paint-code).<br>

#### Referências
https://lark-parser.readthedocs.io/en/latest/

https://github.com/lark-parser/lark/blob/master/README.md
