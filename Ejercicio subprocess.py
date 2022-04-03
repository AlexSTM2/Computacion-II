import subprocess
import datetime
import argparse

args = argparse.ArgumentParser(description="Archivos")
args.add_argument("-c", "--command", type=str)
args.add_argument("-f", "--output", type=str)
args.add_argument("-l", "--log", type=str)
argument = args.parse_args()


def subproc(command, o_file, l_file):
    out_file = open(o_file + ".txt", "w")
    out_file.write("Salida estándar.")
    command_exc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE
    , stderr=subprocess.PIPE, universal_newlines=True)
    out, err = command_exc.communicate()
    print(out, err)

    if command_exc.returncode == 0:
        print("Comando ejecutado.")
    else:
        print("Comando erróneo.")

subproc(argument.command, argument.output, argument.log)

