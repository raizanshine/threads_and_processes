#!/usr/bin/env python
import time
from multiprocessing import cpu_count, Process
from threading import Thread

from timeit import timeit

CPU_CORES_COUNT = cpu_count()


def target_function():
    time.sleep(1)


@timeit
def do_consequently():
    for i in range(CPU_CORES_COUNT + 1):
        target_function()


@timeit
def do_with_threads():
    threads = []
    for i in range(CPU_CORES_COUNT + 1):
        thread = Thread(target=target_function)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


@timeit
def do_with_processes():
    processes = []
    for i in range(CPU_CORES_COUNT + 1):
        process = Process(target=target_function)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    do_consequently()
    do_with_threads()
    do_with_processes()
