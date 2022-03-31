import argparse
parser = argparse.ArgumentParser(description="Prueba de argumentos")
parser.add_argument("-a","--arg1", type=str, help="Cualquier str")
parser.add_argument("-b","--arg2", type=int,help="Agregue cualquier número")
args = parser.parse_args()

def pruebas_argparse(arg1, arg2):
    result = int(arg1) + int(arg2)
    return result
if __name__ == "__main__":
    print(pruebas_argparse(args.arg1, args.arg2))