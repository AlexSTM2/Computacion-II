import socket, sys, argparse, signal
import multiprocessing as mp

def Main():
    parser = argparse.ArgumentParser(description="Estos son los comandos y sus descripciones")
    parser.add_argument("-d", type=str, help="Ingrese el host.")
    parser.add_argument("-p", type=str, help="Es el puerto a ingresar")
    args = parser.parse_args()
    sockets_ex(args = args)
    

def sockets_ex(args):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = args.d
    port = args.p
    server_socket.bind((host, port))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(3)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    

    while True:
        client_socket, addr = server_socket.accept()
        proc = mp.Process(target=msg_upper, args=(client_socket))
        proc.start()

def msg_upper(c_socket):
    while True:
        data = c_socket.recv(1024)
        data = data.decode("ascii").upper()
        if data[:3] == "BYE":
            print("Saliendo...")
            exit(0)
        print("Se ha recibido: ", data)
        c_socket.send(data.encode("ascii"))
    
if __name__ == "__main__":
    Main()
    
