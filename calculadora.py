#Ejercicio de práctica de la calculadora
import sys, getopt

arguments = sys.argv[1:]

def calc(op):
    result = ""
    options = "o:n:m:"
    print("Argumentos:", op)  
    (opts, ar) = getopt.getopt(op, options)
    print(opts)
    for opt, arg in opts:
        if opt == "-o":
            print("Operación a realizar:", arg)
            op_math = arg
        elif opt == "-n":
            print("Primer número:", arg)
            f_num = (arg)
        else:
            print("Segundo número:", arg)
            s_num = (arg)
    if f_num.isnumeric() and s_num.isnumeric():
        print("Números ingresados correctamente")
        if op_math == "+":
            result = int(f_num) + int(s_num)
        elif op_math == "-":
            result = int(f_num) - int(s_num)
        elif op_math == "*":
            result = int(f_num) * int(s_num)
        elif op_math == "/":
            if s_num != "0":
                result = int(f_num) / int(s_num)
            else:
                print("No se puede realizar un división por cero, ingrese los datos nuevamente.")
        else:
            print("Los datos que ha ingresado son inválidos, intente nuevamente.")
    if result != "":
        print("El resultado de su operación es:", result)   


calc(arguments)
