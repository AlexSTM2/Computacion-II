import mmap, os, argparse, signal, time, sys

def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    args = parser.parse_args()
    path_search(args = args)
    Forkeando(args = args)

def Forkeando(args):
    global mapeo
    mapeo = mmap.mmap(-1,15)
    
    #Primer hijo
    ret = os.fork()
    if ret == 0:
        for i in sys.stdin:
            mapeo.write(bytes(i.encode()))
            os.kill(os.getppid(), signal.SIGUSR1)

    #Segundo hijo
    global ret2
    ret2 = os.fork()
    if ret2 == 0:
        signal.signal(signal.SIGUSR1, handler_hijo)
        signal.signal(signal.SIGUSR2, handler_hijo)
        while True:
            signal.pause()
    
    print("Padre esperando señales...")
    signal.signal(signal.SIGUSR1, handler_padre)
    signal.signal(signal.SIGUSR2, handler_padre)

def handler_padre(s,f):
    mapeo.seek(0)
    lectura = mapeo.readline()
    print("Esta es la string ingresada:", lectura.decode())
    print("Enviando señal al segundo hijo...")
    time.sleep(1)
    os.kill(ret2, signal.SIGUSR1)

def handler_hijo(s,f):
    lectura = mapeo.readline().decode.upper()


def path_search(args):
     
    if os.path.exists(args.f):
        pass
    else:
        print("Se creará el archivo especificado en la ruta.")
        archive = open(args.f, "w")
        archive.close()

if __name__ == "__main__":
    Main()