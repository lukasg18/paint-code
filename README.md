# LFA-Parser
Implementação de um parser descendente recursivo para uma Linguagem Livre de Contexto, chamada de MEL.

### Informações gerais
- **Autor**: Lucas Gomes Flegler
- **Linguagem de programação**: Python (versão 3.6.5)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.33.1)

#### Sobre o Lark
Lark é um analisador de gramática livre de contexto. Segundo sua documentação, ele pode analisar qualquer gramática que você lançar nele, não importa o quão complicado ou ambíguo, e fazê-lo de forma eficiente.

### Descrição geral do código fonte
O código fonte está estruturado da seguinte maneira:

```
src
|_ main.py
|_ mel.py
|_ trab2.sh
|_ grammar
   |_ grammar.lark
|_ testes
   |_ testes.txt
```


#### mel.py
É um módulo que contém uma classe única chamada `MEL`, que tem por responsabilidade manipular as expressões matemáticas e encontrar o seu resultado.<br>
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

#### grammar.lark
O método `parser` depois de executado, irá retornar uma árvore contendo o resultado da expressao, seguindo as regras de produção definidas para a gramática que é mostrada logo abaixo.

```html
<expr>   ::= <term> ((‘+’ | ‘-’) <term>)*
<term>   ::= <factor> ((‘*’ | ‘/’ | ‘//’ | ‘%’) <factor>)*
<factor> ::= <base> (‘^’ <factor>)?
<base>   ::= (‘+’ |‘-’) <base>
           | NUMBER
           |  ‘(’ <expr> ‘)’

%import common.SIGNED_NUMBER -> NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
```
Esta gramática se encontra dentro do diretório `grammar` com o nome `grammar.lark`. A extensão de arquivo `.lark` é unica da biblioteca, somente arquivos com esta extensão são analisadas e interpretadas.

#### main.py
É o módulo principal do programa, que tem como objetivo lê a expressão digitada pelo usuário e passar a informação lida para o método `parser`.  Veja o trecho a seguir:

```python
from mel import MEL

try:
    input = raw_input
except NameError:
    pass

def main():
    while True:
        # ignorando espacos
        expr: str = input('> ')
        if len(expr) == 0:
            print("Favor inserir uma expressao")
        else:
            MEL().parser(expr)

if __name__ == '__main__':
    main()
```
Caso a entrada seja vazia, é emitido uma mensagem no console para que tenha pelo menos uma  expressão inserida.

### Como executar?
Para execução do projeto é recomendado utilizar uma máquina virtual do python mas não é obrigatório para o funcionamento do código.<br>
Dentro do diretorio `/src` existe um script básico para execução do programa. O comando abaixo mostra como executar.

```shell
source ./trab2.sh
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

* Entre no diretório "src/"

* Insira o comando para executar o código:
```bash
python main.py
```

### Testes
Para testes, foi criado um arquivo de testes chamado `testes.txt`, que fica dentro do diretório `/src/testes`. Esse arquivo contém algumas expressões que foram usadas para teste da gramática. Dentre eles, temos:
```txt
((2+2)*2)-((2-0)+2)
(10*5)+(100/10)-5+(7%(2^2))
10 * 5 + 100 / 10 - 5 + 7 % 2
(-2.3)^2 + 2.2E1 * 2e1-12 + 1e1+3
(-2.3)^2 + 2.2E1 * 2e1-12 + (1e1+3) % 2
2e5 + 3
(2.*(2.0+2.))-(2.0+(2.-0))
2^2^2^-2
-2^2
-(2^2)
...
```

### Informações adicionais
Todo o código fonte está hospedado no [GitHub](https://github.com/lukasg18/LFA-PARSER-LARK).<br>
Para mais informações a respeito da biblioteca lark, segue abaixo uma imagem resumida sobre funções da biblioteca.<br>
<figure>
<img src="https://raw.githubusercontent.com/lukasg18/lfa-dsl/dev/dsl_images/download.png" width="80%" height="80%" style="display: block; margin-left: auto; margin-right: auto;">
</figure>

#### Referências
https://lark-parser.readthedocs.io/en/latest/

https://github.com/lark-parser/lark/blob/master/README.md