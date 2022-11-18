import asyncio, argparse
import subprocess as sp


async def serv_async(reader, writer):
    while True:
        data = await reader.read(1024)
        com = data.decode()
        out, err = await sub_proc_command(com)
        if data == b"exit":
            print("Connection closed.")
            break
        elif len(out) != 0:
            out = out.decode()
            print("\nOK\n" + out)
            data = "\nOK\n" + out
            writer.write(data.encode())
            
        else:
            err = err.decode()
            print("\nERROR\n" + err)
            data = "\nERROR\n" + err
            writer.write(data.encode())

        
        
async def sub_proc_command(com):
    shell_com = sp.Popen([com], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = shell_com.communicate()
    return out, err


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs',default="localhost",type=str, help="Direccion del Host.")
    parser.add_argument('-p',default=1234,type=int, help="Puerto que el va a usar para iniciar el sv")
    args = parser.parse_args()
    server = await asyncio.start_server(serv_async, args.hs , args.p, reuse_address=True)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())