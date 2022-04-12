import os,sys, argparse, time
import string
#Determino todos los paràmetros
def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-n", type=int, help="Nùmero de procesos hijos.")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    parser.add_argument("-r",type=int, help="Repeticiones de las letras")
    group.add_argument("-v", action="store_true", help="Activa el modo verbose.")
    group = parser.parse_args()
    args = parser.parse_args()
    forkeando(args)

def forkeando(args):
    if args.n and args.f and args.r:
        path_search(args)
        ABC_List = list(string.ascii_uppercase)
        for i in range(args.n):
            letra = ABC_List[i]
            ret = os.fork()
            if ret == 0:
                    escritura(letra, args)
                    os._exit(0)
                
        for i in range(args.n):
            os.wait()
    else:
        print("No ha ingresado correctamente los paràmetros")


def escritura(letra,args):
    pid = os.getpid()
    for g in range(0, args.r):
        with open(f"{args.f}", "a") as fd:
            fd.write(str(letra))
            fd.flush()
            time.sleep(1)
        if args.v:
            print(f"El proceso {pid}", "Està escribiendo la letra", letra)
        
def path_search(args):
     
    if os.path.exists(args.f):
        pass
    else:
        archive = open(args.f, "w")
        archive.close()

if __name__ == "__main__":
    Main()