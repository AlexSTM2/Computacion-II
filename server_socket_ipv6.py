import socket
import click, subprocess, signal
import threading as th
import socketserver as ss
import multiprocessing as mp

@click.command()
@click.option('--c', type=str, help='We can use both threading and multiprocessing modes.', prompt="T for threading server/P for a fork server")
@click.option('--p', help="Server port", type=int, prompt="Server port")
def main(c,p):
    global HOST, PORT
    HOST, PORT = "localhost", p
    directions = socket.getaddrinfo("localhost", p, socket.AF_UNSPEC, socket.SOCK_STREAM)
    threads = []
    for direction in directions:
        threads.append(th.Thread(target=service, args=(direction,c)))
    for h in threads:
        h.start()
    for h in threads:
        h.join()

def service(direction, c):

    if direction[0] == socket.AF_INET and c.lower() == "t":
        print("IPv4")
        server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    elif direction[0] == socket.AF_INET and c.lower() == "p":
        print("IPv4")
        server = ForkedTCPServer((HOST, PORT), MyTCPHandler)
    elif direction[0] == socket.AF_INET6 and c.lower() == "t":
        print("IPv6")
        server = ThreadedTCPServer6((HOST, PORT), MyTCPHandler)
    elif direction[0] == socket.AF_INET6 and c.lower() == "p":
        print("IPv6")
        server = ForkedTCPServer6((HOST, PORT), MyTCPHandler)
    else:
        print("Invalid parameter")

    server.serve_forever()
    try:
        signal.pause()
    except:
        server.shutdown()

def sub_proc_command(com):
    shell_com = subprocess.Popen([com], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = shell_com.communicate()
    return out, err

class ThreadedTCPServer(ss.ThreadingMixIn, ss.TCPServer):
    pass

class ForkedTCPServer(ss.ForkingMixIn, ss.TCPServer):
    pass

class ThreadedTCPServer6(ss.ThreadingMixIn, ss.TCPServer):
    address_family = socket.AF_INET6
    pass

class ForkedTCPServer6(ss.ForkingMixIn, ss.TCPServer):
    address_family = socket.AF_INET6
    pass

class MyTCPHandler(ss.BaseRequestHandler):
    
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            com = self.data.decode()
            out, err = sub_proc_command(com)
            if len(out) != 0:
                out = out.decode()
                print("\nOK\n" + out)
                data = "\nOK\n" + out
                self.request.sendall(data.encode())
            else:
                err = err.decode()
                print("\nERROR\n" + err)
                data = "\nERROR\n" + err
                self.request.sendall(data.encode())

if __name__ == "__main__":
    ss.TCPServer.allow_reuse_address = True
    main()