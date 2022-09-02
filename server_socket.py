import click, subprocess, signal
import threading as th
import socketserver as ss
import multiprocessing as mp
@click.command()
@click.option('--c', type=str, help='We use threading to add concurrency.', prompt="T for threading server/P for a fork server")
@click.option('--p', help="Server port", type=int, prompt="Server port")
def main(c,p):
    HOST, PORT = "localhost", p
    
    if c[0].lower() == "t":
        print("Thread")
        server_thread = th.Thread(target=threading_service(HOST, PORT))
        server_thread.daemon = True
        server_thread.start()

    elif c[0].lower() == "p":
        print("Fork")
        proc = mp.Process(target=fork_service(HOST,PORT))
        proc.daemon = True
        proc.start()

    else:
        print("Please enter a valid tipe of server concurrency...")

def threading_service(h, p):
    with ThreadedTCPServer((h, p), MyTCPHandler) as server:
        
        server.serve_forever()
        try:
            signal.pause()
        except:
            server.shutdown()

def fork_service(h, p):
    with ForkedTCPServer((h,p), MyTCPHandler) as server:
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