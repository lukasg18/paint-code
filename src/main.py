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
      input('\nPress enter to exit\n')
    else:
      rpl()
    
    return 0

if __name__ == '__main__':
    main()