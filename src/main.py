from mel import MEL
import argparse


try:
    input = raw_input
except NameError:
    pass

def rpl():
    while True:
        # ignorando espacos
        expr: str = input('insira a expressao -> ')
        if len(expr) == 0:
            print("Favor inserir uma expressao")
        else:
            MEL().parser(expr)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="input file")
    args = parser.parse_args() 
    
    if args.file:
        print("Abrir arquivo e executar no Lark")
    else:
        rpl()
    
    return 0

if __name__ == '__main__':
    main()