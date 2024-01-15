#!/usr/bin/env python3
"""module for tasks"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """tasks
    Keyword arguments:
    n: number of times
    max_delay: delays
    Return: sorted delays
    """
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delay = await task
        delays.append(delay)
    return sorted(delays)
