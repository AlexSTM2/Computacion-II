
import os,sys, argparse, time
import multiprocessing as mp
import math
#Determino todos los paràmetros

def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-p", type=int, help="Nùmero de procesos.")
    parser.add_argument("-f", type=str, help="Archivo con la matriz a utilizar.")
    parser.add_argument("-c",type=str, help="Operación a realziar.")
    args = parser.parse_args()
    mpool(args)

def mpool(args):
    with open(args.f, "r+") as fd:
        lines = fd.readlines() 
    pool = mp.Pool(processes=args.p)
    
    if args.c == "raiz":
        for line in lines:
            resultados = pool.map(raiz, line.split())
            print(resultados)

    elif args.c == "pot":
        for line in lines:
            resultados = pool.map(pot, line.split())
            print(resultados)

    elif args.c == "log":
        for line in lines:
            resultados = pool.map(log, line.split())
            print(resultados)
    
    else:
        print("Ingrese un argumento correcto")

def raiz(num):
    resultado = math.sqrt(int(num))
    return resultado

def pot(num):
    resultado = int(num)**2
    return resultado

def log(num):
    resultado = math.log10(int(num))
    return resultado

if __name__ == "__main__":
    Main()
