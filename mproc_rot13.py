#Crear dos hijos con multiproccesing 
#Uno de los hijos lee por stdin lo ingresado 
#y debe escribirlo en un mp.Pipe()
#el segundo hijo lee por el mismo pipe, lo encripta en rot13, y lo almacena
#en una qeue.
#El primer hijo debe leer la cola de msj y mostrar el contenido.

import os, sys, time
import multiprocessing as mp


def child1_w(pipe_s, q, stdin):
    #Ingreso por la stdin al hijo 1
    sys.stdin = os.fdopen(stdin)
    for input in sys.stdin:
        if input[:5] == "break":
            
            break
        else:
            pipe_s.send(input)
            print("Primer hijo escribiendo...", input)
            print("Hijo leyendo la cola:")
            time.sleep(0.3)
            print(q.get())

def child2_r(pipe_r, q):
    #Arreglar esto, al poner el break, se me quede esperando el recv
    while cond == True:
        time.sleep(1)
        print("Hijo leyendo: ")
        msg = str(pipe_r.recv())
        q.put(msg)

if __name__ == "__main__":
    global cond
    cond = True
    fd = sys.stdin.fileno()
    #Creo el pipe en el padre y la queue
    pipe_s, pipe_r = mp.Pipe()
    q = mp.Queue()
    proc1 = mp.Process(target = child1_w, args = (pipe_s, q, fd))
    proc2 = mp.Process(target = child2_r, args = (pipe_r, q))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    print("Saliendo")