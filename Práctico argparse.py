import argparse
args =  argparse.ArgumentParser(description="Archivos")
args.add_argument("-i","--file", type=str, help="Archivo a buscar")
args.add_argument("-o","--new_file", type=str, help="Archivo a sobreecribir")
arguments = args.parse_args()

def file_search(file, new_file):
    try:
        f = open(file, "r")
        read_file = f.read()
        print(read_file)
        f.close()
        cond = True
    except FileNotFoundError:
        print("El archivo ingresado, no existe. Ingréselo nuevamente.")
        cond = False
    if cond == True:
        n_file = open(new_file + ".txt", "w")
        n_file.write(read_file)
        n_file.close()
        with open(new_file + ".txt", "r+") as n_file:
            read_new_f = n_file.read()
            print("Su nuevo archivo llamdo", new_file, "tiene el siguiente contenido: \n",
            read_new_f)
file_search(arguments.file, arguments.new_file)