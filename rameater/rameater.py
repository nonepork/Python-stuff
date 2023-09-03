import psutil
import time

memory_comsume = []

while True:
    if psutil.virtual_memory().available/1000000000 > 1.4:
        memory_comsume.append(bytearray(1024*1024*1000))
    elif psutil.virtual_memory().available/1000000000 < 1.4:
        memory_comsume.pop()
    else:
        continue
    time.sleep(0.1) # In case of python itself comsuming memory

