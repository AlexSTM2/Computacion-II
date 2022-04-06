import os,sys, argparse, time

parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
group = parser.add_mutually_exclusive_group()
group_1 = parser.add_mutually_exclusive_group()
parser.add_argument("-n", type=int, help="Nùmero de procesos hijos")
group.add_argument("-v", action="store_true", help="Activa el modo verbose")
group_1.add_argument("-a", action="store_true", help="Muestra la ayuda.")
group = parser.parse_args()
args = parser.parse_args()
group1 = parser.parse_args()

def forkeando(n):
    if group1.a is True:
        parser.print_help()
    for i in range(n):
        ret = os.fork()
        if group.v is True and ret == 0:
            print("Starting process", os.getpid())
            time.sleep(1)
            suma(os.getpid())
            time.sleep(0.5)
            print("Ending process", os.getpid())
            os._exit(0)
        elif ret == 0:
            os._exit(0)
    for i in range(n):
        os.wait()
        
def suma(pid):
    suma = 0
    i = 2
    while i <= int(pid):
        if i % 2 == 0:
            suma += i
        i += 1
    print("PID:", pid, "Suma:",suma)

forkeando(args.n)