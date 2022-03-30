import sys, getopt


(opt,arg) = getopt.getopt(sys.argv[1:], "o:n:m:")
# -a -b algo -c --opcion1 --opcion2="holamundo"

#las que van con ":" como la b: son opciones que reciben argumentos, igual que en C
#el = en las opciones largas es equivalente al : en las cortas

print("opciones: ", opt)
print("argumentos: ", arg)