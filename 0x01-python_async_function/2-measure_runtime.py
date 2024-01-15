#!/usr/bin/env python
"""module to measure time"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime
    Keyword arguments:
    n: number of times
    mex_delay: delays
    Return: total time dive by number of times
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total = end - start
    return total/n
