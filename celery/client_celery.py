import click, socket, sys, json, numpy
import matrix_from_arch as mfa
@click.command()
@click.option("--h", help="Host.", prompt="Enter the host: ")
@click.option("--p", help="Port.", prompt="Enter the port: ", type=int)
@click.option("--m", prompt="Enter the file name: ", type=str)
@click.option("--c", prompt="Enter the calc funcion: ", type=str)
def main(h, p,m,c):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((h,p))
    print(f"Data sent to: {h} in port {p}")
    m, rows, columns = mfa.get_list(m)
    data = json.dumps([m,c])
    s.send(data.encode())
    result_list = []
    for i in range(len(m)):
        std = s.recv(1024)
        result_list.append(std.decode())
    result_list = numpy.array(result_list).reshape(rows, columns)
    print(result_list)

if __name__ == "__main__":
    main()