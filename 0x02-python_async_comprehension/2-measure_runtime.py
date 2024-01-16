#!/usr/bin/env python3
"""module for parell comprehesions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Run time for four parallel comprehensions
    Returns: measure of the total runtime
    """
    start = time.time()
    task = await asyncio.gather(async_comprehension(),
                                async_comprehension(),
                                async_comprehension(),
                                async_comprehension())

    end = time.time()
    total = end - start
    return total
