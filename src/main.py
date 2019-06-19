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


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="input file")
    args = parser.parse_args() 
    
    if args.file:
      file = open(args.file, 'r')
      for line in file:
        print("line: " + line)
    else:
      rpl()
    
    return 0

if __name__ == '__main__':
    main()