<<<<<<< HEAD
import click, socket, subprocess, threading

@click.command()
@click.option("--h", help="Host.", prompt="Enter the host: ")
@click.option("--p", help="Port.", prompt="Enter the port: ", type=int)
def main(h, p):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((h,p))
    print(f"Conected to: {h} in port {p}")
    while True:
        com = str(input("Enter the command to execute: "))
        s.send(com.encode())
        std = s.recv(1024)
        print(std.decode())
=======
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
>>>>>>> 666ba753176518031b17211e9207267cd33b926e

if __name__ == "__main__":
    main()