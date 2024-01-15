#!/usr/bin/env python3
"""module for multiple tasks"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """xecute multiple coroutines at the same
    Keyword arguments:
    n: number of times
    max_delay: delays
    Return: sorted delays
    """
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delay = await task
        delays.append(delay)
    return sorted(delays)
