#!/usr/bin/env python
from multiprocessing import cpu_count, Process
from threading import Thread

from timeit import timeit

CPU_CORES_COUNT = cpu_count()
FACTORIAL_NUMBER = 50000


def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result 


@timeit
def do_consequently():
    for i in range(CPU_CORES_COUNT + 1):
        factorial(FACTORIAL_NUMBER)


@timeit
def do_with_threads():
    threads = []
    for i in range(CPU_CORES_COUNT + 1):
        thread = Thread(target=factorial, args=(FACTORIAL_NUMBER,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


@timeit
def do_with_processes():
    processes = []
    for i in range(CPU_CORES_COUNT + 1):
        process = Process(target=factorial, args=(FACTORIAL_NUMBER,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    do_consequently()
    do_with_threads()
    do_with_processes()
