import os,sys, argparse, time

#Determino todos los paràmetros
def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    args = parser.parse_args()
    path_search(args = args)
    Pipes(args = args)


def Pipes(args):
    r1, w1 = os.pipe()
    r2, w2 = os.pipe()
    fd1 = open(args.f, "r")
    for i in fd1.readlines():
        
        ret = os.fork()
        if ret == 0:
            os.close(w1)
            r1 = os.fdopen(r1, 'r')
            print("Hijo leyendo...", os.getpid())
            texto = r1.readline()
            r1.close()
            w2 = os.fdopen(w2, 'w')
            texto = texto[::-1]
            w2.write(texto)
            os._exit(0)
        else:
            os.close(r1)
            w1 = os.fdopen(w1, 'w')
            w1.write(i)
            w1.close()
            #Padre lee
            time.sleep(1)
            os.close(w2)
            r2 = os.fdopen(r2, 'r')
            p_lectura = r2.readline()
            print(p_lectura)
            r2.close()
            os.wait()
            sys.exit(0)

    # for g in fd1.readline():
    #     print(g)
    #     os.wait()
    fd1.close()

def path_search(args):
     
    if os.path.exists(args.f):
        pass
    else:
        print("Se creará el archivo especificado en la ruta y le escribirá un"
        "texto de ejemplo")
        archive = open(args.f, "w")
        archive.close()
        fd = open(args.f, "a")
        with open(args.f, "a") as fd:
            fd.write("Hola mundo\n"
            "este es un archivo\n"
            "de ejemplo\n")
        
if __name__ == "__main__":
    Main()