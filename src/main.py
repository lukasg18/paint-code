from mel import MEL

try:
    input = raw_input
except NameError:
    pass

def main():
    while True:
        # ignorando espacos
        expr: str = input('insira a expressao -> ')
        if len(expr) == 0:
            print("Favor inserir uma expressao")
        else:
            MEL().parser(expr)

if __name__ == '__main__':
    main()