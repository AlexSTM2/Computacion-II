import os,sys, argparse, time

#Determino todos los paràmetros
def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    args = parser.parse_args()
    path_search(args = args)
    Pipes(args = args)


def Pipes(args):
    
    fd1 = open(args.f, "r+")
    for i in fd1.readlines():
        r1, w1 = os.pipe()
        r2, w2 = os.pipe()
        ret = os.fork()
        if not ret:
            time.sleep(0.5)
            r1_h = os.fdopen(r1, 'r')
            texto = r1_h.readline()
            r1_h.close()
            os.close(r2)
            w2_h = os.fdopen(w2, 'w')
            texto = texto.rstrip("\n")
            texto = texto[::-1]
            w2_h.write(texto)
            w2_h.close()
            os._exit(0)
        else:
            os.close(r1)
            w1_p = os.fdopen(w1, 'w')
            w1_p.write(i)
            w1_p.close()
            #Padre lee
            time.sleep(1)
            os.close(w2)
            r2_p = os.fdopen(r2, 'r')
            p_lectura = r2_p.readline()
            print(p_lectura)
            r2_p.close()

    for g in fd1.readline():
        os.wait()
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