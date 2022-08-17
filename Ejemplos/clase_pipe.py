import os, time

r, w = os.pipe()
ret = os.fork()
if not ret:
    os.write(w, b"Hola mundo")
    os._exit(0)

time.sleep(1)
os.wait()
leido = os.read(r, 100)
print("Leìdo: ", leido.decode())