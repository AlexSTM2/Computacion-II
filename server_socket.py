import click, subprocess, signal
import threading as th
import socketserver as ss
@click.command()
@click.option('--c', type=str, help='We use threading to add concurrency.', prompt="T for threading server/P for a fork server")
@click.option('--p', help="Server port", type=int, prompt="Server port")
def main(c,p):
    HOST, PORT = "localhost", p
    ss.TCPServer.allow_reuse_address = True
    if c[0].lower() == "t":
        print("Thread")
        server_thread = th.Thread(target=threading_service(HOST, PORT))
        server_thread.daemon = True
        server_thread.start()

    elif c[0].lower() == "p":
        print("Fork")
        fork_service(h=HOST, p=PORT)

    else:
        print("Please enter a valid tipe of server concurrency...")

def threading_service(h, p):
    with ThreadedTCPServer((h, p), MyTCPHandler) as server:
        
        server.serve_forever()
        try:
            signal.pause()
        except:
            server.shutdown()

def fork_service(p, h):
    pass

class ThreadedTCPServer(ss.ThreadingMixIn, ss.TCPServer):
    pass

class MyTCPHandler(ss.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024)
        print(self.data.decode().strip() + " recibido")
        self.request.sendall(self.data)
        
if __name__ == "__main__":
    main()