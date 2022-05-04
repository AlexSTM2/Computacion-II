import mmap, os, argparse, signal, time, sys

def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-f", type=str, help="Ingrese el archivo a buscar.")
    global args
    args = parser.parse_args()
    path_search(args = args)
    Forkeando(args = args)

def Forkeando(args):
    global pid_lista
    pid_lista = []
    global mapeo
    mapeo = mmap.mmap(-1,1024)
    print("Padre esperando señales...")
    #Primer hijo
    for i in range(2):
        ret = os.fork()
        if ret == 0:
            #i == 0 Es el primer hijo
            if i == 0:
                for i in sys.stdin:
                    if i[:3] == "bye":
                        os.kill(os.getppid(), signal.SIGUSR2)
                        print("Padre mueriendo..")
                        sys.exit(0)
                    mapeo.write(i.encode())
                    os.kill(os.getppid(), signal.SIGUSR1)
            #Esto lo hace el segundo hijo
            else:
                signal.signal(signal.SIGUSR1, handler_hijo)
                signal.signal(signal.SIGUSR2, handler_hijo)
                while True:
                    signal.pause()
        else:
            pid_lista.append(ret)

    #El padre forkea de nuevo para crear un segundo hijo
        
    signal.signal(signal.SIGUSR1, handler_padre)
    signal.signal(signal.SIGUSR2, handler_padre)
    signal.pause()
    os.wait()
def handler_padre(s,f):
    if s == signal.SIGUSR1:
        lectura = mapeo.readline()
        print("Esta es la string ingresada:", lectura.decode())
        print("Enviando señal al segundo hijo...")
        time.sleep(1)
        os.kill(pid_lista[1], signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(pid_lista[1], signal.SIGUSR2)
        os.wait()
        sys.exit(0)

def handler_hijo(s,f):
    if s == signal.SIGUSR1:
        lectura = mapeo.readline().decode().upper()
        fd = open(args.f, "a")
        fd.write(lectura)
        fd.close()
        print("Hijo 2 leyendo:", lectura)
    elif s == signal.SIGUSR2:
        print("H2 muriendo...")
        sys.exit(0)

def path_search(args):
     
    if os.path.exists(args.f):
        pass
    else:
        print("Se creará el archivo especificado en la ruta.")
        archive = open(args.f, "w")
        archive.close()

if __name__ == "__main__":
    Main()