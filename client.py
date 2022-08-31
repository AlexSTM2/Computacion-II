import click
import socket

from prompt_toolkit import prompt

@click.command()
@click.option("--h", help="The host", prompt="Host: ")
@click.option("--p", help="Port", prompt="Port: ")
def main(h,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
    #Completar para tagear
    print("Connecting.")
    s.connect((h, p))   
    msg = s.recv(1024)                                     
    s.close()
    print("Cerrando conexion")

if __name__ == "__main__":
    main()