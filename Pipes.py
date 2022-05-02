import os,sys, argparse, time

#Determino todos los paràmetros
def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    args = parser.parse_args()
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
            print("Hijo leyendo...")
            texto = r.readline()
            time.sleep(0.5)
            r.close()
            w = os.fdopen(w, 'w')
            texto = texto[::-1]
            w.write(texto)
            os._exit(0)
        else:
            w.close()
            time.sleep(1)
            r = os.fdopen(r)
            p_lectura = r.readline()
            print(p_lectura)
             
    fd1.close()
    for g in fd1.readline():
        print(g)
        os.wait()


if __name__ == "__main__":
    Main()