import socketserver as ss, click, json
import multiprocessing as mp
from matrix_tasks import log, pot, root
from celery.result import AsyncResult

@click.command()
@click.option("--h", help="Host.", prompt="Enter the host: ")
@click.option("--p", help="Port.", prompt="Enter the port: ", type=int)
def main(h,p):
    print("Server executed")
    ss.TCPServer.allow_reuse_address = True   
    server = ss.TCPServer((h, p), MyTCPHandler)
    server.serve_forever()

    
class MyTCPHandler(ss.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        data = json.loads(self.data.decode())
        lista_m, func = data[0], data[1]
        print("{} sent:".format(self.client_address[0]), lista_m, func)
        for num in lista_m:
            if func == "pot":
                result = pot.delay(num)
            elif func == "root":
                result = root.delay(num)
            elif func == "log":
                result = log.delay(num)
            else:
                print("Invalid function")
            res = AsyncResult(result.id)
            self.request.sendall(bytes(str(res.get()), "utf-8"))
    
if __name__ == "__main__":
    main()