import code
from concurrent.futures import thread
import sys, queue, time, codecs
import threading as th

queue = queue.LifoQueue()
def Main():
#Defino mi Main
    
    threads_list = []
    th1 = th.Thread(target=thread_1_job, daemon=True)
    th2 = th.Thread(target=thread_2_job, daemon=True)
    threads_list.append(th1)
    threads_list.append(th2)
    global code
    code = False
    for thread in threads_list:
        thread.start()
    for thread in threads_list:
        thread.join()    

def thread_1_job():
    for stdin in sys.stdin:
        if stdin[:5] != "break":
            queue.put(stdin)
            time.sleep(0.3)
            coded_msg = queue.get()
            print(f"Reading the queue: {coded_msg}")
            
        else:
            print("Thread 1 finishing...")
            queue.put(stdin)
            sys.exit(0)

def thread_2_job():
    
    while True:
        time.sleep(0.5)
        msg = queue.get()
        # print("Entrando a thread 2")
        if msg[:5] != "break":
            print(f"Thread 2 working on {msg} ")
            queue.put(codecs.encode(msg, 'rot_13'))
            queue.task_done()
            if queue.empty():
                break
        else:
            print("Thread 2 finishing...")
            break
    
    
if __name__ == "__main__":
    Main()