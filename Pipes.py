import os,sys, argparse, time

#Determino todos los paràmetros
def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    args = parser.parse_args()
    path_search(args = args)
    Pipes(args = args)


def Pipes(args):
    r, w = os.pipe()
    fd1 = open(args.f, "r+")
    for i in fd1.readlines():
        w = os.fdopen(w, 'w')
        w.write(i)
        
        ret = os.fork()
        if ret == 0:
            w.close()
            r = os.fdopen(r)
            print("Hijo leyendo...", os.getpid())
            texto = r.readline()
            r.close()
            w = os.fdopen(w, 'w')
            texto = texto[::-1]
            w.write(texto)
            os._exit(0)
        else:
            w.close()
            time.sleep(5)
            r = os.fdopen(r)
            p_lectura = r.readline()
            print(p_lectura)
             
    
    for g in fd1.readline():
        print(g)
        os.wait()
    fd1.close()

def path_search(args):
     
    if os.path.exists(args.f):
        pass
    else:
        print("Se creará el archivo especificado en la ruta.")
        archive = open(args.f, "w")
        archive.close()

if __name__ == "__main__":
    Main()