#Ejercicio de práctica de la calculadora
import sys, getopt

arguments = sys.argv[1:]

def calc(op):
    result = ""
    options = "o:n:m:"  
    (opt, arg) = getopt.getopt(op, options) 
    for (opt, ar) in opt:
        if opt == "-o":
            print("Operación a realizar:", ar)
            op_math = ar
        elif opt == "-n":
            print("Primer número:", ar)
            f_num = (ar)
        else:
            print("Segundo número:", ar)
            s_num = (ar)
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
