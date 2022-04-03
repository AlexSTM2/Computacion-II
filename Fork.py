import os,sys, argparse
parser = argparse.ArgumentParser(description="Comandos")
parser.add_argument("-n", "--num", type=int, help="Nùmero de procesos hijos")
# parser.add_argument("-h", "--help", type=str, help="Ayuda")
# parser.add_argument("-v", "--verb", type=str, help="Modo verboso")
args = parser.parse_args()
def forkeando(num):
    for i in range(num):
        ret = os.fork()
    global pid, ppid
    pid = os.getpid()
    ppid = os.getppid()
    print("PID: %d PPID: %d Retorno: %d" % (pid,ppid,ret))

def suma(pid):
    suma = 0
    i = 2
    while i <= int(pid):
        if i % 2 == 0:
            suma += i
        i += 1
    print("Suma:",suma)

      
forkeando(args.num)
suma(pid)