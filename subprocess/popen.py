import subprocess as sp
import click, os, time


def path_check(f_file, s_file):

    files = [f_file, s_file]   
    for file in files:
        if os.path.exists(file):
            pass
        else:   
            print("The file doesn't exist.It has been created.")
            f = open(f_file, "w")
            f.close()

def com_execute(com):
    shell_com = sp.Popen([com], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = shell_com.communicate()
    return out, err


def file_write(f_file, s_file, com, out, err):
    act_time = time.strftime("%c")
    f_log = open(s_file, "a")
    f_out = open(f_file, "a")
    out = out.decode()
    err = err.decode()

    if len(out) != 0:
        print("\nOK\n" + out)
        f_log.write(f"\nDatetime {act_time}: Command {com} executed correctly.")
        f_out.write(f"\n{out}")

    else:
        print("\nERROR\n" + err)
        f_log.write(f"\nDatetime {act_time}: Command {com} executed with errors.")

    f_log.close()
    f_out.close()

@click.command()
@click.option("-f", help="File to write the output.", prompt="Enter the file to write the output: ")
@click.option("-l", help="File to write the log.", prompt="Enter the file to write the log: ")
@click.option("-c", help="Command to execute.", prompt="Enter the command to execute: ", type=str)
def main(c, f, l):
    path_check(f, l)
    out, err = com_execute(c)
    file_write(f, l, c, out, err)

if __name__ == "__main__":
    main()