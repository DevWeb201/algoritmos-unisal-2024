from multiprocessing import Process
import time, random

def lanzr():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    time.sleep(x+y)
    print(f"Bola ({x},{y})")

if __name__ == '__main__':
    procesos = []
    for _ in range(7):
        procesos = Process(target=lanzr)
        procesos.start()
        procesos.append(procesos)

    for proceso in procesos:
        proceso.join()
